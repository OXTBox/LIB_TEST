#!/usr/bin/env bash
# start the xt3d games bench (if needed) and play Thrmnlra in it
G=/home/igame3d/projects/xt3D_Raylib_Livecode_Bridge/tools/gamebench
$G run 'xbListGames
xbPlayGame "Thrmnlra"
return line 1 of field "info"' | tail -1
