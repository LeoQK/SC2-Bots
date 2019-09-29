# StarCraft II Bots

This repository contains two bots built with the [python-sc2](https://github.com/Dentosal/python-sc2) framework for Blizzard's real-time strategy game [StarCraft II](https://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty). Both bots are rule-based and built for a short course tought to international relations students, [Computational Applications to Policy and Strategy](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md). 

Although the bots eschew the reinforcement learning capabilities integrated into the more advanced [pysc2](https://github.com/deepmind/pysc2) framework, they hold interesting lessons for thinking about how autonomous agents might interact with a complex environment and how humans developing the agents can control and predict their performance. The goal of the short course, which was taught at the Johns Hopkins School of Advanced International Studies in Fall 2018, was for students without a background in computer science, but who might one day grapple with autonomous agents deployed among humans, to think critically about how these agents challenge their understanding of policy and strategy. 

If you're interested in the Computational Applications to Policy and Strategy course, please see the full course website [here](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md), or feel free to contact me [here](https://leoklenner.com/).

## Introduction to StarCraft II

StarCraft II is a real-time strategy game released by Blizzard in 2010. The game's precessor is StarCraft Broodwars. In this introduction, we'll briefly go over core gameplay elements of StarCraft II and then touch on some of the reasons why the game is interesting from a computational perspective. 

If you're familiar with the game and don't need a refresher, skip this introduction. 

### Gameplay

#### Overview

In StarCraft II, players can choose between three factions, [Zerg](https://starcraft.fandom.com/wiki/Zerg), [Protoss](https://starcraft.fandom.com/wiki/Protoss) and [Terran](https://starcraft.fandom.com/wiki/Terran). To be good at StarCraft, players need to master two main techniques, macro and micro management, and their associated tasks.

| Technique        | Main task                      | Sub-tasks  | Differentiation |
| :----------------: |:-------------------------:| :---------:| :---------:|
| Macro            | Build and manage an economy | Mine ressources, create new buildings, produce army units and updates | Good macro leads to a large army, multiple base expansions, and continous flow of production |
| Mirco            | Control an army | Coordinate individual units' movements and actions in combat | Good mirco leads to quick and adaptive maneuvers and a high survivability of units |

Depending on a player's skill, the player might decide to pursue a micro or macro-intensive gameplay. This choice is often influenced by the player's opponent and the map on which the game takes place. The game ends if one of the players has lost all their buildings, or a player resigns. A game can last anywhere from 5 to 30 minutes.

To gain a glimpse of what StarCraft II gameplay is like, take a look at one the professional esports matches on [YouTube](https://www.youtube.com/watch?v=QFFrMJykL2w). 

#### Elements

The gameplay of StarCraft revolves around a number of core elements: factions, maps, units and buildings. Each faction has its own units and buildings and there's a large number of maps on which the games take place. 

Units can be divided into workers and army. Workers mine the resources required to produce buildings, etc. Army units deal damage. Average unit costs are lowest for Zerg and highest for Protoss, with Terran in the middle. The unit resource costs determine the composition of the army. Zerg might swarm out with multiple units. A Protoss army of equal strength tends to encompass fewer units.

Given that the composition of an army consumes space, how that space is structured can give an advantage to a speficic faction and its default army composition. For that reason, maps can influence the balance of a game. 

#### Strategies

The possibilities that players have in creating strategies based on how they combine timing, production, selection of units and attack patterns is vast. This is a large driver of the game's computational complexity. Below is a list of aspects that might influence how a player chooses a strategy. 

| Aspect | Description |
|:------:|:-----------:|
| Map | Different features of terrain lead to different advantages. Terran can use a high-ground to wall of their base, Zerg armies might avoid choke points because it exacerbates swarming. | 
| Revealed information | Maps are covered in fog of war, meaning players need to send units to scout the maps to obtain information about their opponent's economy and army. Often strategies are developed as direct counter-strategies, hence how much a player knows a bout their opponent matters a lot. |
| Opponent faction | Given the factions of the two players, each player will pursue different strategies depending on the faction of their opponent. Terran playing against Protoss looks different from Terran playing against Terran. 
| Opponent strategy | Strategies are often developed specifically to counter the opponent's strategy, based on revealed information or initial assumptions about what the opponent's strategy might be. There are constant strategic adjustments based on new information becoming available throughout the game. |
| Build order | Not each unit or building available for a faction can be built immediately, resource costs aside. Instead, there is a hierachy of buildings and units that determines when something can be built. Producing  advanced units might require multiple different buildings as prerequisites, some of which again have their own prerequisites, etc. Players have to balance where they are in this hierachy with where they need to be for a given strategy. | 
| Game stage | Games are divided into three stages, early, mid, and late game. A strategy that might work well in the early game often doesn't work well in the mid or late game. Often, the game stage also determines how many resources a player has accumulated.|

All of these aspects result in the process of strategy selection and adaptation in StarCraft being highly complex. However, there are clear patterns discernible across games, such as proxy or greedy strategies. 

<img src="https://github.com/LeoQK/SC2-Bots/blob/master/static/techtree.jp" width=100 align=center>


### Complexity

StarCraft II is a complex game, especially from a computational perspective where the large action space and imperfect information take their toll on how well algortihms can learn to play the game. 

Consider the following properties of the game's environment:

| Property | Description |
|:------:|:-----------:|
|Action space| 10^8, need for hierarchical actions|
|State space | 10^1685|
|State transitions | Continious|
|Rewards| Unknown for each prior state as the only rewards are binary for win/loss|
|Reward horizon| Far horizon as the only rewards come at the end of the game|
|Mode of information| Imperfect information through fog of war|
|Mode of actions| Simultaneous|

TBC

