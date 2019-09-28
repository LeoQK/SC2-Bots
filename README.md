# StarCraft II Bots

This repository contains two bots built with the [python-sc2](https://github.com/Dentosal/python-sc2) framework for Blizzard's real-time strategy game [StarCraft II](https://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty). Both bots are rule-based and built for a short course tought to international relations students, [Computational Applications to Policy and Strategy](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md). 

Although the bots eschew the learning capabilities integrated into the more advanced [pysc2](https://github.com/deepmind/pysc2) framework, they hold interesting lessons for thinking about how autonomous agents might interact with a complex environment and how humans developing the agents can control and predict their performance. The goal of the short course, which was taught at the Johns Hopkins School of Advanced International Studies in Fall 2018, was for students without a background in computer science, but who might one day grapple with autonomous agents deployed among humans, to think critically about how these agents challenge their understanding of policy and strategy. 

If you're interested in the Computational Applications to Policy and Strategy course, please see the full course website [here](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md), or feel free to contact me [here](https://leoklenner.com/).

## Introduction to StarCraft II

StarCraft II is a real-time strategy game released by Blizzard in 2010. The game's precessor is StarCraft Broodwars. In this introduction, we'll briefly go over core gameplay elements of StarCraft II and then touch on some of the reasons why the game is interesting from a computational perspective. 

### Gameplay

In StarCraft II, players can choose between three factions, Zerg, Protoss and Terran. To defeat their opponent, a player has two main tasks. First, build and manage an economy. This includes buiding workers to mine ressources, create new buildings, and use the buildings to produce army units and updates. We refer to the economic gameplay as *macro* gameplay. Second, control an army. This includes commanding army units mainly on a tactical level. The strategic level covers the creation of units to overmatch the opponent's army and is considered part of the macro gameplay. The tactical level covers the control of individual units in combat. We refer to the control of units as *micro* gameplay. Depending on a player's skill, the player might decide to pursue a micro or macro-intensive gameplay. The former is generally differentiated through a large army, the latter through quick maneuvers and high unit survival.  

The game ends if one of the players has lost all their buildings, or a player resigns. A game can last anywhere from 5 to 30 minutes. To gain a glimpse of what StarCraft II gameplay is like, take a look at one the professional esports matches on [YouTube](https://www.youtube.com/watch?v=QFFrMJykL2w). 


### Complexity
