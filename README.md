# LIB_TEST: what to try this weekend (no AI needed)

Friday, November 13, 2026. Everything here runs on its own. Write what you see in
`OBSERVATIONS.txt` in this folder (or anywhere in `LIB_LLMIN/`): rough notes are fine.

## 1. Thrmnlra in Vibecode3D
Double-click **`PLAY_Thrmnlra_Vibecode3D.bat`** (starts the standalone, loads the game, plays).
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
