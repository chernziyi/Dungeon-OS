from dataclasses import dataclass
from typing import List
from typing import Tuple

@dataclass
class LevelData:
    difficulty: int
    enemyRoster: List[str]
    def load_from(self, other: "LevelData"):
        self.__dict__.update(other.__dict__)

combatZone0 = [LevelData(1, ["Obelisk", "Cultist"])] #debugging only

combatZone1 = [LevelData(1, ["Bee"]),\
               LevelData(1, ["Mindless Roots"])]