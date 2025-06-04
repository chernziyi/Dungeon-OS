from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class UpgradeData:
    difficulty: int
    table: Tuple 
    def load_from(self, other: "UpgradeData"):
        self.__dict__.update(other.__dict__)

pirateUpgrades =\
[UpgradeData(1, [["STR", 1, 5], ["ACCURACY", 0.05, 3], ["Cannon Call", 0, 1], ["Drinks Up!", 0, 1]])]

dissectorUpgrades =\
[UpgradeData(1, [["STR", 1, 3], ["HEALBONUS", 2, 5], ["Bloody Jabs", 0, 1], ["Bandages", 0, 1]]),
UpgradeData(2, [["STR", 1, 3], ["HEALBONUS", 2, 5], ["Bloody Jabs", 0, 1], ["Bandages", 0, 1]])]

qiMasterUpgrades =\
[UpgradeData(1, [["STR", 1, 3], ["DEF", 1, 3], ["HP", 20, 2], ["On Guard", 0, 1]])]

ravenUpgrades =\
[UpgradeData(1, [["SPD", 1, 5], ["SPD", 2, 1], ["Rusty Graze", 0, 2], ["Velocity", 0, 2]])]

astrologistUpgrades =\
[UpgradeData(1, [["JUICE", 5, 5], ["Radiant Glow", 0, 1], ["Rising Moon", 0, 1], ["STARS", 1, 3]])]

bardUpgrades =\
[UpgradeData(1, [["STR", 1, 5], ["DODGE", 0.05, 3], ["Leer", 0, 1], ["Fancy Feet", 0, 1]])]

upgradeTable = [pirateUpgrades, dissectorUpgrades, qiMasterUpgrades, ravenUpgrades, astrologistUpgrades, bardUpgrades]