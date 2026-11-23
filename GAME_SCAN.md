# Game scan

Made by `LIB_TEST/game_scan.py` (bubble p1-01). It reads the card scripts and changes nothing.
Every column is read from the text, so it is a good guess, not a proof.

**92 card scripts**: 56 in LIB_GAMES, 1 in LIB_GAD, 35 in LIB_COMFY. 66 have their own `<Prefix>.StartLevel`; 64 say how many levels; 86 poll `the keysDown`; 11 read Tab; 85 read the arrows; 16 name a library file.

Files: `game_scan.tsv` (one row a game), `game_scan_level_calls.tsv` (one row per StartLevel call, for p1-13).

| # | Game | Source | Kind | Prefix | Levels | Keys | Tab | Arrows | Libraries | Level calls (after) |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Amazing Couple | LIB_GAMES | game | Couple |  | keysDown+arrowKey |  | yes | lib_bit.livecodescript, lib_map.livecodescript, lib_cellmap.livecodescript |  |
| 2 | Antack | LIB_GAMES | game | Antack | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 5 (0) |
| 3 | Antack Fresh | LIB_GAMES | game | Antack | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 5 (0) |
| 4 | Bank Shot Bounce | LIB_GAMES | not in catalog | BS | 5 (header) | keysDown+arrowKey |  | yes |  |  |
| 5 | Bat Duel | LIB_GAMES | game | Duel | 5 (header) | keysDown |  | yes |  | 4 (2) |
| 6 | Big Ball Of Vectors | LIB_GAMES | game | Ball | 5 (header) | keysDown+arrowKey |  | yes |  | 2 (0) |
| 7 | Block City Hustle | LIB_GAMES | game | Hust | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (0) |
| 8 | Bounce Rally | LIB_GAMES | game | Rally | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 9 | Canyon | LIB_GAMES | game | Canyon | 4 (compare) | none found |  |  |  |  |
| 10 | City Shield | LIB_GAMES | game | City | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 11 | Coast Road | LIB_GAMES | game | Coast | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 12 | Comfy Pong1 | LIB_GAMES | game | Cpong | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 13 | Crater Crawler | LIB_GAMES | game | Crater | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 14 | Cross Traffic | LIB_GAMES | game | Cross | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 15 | Dead Days | LIB_GAMES | game | DD |  | keysDown+rawKeyDown,arrowKey |  | yes | anim_list.livecodescript |  |
| 16 | Deep Dive | LIB_GAMES | game | Dive | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 17 | Dodge Tunnel | LIB_GAMES | game | Dodge | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 18 | Dot Maze | LIB_GAMES | game | Maze | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 19 | Dot Maze Lean | LIB_GAMES | game | Maze | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 20 | Face | LIB_GAMES | tool | Face |  | none found |  |  | lib_map.livecodescript |  |
| 21 | Fare Dash | LIB_GAMES | game | Fare | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 22 | Floppy Flynn | LIB_GAMES | game | Flop | 5 (header) | keysDown |  |  |  |  |
| 23 | Fuel Line | LIB_GAMES | game | Fuel | 5 (compare) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 24 | Grid Sprint | LIB_GAMES | game | Grid | 5 (header) | keysDown+arrowKey |  | yes |  | 5 (4) |
| 25 | Hunter | LIB_GAMES | game | Hunter |  | keysDown+rawKeyUp,arrowKey+Input.* |  | yes |  |  |
| 26 | Interceptor Run | LIB_GAMES | game | Int | 5 (compare) | keysDown+rawKeyDown,arrowKey |  | yes |  | 3 (2) |
| 27 | Jai Alai Block | LIB_GAMES | game | Jai | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 28 | Light Trail Arena | LIB_GAMES | game | Light | 5 (compare) | keysDown+arrowKey |  | yes |  | 4 (1) |
| 29 | Long Worm | LIB_GAMES | game | Worm | 5 (header) | keysDown+arrowKey |  | yes |  | 4 (2) |
| 30 | Matrix Lock | LIB_GAMES | game | Lock | 5 (header) | keysDown+arrowKey |  | yes |  | 2 (0) |
| 31 | Neon Drift Wastes | LIB_GAMES | game | Neon | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 32 | Nine Ball | LIB_GAMES | not in catalog | NB |  | keysDown+arrowKey |  | yes |  |  |
| 33 | Photon Ball | LIB_GAMES | game | PB |  | keysDown+arrowKey |  | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 34 | Probe Vs Cone | LIB_GAMES | game | Probe | 5 (header) | keysDown+arrowKey |  | yes |  | 2 (0) |
| 35 | Prompt And Glaze Maze | LIB_GAMES | game | Maze | 5 (header) | keysDown+arrowKey |  | yes |  | 2 (0) |
| 36 | Ramp Rider | LIB_GAMES | game | Ramp | 5 (compare) | keysDown+arrowKey |  | yes |  | 5 (1) |
| 37 | Rock Field | LIB_GAMES | game | Rock | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 38 | Shaft Descent | LIB_GAMES | game | Shaft | 5 (header) | keysDown+arrowKey |  | yes |  | 2 (1) |
| 39 | Simple Test1 | LIB_GAMES | tool | Cube |  | none found |  |  |  |  |
| 40 | Simple Test2 | LIB_GAMES | tool | Demo |  | rawKeyDown |  |  |  |  |
| 41 | Sky Raiders | LIB_GAMES | game | Raid | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 42 | Soft Landing | LIB_GAMES | game | Land | 5 (header) | keysDown+arrowKey |  | yes |  | 5 (0) |
| 43 | Squad Buggy | LIB_GAMES | game | Squad | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 44 | Stack Down | LIB_GAMES | game | Stack | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 45 | Tabletop Racers | LIB_GAMES | game | Table | 5 (compare) | keysDown+arrowKey |  | yes |  | 5 (1) |
| 46 | Thrmnlra | LIB_GAMES | game | Thrm |  | keyDown,returnKey,enterKey,backspaceKey |  |  | sequencer.livecodescript, lib_map.livecodescript |  |
| 47 | Trench Run | LIB_GAMES | game | Trench |  | keysDown+arrowKey |  | yes |  |  |
| 48 | Vector Blob Apocalypse | LIB_GAMES | game | Blob | 5 (header) | keysDown+arrowKey |  | yes |  | 2 (1) |
| 49 | Vector Pong 3D | LIB_GAMES | game | Pong | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (0) |
| 50 | Vector Toss | LIB_GAMES | game | VT | 4 (compare) | keysDown+arrowKey |  | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 51 | Vine Run | LIB_GAMES | game | Vine | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 52 | Wall Breaker | LIB_GAMES | game | Wall | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 53 | Wreck Ring | LIB_GAMES | game | Wreck | 5 (compare) | keysDown+arrowKey |  | yes |  | 4 (1) |
| 54 | Demo | LIB_GAMES | tool | Demo |  | rawKeyDown |  |  |  |  |
| 55 | uDead | LIB_GAMES | game | uDead | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 2 (1) |
| 56 | u Dead Cull Test | LIB_GAMES | not in catalog | uDead | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 2 (1) |
| 57 | Genetic Anomaly | LIB_GAD | game | GA |  | keysDown+rawKeyDown | yes | yes |  |  |
| 58 | Comfy Bricks1 | LIB_COMFY | comfy | Brick | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 59 | Comfy Bricks369094105 | LIB_COMFY | comfy | Brick | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 60 | Comfy Bricks727270000 | LIB_COMFY | comfy | Brick | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 61 | Comfy Dodge1 | LIB_COMFY | comfy | Dodge | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 62 | Comfy Dodge1027255621 | LIB_COMFY | comfy | Dodge | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 63 | Comfy Dodge1425542174 | LIB_COMFY | comfy | Dodge | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 64 | Comfy Lander1 | LIB_COMFY | comfy | Lander | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 65 | Comfy Lander802252756 | LIB_COMFY | comfy | Lander | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 66 | Comfy Lander999014855 | LIB_COMFY | comfy | Lander | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 67 | Comfy Photon1 | LIB_COMFY | comfy | PB |  | keysDown+arrowKey | yes | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 68 | Comfy Photon11 | LIB_COMFY | comfy | PB |  | keysDown+arrowKey | yes | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 69 | Comfy Photon12 | LIB_COMFY | comfy | PB |  | keysDown+arrowKey | yes | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 70 | Comfy Photon13 | LIB_COMFY | comfy | PB |  | keysDown+arrowKey | yes | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 71 | Comfy Photon542874626 | LIB_COMFY | comfy | PB |  | keysDown+arrowKey | yes | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 72 | Comfy Photon937801948 | LIB_COMFY | comfy | PB |  | keysDown+arrowKey | yes | yes | anim_list.livecodescript, lib_data.livecodescript, stamina.livecodescript |  |
| 73 | Comfy Pong1121386700 | LIB_COMFY | comfy | Cpong | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 74 | Comfy Pong2102167373 | LIB_COMFY | comfy | Cpong | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 75 | Comfy Pong990442537 | LIB_COMFY | comfy | Cpong | 3 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 76 | Comfy Rocks1 | LIB_COMFY | comfy | Rocks | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 77 | Comfy Rocks1986587068 | LIB_COMFY | comfy | Rocks | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 78 | Comfy Rocks836984315 | LIB_COMFY | comfy | Rocks | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 79 | Comfy Squad1 | LIB_COMFY | comfy | Squad | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 80 | Comfy Squad1153357979 | LIB_COMFY | comfy | Squad | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 81 | Comfy Squad443265200 | LIB_COMFY | comfy | Squad | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 82 | Comfy Squad992306219 | LIB_COMFY | comfy | Squad | 5 (header) | keysDown+arrowKey |  | yes |  | 3 (1) |
| 83 | Comfy Toss1 | LIB_COMFY | comfy | VT | 4 (compare) | keysDown+arrowKey | yes | yes | anim_list.livecodescript |  |
| 84 | Comfy Toss1895324116 | LIB_COMFY | comfy | VT | 4 (compare) | keysDown+arrowKey | yes | yes | anim_list.livecodescript |  |
| 85 | Comfy Toss1940951111 | LIB_COMFY | comfy | VT | 4 (compare) | keysDown+arrowKey | yes | yes | anim_list.livecodescript |  |
| 86 | Comfy Toss401421723 | LIB_COMFY | comfy | VT | 4 (compare) | keysDown+arrowKey | yes | yes | anim_list.livecodescript |  |
| 87 | Comfy Waves1 | LIB_COMFY | comfy | Wave | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 88 | Comfy Waves1516237256 | LIB_COMFY | comfy | Wave | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 89 | Comfy Waves2050313440 | LIB_COMFY | comfy | Wave | ? (StartLevel, no count) | keysDown+arrowKey |  | yes |  | 3 (2) |
| 90 | Comfy Worm1 | LIB_COMFY | comfy | Coil | 3 (header) | keysDown+arrowKey |  | yes |  | 4 (2) |
| 91 | Comfy Worm147572964 | LIB_COMFY | comfy | Coil | 3 (header) | keysDown+arrowKey |  | yes |  | 4 (2) |
| 92 | Comfy Worm540039511 | LIB_COMFY | comfy | Coil | 3 (header) | keysDown+arrowKey |  | yes |  | 4 (2) |

## Level calls with code after them (p1-13)

A call to the game's own StartLevel that is followed, in the same handler, by more code (or by
the next turn of a loop). If the loading screen and the level start make StartLevel wait, that code may run
against the new level before it is there. 'nothing' calls are left out.

| Game | Line | In handler | Then |
|---|---|---|---|
| BatDuel | 142 | Duel.Point | `put empty into sHUDWas` |
| BatDuel | 145 | Duel.Point | `put empty into sHUDWas` |
| BounceRally | 206 | Game.OnUpdate | `put tKeys into sKeysWas` |
| BounceRally | 262 | Game.OnUpdate | `Rally.ShowHUD` |
| CityShield | 89 | Game.OnUpdate | `put tSpace into sSpaceWas` |
| CityShield | 190 | Game.OnUpdate | `City.ShowHUD` |
| CoastRoad | 208 | Game.OnUpdate | `put tKeys into sKeysWas` |
| CoastRoad | 300 | Game.OnUpdate | `Coast.ShowHUD` |
| ComfyPong1 | 156 | Game.OnUpdate | `Cpong.ShowHUD` |
| CraterCrawler | 319 | Game.OnUpdate | `put tKeys into sKeysWas` |
| CrossTraffic | 145 | Game.OnUpdate | `Cross.ShowHUD` |
| DeepDive | 143 | Game.OnUpdate | `Dive.ShowHUD` |
| DodgeTunnel | 97 | Game.OnUpdate | `put tKeys into sKeysWas` |
| DodgeTunnel | 168 | Game.OnUpdate | `Dodge.ShowHUD` |
| DotMaze | 210 | Game.OnUpdate | `Maze.ShowHUD` |
| DotMazeLean | 316 | Game.OnUpdate | `Maze.ShowHUD` |
| FareDash | 283 | Game.OnUpdate | `put tKeys into sKeysWas` |
| FuelLine | 175 | Game.OnUpdate | `put tKeys into sKeysWas` |
| GridSprint | 263 | Game.OnUpdate | `put tKeys into sKeysWas` |
| GridSprint | 269 | Game.OnUpdate | `put tKeys into sKeysWas` |
| GridSprint | 271 | Game.OnUpdate | `put tKeys into sKeysWas` |
| GridSprint | 273 | Game.OnUpdate | `put tKeys into sKeysWas` |
| InterceptorRun | 250 | Game.OnUpdate | `put tKeys into sKeysWas` |
| InterceptorRun | 329 | Game.OnUpdate | `Int.ShowHUD` |
| JaiAlaiBlock | 179 | Game.OnUpdate | `Jai.ShowHUD` |
| LightTrailArena | 452 | Game.OnUpdate | `put tKeys into sKeysWas` |
| LongWorm | 148 | Game.OnUpdate | `Worm.ShowHUD` |
| LongWorm | 175 | Game.OnUpdate | `Worm.ShowHUD` |
| NeonDriftWastes | 126 | Game.OnUpdate | `put tKeys into sKeysWas` |
| NeonDriftWastes | 205 | Game.OnUpdate | `Neon.ShowHUD` |
| RampRider | 284 | Game.OnUpdate | `put tKeys into sKeysWas` |
| RockField | 109 | Game.OnUpdate | `put (32 is among the items of tKeys) into sFireWas` |
| RockField | 202 | Game.OnUpdate | `Rock.ShowHUD` |
| ShaftDescent | 244 | Game.OnUpdate | `Shaft.ShowHUD` |
| SkyRaiders | 199 | Game.OnUpdate | `Raid.ShowHUD` |
| SquadBuggy | 388 | Game.OnUpdate | `put tKeys into sKeysWas` |
| StackDown | 155 | Game.OnUpdate | `Stack.ShowHUD` |
| StackDown | 224 | Stack.Land | `Stack.ShowHUD` |
| TabletopRacers | 260 | Game.OnUpdate | `put tKeys into sKeysWas` |
| VectorBlobApocalypse | 173 | Game.OnUpdate | `Blob.ShowHUD` |
| VineRun | 222 | Game.OnUpdate | `Vine.ShowHUD` |
| WallBreaker | 160 | Game.OnUpdate | `Wall.ShowHUD` |
| WreckRing | 189 | Game.OnUpdate | `put tKeys into sKeysWas` |
| uDead | 101 | Game.OnStart | `if gNoMouse is not true then set the lockCursor to true` |
| uDead_CullTest | 114 | Game.OnStart | `if gNoMouse is not true then set the lockCursor to true` |
| ComfyBricks1 | 429 | Game.OnUpdate | `Brick.ShowHUD` |
| ComfyBricks1 | 461 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyBricks369094105 | 429 | Game.OnUpdate | `Brick.ShowHUD` |
| ComfyBricks369094105 | 461 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyBricks727270000 | 429 | Game.OnUpdate | `Brick.ShowHUD` |
| ComfyBricks727270000 | 461 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyDodge1 | 358 | Game.OnUpdate | `Dodge.ShowHUD` |
| ComfyDodge1 | 384 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyDodge1027255621 | 358 | Game.OnUpdate | `Dodge.ShowHUD` |
| ComfyDodge1027255621 | 384 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyDodge1425542174 | 358 | Game.OnUpdate | `Dodge.ShowHUD` |
| ComfyDodge1425542174 | 384 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyLander1 | 416 | Game.OnUpdate | `Lander.ShowHUD` |
| ComfyLander802252756 | 416 | Game.OnUpdate | `Lander.ShowHUD` |
| ComfyLander999014855 | 416 | Game.OnUpdate | `Lander.ShowHUD` |
| ComfyPong1121386700 | 156 | Game.OnUpdate | `Cpong.ShowHUD` |
| ComfyPong2102167373 | 156 | Game.OnUpdate | `Cpong.ShowHUD` |
| ComfyPong990442537 | 156 | Game.OnUpdate | `Cpong.ShowHUD` |
| ComfyRocks1 | 381 | Game.OnUpdate | `Rocks.ShowHUD` |
| ComfyRocks1 | 408 | Game.OnUpdate | `if sScore >= sNextLife and sCfg["extraLife"] > 0 then` |
| ComfyRocks1986587068 | 381 | Game.OnUpdate | `Rocks.ShowHUD` |
| ComfyRocks1986587068 | 408 | Game.OnUpdate | `if sScore >= sNextLife and sCfg["extraLife"] > 0 then` |
| ComfyRocks836984315 | 381 | Game.OnUpdate | `Rocks.ShowHUD` |
| ComfyRocks836984315 | 408 | Game.OnUpdate | `if sScore >= sNextLife and sCfg["extraLife"] > 0 then` |
| ComfySquad1 | 406 | Game.OnUpdate | `put tKeys into sKeysWas` |
| ComfySquad1153357979 | 404 | Game.OnUpdate | `put tKeys into sKeysWas` |
| ComfySquad443265200 | 405 | Game.OnUpdate | `put tKeys into sKeysWas` |
| ComfySquad992306219 | 404 | Game.OnUpdate | `put tKeys into sKeysWas` |
| ComfyWaves1 | 420 | Game.OnUpdate | `Wave.ShowHUD` |
| ComfyWaves1 | 442 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyWaves1516237256 | 420 | Game.OnUpdate | `Wave.ShowHUD` |
| ComfyWaves1516237256 | 442 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyWaves2050313440 | 420 | Game.OnUpdate | `Wave.ShowHUD` |
| ComfyWaves2050313440 | 442 | Game.OnUpdate | `if sMsgT > 0 then subtract 1 from sMsgT` |
| ComfyWorm1 | 460 | Game.OnUpdate | `Coil.ShowHUD` |
| ComfyWorm1 | 468 | Game.OnUpdate | `Coil.ShowHUD` |
| ComfyWorm147572964 | 460 | Game.OnUpdate | `Coil.ShowHUD` |
| ComfyWorm147572964 | 468 | Game.OnUpdate | `Coil.ShowHUD` |
| ComfyWorm540039511 | 460 | Game.OnUpdate | `Coil.ShowHUD` |
| ComfyWorm540039511 | 468 | Game.OnUpdate | `Coil.ShowHUD` |
