import random
import sc2
from sc2 import run_game, maps, Race, Difficulty
from sc2.player import Bot, Computer
from sc2.constants import SCV, COMMANDCENTER, SUPPLYDEPOT, BARRACKS, MARINE

class CAPSbot(sc2.BotAI):
    async def on_step(self, iteration):
        await self.distribute_workers()
        await self.build_workers()
        await self.build_supplydepot()
        await self.build_barracks()
        await self.train_marines()
        await self.attack()

    async def build_workers(self):
        for cc in self.units(COMMANDCENTER).ready.noqueue:
            if self.can_afford(SCV) and self.units(SCV).amount < 80:
                await self.do(cc.train(SCV))

    async def build_supplydepot(self):
        if self.supply_left < 8 and not self.already_pending(SUPPLYDEPOT) and self.can_afford(SUPPLYDEPOT):
            await self.build(SUPPLYDEPOT, near=self.units(COMMANDCENTER).first)

    async def build_barracks(self):
        if self.can_afford(BARRACKS) and self.units(BARRACKS).amount < 4:
            await self.build(BARRACKS, near=self.units(COMMANDCENTER).first)

    async def train_marines(self):
        for rax in self.units(BARRACKS):
            if rax.is_ready and rax.noqueue:
                if self.can_afford(MARINE) and self.units(MARINE).amount < 50:
                    await self.do(rax.train(MARINE))

    async def attack(self):
        if self.units(MARINE).amount > 12:
            if len(self.known_enemy_units) > 0:
                for m in self.units(MARINE).idle:
                    await self.do(m.attack(random.choice(self.known_enemy_units)))

        if self.units(MARINE).amount > 10:
            for m in self.units(MARINE).idle:
                await self.do(m.attack(self.enemy_start_locations[0]))

run_game(maps.get("AbyssalReefLE"),[
    Bot(Race.Terran, CAPSbot()),
    Computer(Race.Terran, Difficulty.VeryHard)
    ], realtime=False)

