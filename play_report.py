#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# play_report.py (play test 0001, bubble p1-08, 23 Nov 2026) - what a play test session was: "21 games in 47 minutes, 3 never got past level 1".
# Reads only; changes nothing.
#
# Reads the play record LIB_LOADING_SCREEN writes (Documents/My Games/Vibecode3D/play_record.txt):
#   date time user game engine event level seconds score fps
# event: start (a game opens, level 1 or the level it starts on), level (a new level: "level" is the one
# entered, "seconds" the time in the level just left), end (game over), quit (the window went or Reset).
#
# Use:
#   python3 -I play_report.py                     the owner's record (Windows Documents), last session
#   python3 -I play_report.py PACK_FOLDER         a tester pack (LIB_BAT/tester_pack.bat): record + notes
#   python3 -I play_report.py FILE --all          every session, not only the last
#   python3 -I play_report.py --date 2026-11-23   the sessions of that day
#   --gap 30                                       minutes with no line that start a new session (default 30)
#   --out report.md                                also write the report to a file

import argparse
import glob
import os
import statistics
import sys
from datetime import datetime, timedelta

GAP_MIN = 30


def find_record(path):
    """The play_record.txt: the given file, inside the given folder, else the Windows Documents one."""
    if path:
        if os.path.isfile(path):
            return path
        hits = sorted(glob.glob(os.path.join(path, "**", "play_record.txt"), recursive=True))
        return hits[0] if hits else None
    hits = sorted(glob.glob("/mnt/c/Users/*/Documents/My Games/Vibecode3D/play_record.txt"))
    home = os.path.expanduser("~/Documents/My Games/Vibecode3D/play_record.txt")
    if os.path.isfile(home):
        hits.append(home)
    return hits[0] if hits else None


def when(date, time):
    for fmt in ("%Y-%m-%d %I:%M:%S %p", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(date + " " + time, fmt)
        except ValueError:
            pass
    return None


def num(text):
    try:
        return float(text)
    except (TypeError, ValueError):
        return None


def read_record(path):
    rows = []
    with open(path, encoding="utf-8", errors="replace") as f:
        for n, line in enumerate(f):
            parts = line.rstrip("\r\n").split("\t")
            if n == 0 and parts[:1] == ["date"]:
                continue
            if len(parts) < 7:
                continue
            parts += [""] * (10 - len(parts))
            t = when(parts[0], parts[1])
            if t is None:
                continue
            rows.append({
                "t": t, "user": parts[2], "game": parts[3], "engine": parts[4], "event": parts[5],
                "level": num(parts[6]), "seconds": num(parts[7]), "score": parts[8], "fps": num(parts[9]),
            })
    rows.sort(key=lambda r: r["t"])
    return rows


def runs_of(rows):
    """One run = a game from its start line to its end/quit line (or to the next start: no end line)."""
    runs, cur = [], None
    for r in rows:
        if r["event"] == "start" or cur is None or cur["game"] != r["game"] or cur["closed"]:
            if cur is not None:
                runs.append(cur)
            cur = {"game": r["game"], "engine": r["engine"], "user": r["user"], "first": r["t"],
                   "last": r["t"], "seconds": 0.0, "top": r["level"] or 1, "levels": 0,
                   "closed": False, "how": "open", "fps": [], "score": ""}
            if r["event"] == "start":
                continue
        cur["last"] = r["t"]
        if r["seconds"] is not None:
            cur["seconds"] += r["seconds"]
        if r["fps"] is not None:
            cur["fps"].append(r["fps"])
        if r["level"] is not None and r["level"] > cur["top"]:
            cur["top"] = r["level"]
        if r["score"]:
            cur["score"] = r["score"]
        if r["event"] == "level":
            cur["levels"] += 1
        elif r["event"] in ("end", "quit"):
            cur["closed"] = True
            cur["how"] = r["event"]
    if cur is not None:
        runs.append(cur)
    for run in runs:      # a run with no end line: count the time we saw (its last level is lost)
        if run["seconds"] == 0:
            run["seconds"] = (run["last"] - run["first"]).total_seconds()
    return runs


def sessions_of(runs, gap_min):
    out, cur = [], []
    for run in runs:
        if cur and run["first"] - max(r["last"] for r in cur) > timedelta(minutes=gap_min):
            out.append(cur)
            cur = []
        cur.append(run)
    if cur:
        out.append(cur)
    return out


def notes_in(folder, first, last):
    """Tester notes (tell_YYYY-MM-DD_HHMMSS.txt under Games/<Game>/LIB_LLM) made during the session."""
    found = []
    if not folder or not os.path.isdir(folder):
        return found
    for path in sorted(glob.glob(os.path.join(folder, "**", "tell_*.txt"), recursive=True)):
        stamp = os.path.basename(path)[5:22]
        try:
            t = datetime.strptime(stamp, "%Y-%m-%d_%H%M%S")
        except ValueError:
            continue
        if first - timedelta(minutes=5) <= t <= last + timedelta(minutes=5):
            game = os.path.basename(os.path.dirname(os.path.dirname(path)))
            with open(path, encoding="utf-8", errors="replace") as f:
                keys = dict(l.rstrip("\r\n").split("\t", 1) for l in f if "\t" in l)
            text = keys.get("tell", "").strip()
            if keys.get("state"):
                text += f"  (state {keys['state']})"
            found.append((t, game, text))
    return found


def minutes(sec):
    return f"{sec / 60:.1f}"


def report(session, notes):
    first = min(r["first"] for r in session)
    last = max(r["last"] for r in session)
    games = {}
    for run in session:
        g = games.setdefault(run["game"], {"runs": 0, "sec": 0.0, "top": 1, "levels": 0, "hows": [],
                                           "fps": [], "engine": set(), "score": ""})
        g["runs"] += 1
        g["sec"] += run["seconds"]
        g["top"] = max(g["top"], run["top"])
        g["levels"] += run["levels"]
        g["hows"].append(run["how"])
        g["fps"] += run["fps"]
        g["engine"].add(run["engine"])
        g["score"] = run["score"] or g["score"]
    wall = (last - first).total_seconds()
    played = sum(g["sec"] for g in games.values())
    stuck = [n for n, g in games.items() if g["top"] <= 1]
    open_runs = sum(h == "open" for g in games.values() for h in g["hows"])
    users = sorted({r["user"] for r in session if r["user"]})

    lines = [f"## {first:%Y-%m-%d} {first:%H:%M} - {last:%H:%M}" + (f"  ({', '.join(users)})" if users else ""),
             "",
             f"**{len(games)} games in {minutes(wall)} minutes** ({minutes(played)} minutes in levels, "
             f"{len(session)} starts). {len(stuck)} never got past level 1."
             + (f" {open_runs} start(s) with no quit or game-over line (closed hard or crashed?)." if open_runs else ""),
             "",
             "| game | engine | starts | minutes | top level | level changes | ended | fps | score |",
             "|---|---|---|---|---|---|---|---|---|"]
    for name, g in sorted(games.items(), key=lambda kv: -kv[1]["sec"]):
        fps = f"{statistics.median(g['fps']):.0f}" if g["fps"] else ""
        hows = ", ".join(f"{h} x{g['hows'].count(h)}" if g["hows"].count(h) > 1 else h
                         for h in dict.fromkeys(g["hows"]))
        lines.append(f"| {name} | {'/'.join(sorted(g['engine']))} | {g['runs']} | {minutes(g['sec'])} | "
                     f"{g['top']:g} | {g['levels']} | {hows} | {fps} | {g['score']} |")
    if stuck:
        lines += ["", "Never past level 1: " + ", ".join(sorted(stuck))]
    if notes:
        lines += ["", f"### Notes written while playing ({len(notes)})", ""]
        for t, game, text in notes:
            lines.append(f"- {t:%H:%M:%S} **{game}**: {text}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Report on Vibecode3D play sessions from play_record.txt")
    ap.add_argument("path", nargs="?", help="play_record.txt, or a folder holding one (a tester pack)")
    ap.add_argument("--all", action="store_true", help="every session, not only the last")
    ap.add_argument("--date", help="only sessions starting that day (YYYY-MM-DD)")
    ap.add_argument("--gap", type=float, default=GAP_MIN, help="minutes of quiet that start a new session")
    ap.add_argument("--out", help="also write the report here")
    a = ap.parse_args()

    rec = find_record(a.path)
    if not rec:
        sys.exit("No play_record.txt found" + (f" in {a.path}" if a.path else "") + ".")
    rows = read_record(rec)
    if not rows:
        sys.exit(f"{rec}: no play lines yet.")
    sessions = sessions_of(runs_of(rows), a.gap)
    if a.date:
        sessions = [s for s in sessions if f"{s[0]['first']:%Y-%m-%d}" == a.date]
    elif not a.all:
        sessions = sessions[-1:]
    if not sessions:
        sys.exit("No session matches.")
    notes_root = a.path if a.path and os.path.isdir(a.path) else None

    parts = [f"# Play report\n\nFrom `{rec}`: {len(rows)} lines.\n"]
    for s in sessions:
        notes = notes_in(notes_root, min(r["first"] for r in s), max(r["last"] for r in s))
        parts.append(report(s, notes))
    text = "\n\n".join(parts) + "\n"
    print(text)
    if a.out:
        with open(a.out, "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    main()
