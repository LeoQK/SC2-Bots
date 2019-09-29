# StarCraft II Bots

This repository contains two bots built with the [python-sc2](https://github.com/Dentosal/python-sc2) framework for Blizzard's real-time strategy game [StarCraft II](https://en.wikipedia.org/wiki/StarCraft_II:_Wings_of_Liberty). Both bots are rule-based and built for a short course tought to international relations students, [Computational Applications to Policy and Strategy](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md). 

Although the bots eschew the reinforcement learning capabilities integrated into the more advanced [pysc2](https://github.com/deepmind/pysc2) framework, they hold interesting lessons for thinking about how autonomous agents might interact with a complex environment and how humans developing the agents can control and predict their performance. The goal of the short course, which was taught at the Johns Hopkins School of Advanced International Studies in Fall 2018, was for students without a background in computer science, but who might one day grapple with autonomous agents deployed among humans, to think critically about how these agents challenge their understanding of policy and strategy. 

If you're interested in the Computational Applications to Policy and Strategy course, please see the full course website [here](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/CAPS_course_website.md), or feel free to contact me [here](https://leoklenner.com/).

## Intro to StarCraft II

For a description of how the gameplay of StarCraft II works and why the game is challenging from a computational perspective, read the [gameplay overview](https://github.com/LeoQK/SC2-Bots/blob/master/docs/SC2_Overview.md) in the docs folder.

## The Bots

There are two bots in this repository, [CAPSbot](https://github.com/LeoQK/SC2-Bots/blob/master/bots/CapsBot.py) and [TerranBioRush](https://github.com/LeoQK/SC2-Bots/blob/master/bots/TerranBioRush.py). Both bots play Terran and implement simple rush strategies. The boths are rule-based and hence aren't capable of learning. See this [example of a Terran reinforcement learning bot](https://github.com/skjb/pysc2-tutorial/blob/master/Reinforcement%20Learning%20Terran%20Bot/learning_agent.py). 

### CAPSbot

[CAPSbot](https://github.com/LeoQK/SC2-Bots/blob/master/bots/CapsBot.py) builds MARINE and CYCLONE units and once > 20 MARINES and 4 CYCLONES are available, the bot attacks the enemy base. The attack takes place around the 5:30 minute mark. CAPSbot generally defeats the in-game AI in all lineups on "hard" difficulty.  

See this [forum post](https://us.battle.net/forums/en/sc2/topic/20762966106) for a discussion of the MARINE + CYCLONE rush strategy and how to counter it. 

### TerranBioRush

[TerranBioRush](https://github.com/LeoQK/SC2-Bots/blob/master/bots/TerranBioRush.py) builds only MARINE units from 4 BARRACKS buildings and once > 12 MARINES are available, the bot attacks the enemy base. The attack takes place around the 3:00 minute mark. TerranBioRush mostly defeats the in-game AI in all lineups on "elite" difficulty. 

### Failure Modes

The performance of rule-based bots is not fully predictable when deployed in a complex environment like StarCraft. 

The failure modes of the bots arise from suboptimal navigation of certain terrain features, e.g. the army might split up around a mountain pass and thereby reduce its combined damage output and lose the game. Other failure modes arise from resupplying the army on a unit by unit basis, which often prooves ineffective compared to a larger batch of units sent together, or locking units between buildings through randomized building placements. For a brief discussion of these failure modes, see this [slide deck](https://github.com/SAIS-S2S-Technology/Roadmap/blob/master/CAPS/Slides/CAPS%2003%20Building%20a%20Rule-Based%20StarCraft%20II%20Bot.pdf) from the original course. 

