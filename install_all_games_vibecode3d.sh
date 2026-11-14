#!/usr/bin/env bash
# Vibecode3D standalone: install every game card script from LIB_GAMES (the standalone can't save
# its stack, so run this after each start), rebuild the game menu, optionally play one.
#   bash install_all_games_vibecode3d.sh [GameToPlay]
V=/home/igame3d/projects/Vibecode3D/tools_vibe.sh
D=/home/igame3d/projects/LIB_GAMES/Vibecode3D_Games
$V run 'try
  Game.Exit
end try' >/dev/null 2>&1
for f in "$D"/Vibecode3D_Play_*.livecodescript; do
  n=$(basename "$f" .livecodescript); n=${n#Vibecode3D_Play_}
  W=$(wslpath -w "$f")
  r=$($V run "if there is not a card \"Play.$n\" then Game.Rebuild \"$n\", false
set the script of card \"Play.$n\" to URL (\"file:\" & \"$W\")
put the result into tR
try
  save.card.script.to.set \"Play.$n\"
end try
if tR is empty then return \"ok\"
return \"COMPILE ERROR \" & tR" 2>&1 | tail -1)
  echo "$n: $r"
done
$V run 'try
  Menu.Threedots.Build
end try
return "menu rebuilt"' | tail -1
# game notes: ` or F2 in any game opens a note box; notes go to LIB_LLMIN/LIB_GAMES/GAME_NOTES.txt
NW=$(wslpath -w /home/igame3d/projects/LIB_GAMES/tools/GameNotes.livecodescript)
$V run "if there is a stack \"GameNotes\" then
  remove script of stack \"GameNotes\" from front
  delete stack \"GameNotes\"
end if
start using stack \"$NW\"
insert script of stack \"GameNotes\" into front
return \"game notes on: \` or F2\"" | tail -1
if [ -n "$1" ]; then
  $V run "repeat for each item tS in \"Sequencer,Seq_Clip_Wait,Seq_Clip_Cue,Seq_Clip_Console,Seq_Clip_Type,Seq_Clip_Ask,Seq_Clip_Title,Seq_Clip_Fade,Seq_Clip_Input,Seq_Clip_Hotword,Thrmnlra_Clip_Countdown,Thrmnlra_Clip_RecallKey,Thrmnlra_Clip_Targets,Thrmnlra_Clip_Drill,Thrmnlra_Clip_Outbound\"
  if there is a stack tS then delete stack tS
end repeat
Game.Select \"$1\"
Game.Play
return the short name of this card" | tail -1
fi
