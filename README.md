# StarCraft II Bots

This repository contains two bots built with the [python-sc2](https://github.com/Dentosal/python-sc2) framework for Blizzard's real-time strategy game [StarCraft II](https://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty). Both bots are rule-based and built for a short course tought to international relations students, [Computational Applications to Policy and Strategy](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md). 

Although the bots eschew the reinforcement learning capabilities integrated into the more advanced [pysc2](https://github.com/deepmind/pysc2) framework, they hold interesting lessons for thinking about how autonomous agents might interact with a complex environment and how humans developing the agents can control and predict their performance. The goal of the short course, which was taught at the Johns Hopkins School of Advanced International Studies in Fall 2018, was for students without a background in computer science, but who might one day grapple with autonomous agents deployed among humans, to think critically about how these agents challenge their understanding of policy and strategy. 

If you're interested in the Computational Applications to Policy and Strategy course, please see the full course website [here](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md), or feel free to contact me [here](https://leoklenner.com/).

## Introduction to StarCraft II

StarCraft II is a real-time strategy game released by Blizzard in 2010. The game's precessor is StarCraft Broodwars. In this introduction, we'll briefly go over core gameplay elements of StarCraft II and then touch on some of the reasons why the game is interesting from a computational perspective. 

If you're familiar with the game and don't need a refresher, skip this introduction. 

### Gameplay

#### Overview

In StarCraft II, players can choose between three factions, Zerg, Protoss and Terran. To defeat their opponent, a player has to master two main techniques, macro and micro management, and their associated tasks.

| Technique        | Main task                      | Sub-tasks  | Differentiation |
| :----------------: |:-------------------------:| :---------:| :---------:|
| Macro            | Build and manage an economy | Mine ressources, create new buildings, produce army units and updates | Good macro leads to a large army, multiple base expansions, and continous flow of production |
| Mirco            | Control an army | Coordinate individual units' movements and actions in combat | Good mirco leads to quick and adaptive maneuvers and a high survivability of units |

Depending on a player's skill, the player might decide to pursue a micro or macro-intensive gameplay. This choice is often influenced by the player's opponent and the map on which the game takes place. The game ends if one of the players has lost all their buildings, or a player resigns. A game can last anywhere from 5 to 30 minutes.

To gain a glimpse of what StarCraft II gameplay is like, take a look at one the professional esports matches on [YouTube](https://www.youtube.com/watch?v=QFFrMJykL2w). 

#### Elements

The gameplay of StarCraft revolves around a number of core elements: factions, maps, units and buildings. Each faction has its own units and buildings and there's a large number of maps on which the games take place. 

To give a brief description of the factions, Zerg are swarm-based insects, Protoss a high-tech civilization, and Terran humans. Average unit costs are lowest for Zerg and highest for Protoss, with Terran in the middle. The ressource costs determine the composition of the army; while Zerg might swarm out with multiple units, a Protoss army of equal strength tends to encompass fewer units. 

Given that the composition of an army consumes space, how that space is structured can give an advantage to a speficic faction and its default army composition. For that reason, maps can influence the balance of a game. 

#### Strategies

The possibilities that players have in creating strategies based on how they combine timing, production, selection of units and attack patterns is vast. This is a large driver of the game's computational complexity. Below is a list of aspects that might influence how a player chooses a strategy. 

| Aspect | Description |
|:------:|:-----------:|
| Map | Different features of terrain lead to different advantages. Terran can use a high-ground to wall of their base, Zerg armies might avoid choke points because it exacerbates swarming. | 
| Revealed information |
| Opponent faction |
| Opponent strategy |
| Resource costs |
| Build order |
| Game stage |

### Complexity
