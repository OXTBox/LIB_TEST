#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# game_scan.py: one table of every game card script (play test 0001, bubble p1-01, 23 Nov 2026).
# Reads only; it changes no game. Counting is surer as code than as a model reading 80 files.
#
#   python3 -I game_scan.py              -> writes game_scan.tsv + GAME_SCAN.md beside this file
#   python3 -I game_scan.py --no-comfy   -> leaves out the generated Comfy Games
#   python3 -I game_scan.py --out DIR    -> writes them somewhere else
#
# What it finds (by reading the text, so every column is a good guess, not a proof):
#   prefix      the card's own handler prefix (the X of `on X.StartLevel`, else the most used X.)
#   levels      how many levels, and how it knew: header comment ("5 levels"), a constant
#               (kLevels = 5), or the biggest number the level is compared with (sLevel >= 5)
#   keys        keysDown (polls the keys each frame) and/or the messages it handles
#   tab/arrows  whether it reads Tab (65289) or the arrows (65361-65364, arrowKey)
#   libraries   the .livecodescript files it names (most are loaded with `start using`)
#   level calls (for p1-13) every line that calls its own <Prefix>.StartLevel, the handler it is in,
#               and what runs after it in that handler before it leaves: "nothing" = the call is the
#               last thing done, else the first statement after it (that code may expect the new
#               level at once), or "(the loop goes on)". Branches that do not run are skipped.
import argparse
import collections
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECTS = os.path.dirname(HERE)
SOURCES = [  # (source label, folder, file pattern)
    ("LIB_GAMES", os.path.join(PROJECTS, "LIB_GAMES", "Vibecode3D_Games"), r"Vibecode3D_Play_(.+)\.livecodescript$"),
    ("LIB_GAD", os.path.join(PROJECTS, "LIB_GAD", "GeneticAnomaly"), r"Vibecode3D_Play_(.+)\.livecodescript$"),
    ("LIB_COMFY", os.path.join(PROJECTS, "LIB_COMFY", "games"), r"Vibecode3D_Play_(.+)\.livecodescript$"),
]
CATALOG = os.path.join(PROJECTS, "LIB_PUBLIC", "install", "catalog.tsv")
# prefixes that belong to the engine or the libraries, never a card's own
ENGINE = {"Game", "Scene", "Entity", "Mesh", "Camera", "HUD", "FX", "Particles", "Collision", "Vibe",
          "Input", "Sound", "Music", "Loading", "Player", "Con", "Lean", "Cull", "Menu", "Data", "Map",
          "Bit", "CellMap", "Anim", "Seq", "Stamina", "Skin", "Light", "Line", "Text", "Math", "Debug",
          "Timer", "Path", "Physics", "Body", "Box2D", "Emit", "Power", "Uni", "Ig"}

R_HANDLER = re.compile(r"^\s*(?:private\s+)?(on|command|function|before|after)\s+([A-Za-z0-9_.]+)", re.I)
R_END = re.compile(r"^\s*end\s+([A-Za-z0-9_.]+)\s*$", re.I)
R_LIB = re.compile(r'"([^"]*\.livecodescript)"')
R_HEADER_LEVELS = re.compile(r"\b(\d+)\s+levels?\b", re.I)
R_CONST_LEVELS = re.compile(r"^\s*constant\s+k\w*(?:Levels|LevelCount|MaxLevel|LastLevel)\w*\s*=\s*(\d+)", re.I | re.M)
R_COMPARE = re.compile(r"\b[sgt]\w*Level\b\s*(>=|>|=|is)\s*(\d+)\b")
MSG_KEYS = ["keyDown", "keyUp", "rawKeyDown", "rawKeyUp", "arrowKey", "tabKey", "returnKey",
            "enterKey", "escapeKey", "deleteKey", "backspaceKey", "functionKey", "commandKeyDown"]
STRUCTURE = re.compile(r"^(end\s+(if|repeat|switch)|else|break|exit\s+repeat|next\s+repeat|"
                       r"exit\s+[A-Za-z0-9_.]+|pass\s+[A-Za-z0-9_.]+|exit\s+to\s+top|end\s+try|catch\b.*)$", re.I)


def strip_comment(line):
    """The line without its -- or # comment (strings kept)."""
    out, q = [], False
    i = 0
    while i < len(line):
        c = line[i]
        if c == '"':
            q = not q
        elif not q and (line.startswith("--", i) or c == "#"):
            break
        out.append(c)
        i += 1
    return "".join(out).rstrip()


def catalog():
    names = {}
    if os.path.exists(CATALOG):
        with open(CATALOG, encoding="utf-8") as f:
            next(f, None)
            for line in f:
                p = line.rstrip("\n").split("\t")
                if len(p) >= 4:
                    names[p[1]] = (p[2], p[3])
    return names


def find_games(with_comfy):
    out = []
    for label, folder, pat in SOURCES:
        if label == "LIB_COMFY" and not with_comfy:
            continue
        if not os.path.isdir(folder):
            continue
        for fn in sorted(os.listdir(folder)):
            m = re.match(pat, fn)
            if m:
                out.append((label, m.group(1), os.path.join(folder, fn)))
    return out


def handlers(lines):
    """[(name, kind, first line index, last line index)]"""
    out, cur = [], None
    for i, raw in enumerate(lines):
        line = strip_comment(raw)
        if cur is None:
            m = R_HANDLER.match(line)
            if m:
                cur = (m.group(2), m.group(1).lower(), i)
        else:
            m = R_END.match(line)
            if m and m.group(1).lower() == cur[0].lower():
                out.append((cur[0], cur[1], cur[2], i))
                cur = None
    return out


R_IF_OPEN = re.compile(r"^(else\s+)?if\b.*\bthen$", re.I)


def skip_to(lines, k, end, opener, closer):
    """From line k (inside a block), the line index of the closer that ends that block."""
    d = 0
    for j in range(k + 1, end):
        s = strip_comment(lines[j]).strip()
        if re.match(closer, s, re.I):
            if d == 0:
                return j
            d -= 1
        elif re.match(opener, s, re.I) and not re.match(r"^else\b", s, re.I):
            d += 1
    return end


def after_call(lines, i, end):
    """What runs after the call on line i before the handler leaves: 'nothing', the first real
    statement, or '(the loop goes on)'. Branches that do not run (else, other cases) are skipped."""
    k = i + 1
    while k < end:
        s = strip_comment(lines[k]).strip()
        if not s or re.match(r"^end\s+(if|switch|try)$", s, re.I):
            k += 1
        elif re.match(r"^exit\s+to\s+top$|^exit\s+(?!repeat\b)[A-Za-z0-9_.]+$|^pass\s", s, re.I):
            return "nothing"
        elif re.match(r"^else\b", s, re.I):
            k = skip_to(lines, k, end, r"^if\b.*\bthen$", r"^end\s+if$") + 1
        elif re.match(r"^(case\b|default$|break$)", s, re.I):
            k = skip_to(lines, k, end, r"^switch\b", r"^end\s+switch$") + 1
        elif re.match(r"^catch\b|^finally$", s, re.I):
            k = skip_to(lines, k, end, r"^try$", r"^end\s+try$") + 1
        elif re.match(r"^exit\s+repeat$", s, re.I):
            k = skip_to(lines, k, end, r"^repeat\b", r"^end\s+repeat$") + 1
        elif re.match(r"^(end\s+repeat|next\s+repeat)$", s, re.I):
            return "(the loop goes on)"
        else:
            return s[:70]
    return "nothing"


def scan(label, key, path, cat):
    with open(path, encoding="utf-8", errors="replace") as f:
        text = f.read()
    lines = text.splitlines()
    code = "\n".join(strip_comment(l) for l in lines)
    hs = handlers(lines)
    names = [h[0] for h in hs]

    prefix = ""
    for n in names:
        m = re.match(r"([A-Za-z0-9_]+)\.StartLevel$", n, re.I)
        if m:
            prefix = m.group(1)
            break
    if not prefix:
        c = collections.Counter(n.split(".")[0] for n in names if "." in n and n.split(".")[0] not in ENGINE)
        prefix = c.most_common(1)[0][0] if c else ""
    has_start = any(n.lower() == f"{prefix}.startlevel".lower() for n in names)

    # levels
    header = "\n".join(l for l in lines[:40] if l.lstrip().startswith(("#", "--")))
    levels, how = "", ""
    m = R_HEADER_LEVELS.search(header)
    if m:
        levels, how = m.group(1), "header"
    if not levels:
        m = R_CONST_LEVELS.search(code)
        if m:
            levels, how = m.group(1), "constant"
    if not levels:
        nums = [int(n) for op, n in R_COMPARE.findall(code) if 1 < int(n) < 100]
        if nums:
            levels, how = str(max(nums)), "compare"
    if not levels and has_start:
        levels, how = "?", "StartLevel, no count"

    # keys
    msgs = [k for k in MSG_KEYS if re.search(rf"^\s*on\s+{k}\b", code, re.I | re.M)]
    polls = bool(re.search(r"\bthe\s+keysDown\b", code, re.I))
    keys = ("keysDown" if polls else "") + (("+" if polls and msgs else "") + ",".join(msgs) if msgs else "")
    if re.search(r"\bInput\.(Down|Axis|Actions)\b", code):
        keys += ("+" if keys else "") + "Input.*"
    tab = bool(re.search(r"\b65289\b", code) or "tabKey" in msgs)
    arrows = bool(re.search(r"\b6536[1-4]\b", code) or "arrowKey" in msgs)

    libs = []
    for s in R_LIB.findall(code):
        for part in s.split(","):
            part = part.strip()
            if part and part != ".livecodescript" and os.path.basename(part) not in libs:
                libs.append(os.path.basename(part))
    uses = len(re.findall(r"\bstart\s+using\b", code, re.I))

    # p1-13: calls of its own StartLevel
    calls = []
    if has_start:
        r_call = re.compile(rf"^\s*(?:.*\bthen\s+)?{re.escape(prefix)}\.StartLevel\b", re.I)
        for name, kind, a, b in hs:
            if name.lower() == f"{prefix}.startlevel".lower():
                continue
            for i in range(a + 1, b):
                if r_call.match(strip_comment(lines[i])):
                    calls.append({"line": i + 1, "in": name, "after": after_call(lines, i, b)})

    disp, kind = cat.get(key, ("", ""))
    if not disp:
        disp = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", key.replace("_", " "))
    return {"source": label, "key": key, "name": disp, "kind": kind or ("comfy" if label == "LIB_COMFY" else "not in catalog"),
            "file": os.path.relpath(path, PROJECTS), "lines": len(lines), "prefix": prefix,
            "startlevel": has_start, "levels": levels, "levels_how": how, "keys": keys or "none found",
            "tab": tab, "arrows": arrows, "libraries": libs, "start_using": uses, "calls": calls}


def yn(b):
    return "yes" if b else ""


def write(rows, out_dir):
    tsv = os.path.join(out_dir, "game_scan.tsv")
    cols = ["source", "key", "name", "kind", "prefix", "startlevel", "levels", "levels_how", "keys", "tab",
            "arrows", "libraries", "start_using", "level_calls", "calls_with_code_after", "lines", "file"]
    with open(tsv, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            after = [c for c in r["calls"] if c["after"] != "nothing"]
            vals = [r["source"], r["key"], r["name"], r["kind"], r["prefix"], yn(r["startlevel"]), r["levels"],
                    r["levels_how"], r["keys"], yn(r["tab"]), yn(r["arrows"]), ",".join(r["libraries"]),
                    str(r["start_using"]), str(len(r["calls"])), str(len(after)), str(r["lines"]), r["file"]]
            f.write("\t".join(vals) + "\n")
    # the level calls, one row each (p1-13 reads this)
    with open(os.path.join(out_dir, "game_scan_level_calls.tsv"), "w", encoding="utf-8", newline="\n") as f:
        f.write("key\tprefix\tline\tin_handler\tthen\n")
        for r in rows:
            for c in r["calls"]:
                f.write(f"{r['key']}\t{r['prefix']}\t{c['line']}\t{c['in']}\t{c['after']}\n")

    by = collections.Counter(r["source"] for r in rows)
    games = [r for r in rows if r["kind"] not in ("tool",)]
    md = ["# Game scan", "",
          "Made by `LIB_TEST/game_scan.py` (bubble p1-01). It reads the card scripts and changes nothing.",
          "Every column is read from the text, so it is a good guess, not a proof.", "",
          f"**{len(rows)} card scripts**: " + ", ".join(f"{n} in {s}" for s, n in by.items()) +
          f". {sum(r['startlevel'] for r in rows)} have their own `<Prefix>.StartLevel`; "
          f"{sum(1 for r in rows if r['levels'] and r['levels'] != '?')} say how many levels; "
          f"{sum(1 for r in rows if 'keysDown' in r['keys'])} poll `the keysDown`; "
          f"{sum(r['tab'] for r in rows)} read Tab; {sum(r['arrows'] for r in rows)} read the arrows; "
          f"{sum(1 for r in rows if r['libraries'])} name a library file.", "",
          "Files: `game_scan.tsv` (one row a game), `game_scan_level_calls.tsv` (one row per StartLevel call, for p1-13).",
          "", "| # | Game | Source | Kind | Prefix | Levels | Keys | Tab | Arrows | Libraries | Level calls (after) |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    for n, r in enumerate(rows, 1):
        lv = f"{r['levels']} ({r['levels_how']})" if r["levels"] else ""
        after = [c for c in r["calls"] if c["after"] != "nothing"]
        lc = f"{len(r['calls'])} ({len(after)})" if r["calls"] else ""
        md.append(f"| {n} | {r['name']} | {r['source']} | {r['kind']} | {r['prefix']} | {lv} | {r['keys']} | "
                  f"{yn(r['tab'])} | {yn(r['arrows'])} | {', '.join(r['libraries'])} | {lc} |")
    md += ["", "## Level calls with code after them (p1-13)", "",
           "A call to the game's own StartLevel that is followed, in the same handler, by more code (or by",
           "the next turn of a loop). If the loading screen and the level start make StartLevel wait, that code may run",
           "against the new level before it is there. 'nothing' calls are left out.", "",
           "| Game | Line | In handler | Then |", "|---|---|---|---|"]
    for r in rows:
        for c in r["calls"]:
            if c["after"] != "nothing":
                then = c["after"].replace("|", "\\|")
                md.append(f"| {r['key']} | {c['line']} | {c['in']} | `{then}` |")
    with open(os.path.join(out_dir, "GAME_SCAN.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(md) + "\n")
    return tsv, len(games)


def main():
    ap = argparse.ArgumentParser(description="One table of every game card script (reads only).")
    ap.add_argument("--no-comfy", action="store_true", help="leave out the generated Comfy Games")
    ap.add_argument("--out", default=HERE, help="folder for game_scan.tsv and GAME_SCAN.md")
    a = ap.parse_args()
    cat = catalog()
    rows = [scan(lbl, key, p, cat) for lbl, key, p in find_games(not a.no_comfy)]
    os.makedirs(a.out, exist_ok=True)
    tsv, n = write(rows, a.out)
    by = collections.Counter(r["source"] for r in rows)
    print(f"{len(rows)} card scripts ({', '.join(f'{s} {c}' for s, c in by.items())}); "
          f"{sum(r['startlevel'] for r in rows)} with StartLevel; "
          f"{sum(len(r['calls']) for r in rows)} level calls -> {a.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
