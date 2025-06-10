from dataclasses import dataclass
from typing import List
from typing import Tuple

@dataclass
class EnemyData:
    id: str
    actualId: str
    hp: int
    maxhp: int
    strength: int
    defense: int
    speed: int
    counter: float
    specialStats: Tuple[str]
    traits: Tuple[str]
    skills: Tuple[str]
    status: Tuple
    intent: List
    intentTarget: List
    intentChart: Tuple[str]
    lootTable: Tuple[str, int]
    attackText: str
    alive: bool
    summon: bool
    def load_from(self, other: "EnemyData"):
        self.__dict__.update(other.__dict__)

#all intentChart refs:
#default attack: "default", [all skills]
#use when lower than x% health: "hpBelow", percentage, [all skills]

#Bees: suicide bombers with necromany
BeeName =\
["Honeybee", "Hardworking Bee"]
BeeStats =\
[EnemyData("Honeybee", "Honeybee", 15, 15, 5, 0, 5, 0, [], [], [["Attack", 0], ["Kamikaze", 0]], [], [], [],\
["default", [0], "hpBelow", 0.5, [1]],\
[["Honeypot", 2], ["Nope", 1], ["Coins", 10]],\
"user goes in for a sting!", True, False),
EnemyData("Hardworking Bee", "Hardworking Bee", 20, 20, 8, 1, 8, 0, [], [], [["Kamikaze", 0], ["Overtime", 0]], [["UNDYING", 2, "", ""]], [], [],\
["default", [0], "notSummon", [1], "hpBelow", 0.5, [0]],\
[["Honeypot", 2], ["Nope", 1], ["Coins", 25]],\
"user goes in for a sting!", True, False)]

#Plants: drain stats, debuff masters.
PlantName =\
["Mindless Roots"]
PlantStats =\
[EnemyData("Mindless Roots", "Mindless Roots", 10, 10, 3, 5, 4, 0, [], [["Enroaching Roots", 0]], [["Attack", 0]], [], [], [],\
["default", [0]],\
[["Herbal Leaf", 2], ["Nope", 1], ["Coins", 10]],\
"Roots lash out by instinct!", True, False)]

#Goldbots: Succ coin, shoot coin.
GoldbotName =\
[]
GoldbotStats =\
[]

#Cultists: OBELISK-CHAN NOTICE ME!
CultName =\
["Obelisk", "Cultist"]
CultStats =\
[EnemyData("Obelisk", "Obelisk", 0, 0, 0, 0, 10, 0, [], [["One With Nature", 0], ["Faith-fueled", 30], ["Conduit Of Faith", 0]], [["The Calling", 0]], [], [], [],\
["none"],\
[["Nope", 1], ["Coins", 30]],\
"The Obelisk whispers...", True, False),
EnemyData("Cultist", "Cultist", 30, 30, 3, 4, 6, 0, [], [], [["Prayer", 0]], [], [], [],\
["default", [0]],\
[["Nope", 1], ["Coins", 20]],\
"user attempts to convert you with violence!", True, False)]

#Ooze: Trojan Horses, become your party, damage share, blah blah.
OozeName =\
[]
OozeStats =\
[]

PirateSummonName =\
["Cannon"]
PirateSummonStats =\
[EnemyData("Cannon", "Cannon", 15, 15, 4, 2, 3, 0, [], [], [["Attack", 0]], [], [], [],\
["default", [0]],\
[["Nope", 1]],\
"'Fire in the hole!'", True, False)]

RavenSummonName =\
["Birb"]
RavenSummonStats =\
[EnemyData("Birb", "Birb", 5, 5, 2, 0, 6, 0, [], [["Swarm", 0]], [["Attack", 0]], [], [], [],\
["default", [0]],\
[["Nope", 1]],\
"user does what users do best-- be annoying!", True, False)]

ShamanSummonName =\
["Slippery Sand"]
ShamanSummonStats =\
[EnemyData("Slippery Sand", "Slippery Sand", 0, 0, 0, 0, 1, 0, [], [["One With Nature", 0], ["Slippery", 0]], [], [], [], [],\
["none"],\
[["Nope", 1]],\
"user can't do jack. It's SAND", True, False)]

enemyName = BeeName + PlantName + GoldbotName + CultName + OozeName + PirateSummonName + RavenSummonName + ShamanSummonName
enemyStats = BeeStats + PlantStats + GoldbotStats + CultStats + OozeStats + PirateSummonStats + RavenSummonStats + ShamanSummonStats