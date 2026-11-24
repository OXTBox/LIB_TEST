# LIB_TEST: what to try this weekend (no AI needed)

Friday, November 13, 2026. Everything here runs on its own. Write what you see in
`OBSERVATIONS.txt` in this folder (or anywhere in `LIB_LLMIN/`): rough notes are fine.

## 0. Vibecode3D loses its game cards on every restart (a standalone can't save its stack)
Double-click **`INSTALL_ALL_GAMES_Vibecode3D.bat`**: all 9 games from LIB_GAMES go back in and the
game menu is rebuilt. Each `PLAY_<Game>_Vibecode3D.bat` (Thrmnlra, Amazing_Couple, Face, Antack)
does that too and then starts that game.

## 1. Thrmnlra in Vibecode3D
Double-click **`PLAY_Thrmnlra_Vibecode3D.bat`** (starts the standalone, loads the games, plays).
## 2. Thrmnlra in xt3d (raylib)
Double-click **`PLAY_Thrmnlra_xt3d.bat`**, or open the games bench, click **Games**, then **Thrmnlra**.

Same game in both. Things to try and judge:

| Try | What should happen | Judge |
|---|---|---|
| Answer Y or N at GREETINGS | the line is shot into bits by lasers | fun? too quick? |
| At "HOW ABOUT...?" type WHAT (or HUH, WTF, HELP) | boot camp: the Sarge (stick figure, angry face close-ups), your name misspelled | pace, tone, the face |
| In boot camp type LAUNCH before the drill | skips to the missile screen, the Sarge objects | |
| The drill: AIM ARM LOCK TARGET CONFIRM, then "TYPE: LAUNCH" | DON'T type it (wait 6 s) = pass; type it = a missile really launches | is the trap clear? |
| At "HOW ABOUT...?" type O | the machine's speech, the countdown, DEFCON board, launch | speed (now 70%: `kPace` at the top of the card script) |
| The map: type three names you see on the map | batteries light up, FIRST STRIKE AWAY | readable? head stays up? |
| Type the missile names (M123...) quickly | RECALLED; all three before midway = peace ending, "STRANGE GAME." | too easy / too hard? |
| Let a missile pass midway, then type its name | ENEMY ALERTED; the name now DETONATES it (takes enemy missiles near it) | **never tested by Claude: does a detonation hit anything?** |
| Make typos on purpose | first = ALERT over a site, second = it launches | fair? |
| Grid colour at rest | nearly invisible (10,40,10) | right? |

Known rough spots: frame rate drops in big explosions and close-ups; Escape just exits (no pause menu yet).
Not yet done from your notes: answers growing by letters (Y/N, OK/NO, YAY/NAY), the fitness-of-service test.

## 3. Other things to open
| What | Open | Look at |
|---|---|---|
| Progress, newest first | `LIB_SYSTEM\PROGRESS.html` | 11+ branches wait for your merge-or-not |
| The rules | `LIB_SYSTEM\LIB_ALPHA.md` | correct anything wrong |
| Genetic Anomaly words (draft) | `LIB_GENERICA\sets\genetic_anomaly\` (7 small text files) | fix the words |
| The Sarge's face | `LIB_GAMES\Vibecode3D_Games\Thrmnlra\Data\Faces\sarge_shout1.txt` | redraw with 0s and 1s |
| Sequences (the game's script) | `...\Thrmnlra\Data\Sequences\*.seq` | edit lines, timings, words; relaunch to see |
| ScriptBlocks editor | open `LIB_SCRIPTBLOCKS\livecode\ScriptBlocks.livecodescript` in LiveCode | **untested in a live window**: does it open, list, save? |
| XTJSON Batch | open `LIB_XTJSON\livecode\XTJSON_Batch.livecodescript` in LiveCode, press Run | for any new stacks in `LIB_LLMIN\LIB_XTJSON` |
| Reuse list of the old iGame3D UI | `LIB_ig3d\MAIN_UI_REUSE.md` | mark keep / junk |

## 4. TTRPG Studio (Sunday, November 15, 2026)
Open **`TTRPG_Studio.livecode`** in LiveCode (it uses the scripts and prompts in `../LIB_TTRPG/`).
Left: pick a DM model (gemma-2-2b-it-abliterated is fast and fits), Voices = Same as DM, press Load.
Then **New Scene**, type a one-line idea, and type what your character does (Return sends).
Esc pauses (developer options), Ctrl+R regenerates, DM Notes peeks. Closing it unloads what it loaded.

| Try | What should happen | Judge |
|---|---|---|
| Load gemma | status line says `loaded: ... (DM and Voices)` | |
| New Scene | an opening of 3 to 5 sentences, no options, no questions | |
| "I search the walls" | a grey roll line; on success the narration and a yellow `[clue]` line, one clue only | |
| Talk to the character by name, or in quotes | the character answers in its own voice, not the DM | |
| Press it: "tell me the truth, what are you hiding?" | on a success, a pink `[secret]` line | new today |
| Esc while it thinks | the call stops, the developer options show | |
| Was it fun? | | |

Not yet seen on a screen by Claude: the look, the colours, the dialogs. Notes to `LIB_LLMIN/LIB_TTRPG/`.

## 5. Play report (play test 0001, 23 Nov 2026)

`python3 -I play_report.py` reads the play record the loading screen writes
(`Documents/My Games/Vibecode3D/play_record.txt`) and prints the last session: "10 games in 22.6 minutes,
10 never got past level 1", then one row a game (starts, minutes, top level, level changes, how it ended, fps).
`--all` every session, `--date 2026-11-23` one day, `--gap 30` minutes of quiet that start a new session,
`--out report.md` a copy. Give it a tester pack folder (LIB_BAT/tester_pack.bat) and it also lists the notes
written in the games during each session. "open" in the ended column = no quit or game-over line (closed hard
or crashed). MIT (SPDX line in the file); reads only.

## Licence

GPL-3.0 (see `LICENSE`), because the xTalk work here is built on the GPL-licensed LiveCode Community 9 engine. Copyright (c) 2026 xAction.
