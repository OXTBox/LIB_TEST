#!/usr/bin/env bash
# start the Vibecode3D standalone (if needed), make the Play.Thrmnlra card, load its script, play
V=/home/igame3d/projects/Vibecode3D/tools_vibe.sh
W=$(wslpath -w /home/igame3d/projects/LIB_GAMES/Vibecode3D_Games/Vibecode3D_Play_Thrmnlra.livecodescript)
$V run "try
  Game.Exit
end try
repeat for each item tS in \"Sequencer,Seq_Clip_Wait,Seq_Clip_Cue,Seq_Clip_Console,Seq_Clip_Type,Seq_Clip_Ask,Seq_Clip_Title,Seq_Clip_Fade,Seq_Clip_Input,Seq_Clip_Hotword,Thrmnlra_Clip_Countdown,Thrmnlra_Clip_RecallKey,Thrmnlra_Clip_Targets,Thrmnlra_Clip_Drill,Thrmnlra_Clip_Outbound\"
  if there is a stack tS then delete stack tS
end repeat
if there is not a card \"Play.Thrmnlra\" then Game.Rebuild \"Thrmnlra\", false
set the script of card \"Play.Thrmnlra\" to URL (\"file:\" & \"$W\")
Game.Select \"Thrmnlra\"
Game.Play
return the short name of this card" | tail -1
