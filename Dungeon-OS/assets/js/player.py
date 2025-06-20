from dataclasses import dataclass, field
from typing import Tuple
from typing import List

from skills import SkillData, pirateSkillList, dissectorSkillList, ravenSkillList, qiMasterSkillList, shamanSkillList, bardSkillList

@dataclass
class PlayerData:
    id: str = ""
    classId: str = ""
    hp: int = 0
    maxhp: int = 0
    juice: int = 0
    maxjuice: int = 0
    strength: int = 0
    defense: int = 0
    speed: int = 0
    counter: float = 0.0
    specialStats: Tuple[str, ...] = field(default_factory=tuple)
    traits: Tuple[str, ...] = field(default_factory=tuple)
    skills: Tuple[str, ...] = field(default_factory=tuple)
    status: Tuple = field(default_factory=tuple)
    equipment: Tuple[str, ...] = field(default_factory=tuple)
    equipmentSlots: int = 0
    attackText: str = ""
    alive: bool = True

    def load_from(self, other: "PlayerData"):
        self.__dict__.update(other.__dict__)

@dataclass
class ClassData:
    id: str = ""
    desc: str = ""
    stats: PlayerData = field(default_factory=PlayerData)
    skillList: List["SkillData"] = field(default_factory=list)

    def load_from(self, other: "ClassData"):
        self.__dict__.update(other.__dict__)
                    
classes = ["Pirate", "Dissector", "Qi Master", "Raven", "Shaman", "Bard"]

classList = [ClassData("Pirate", "Firing shots and summoning cannons, Pirates deliver killing blows to finish off enemies. Arrr!",\
            PlayerData("Pirate", "Pirate", 100, 100, 10, 10, 7, 2, 5, 0, [["MAX AMMO", 1]], [], [["Pistol Shot", 0]], [], [], 2,\
            "user gives out a taste of their cutlass!", True),\
            pirateSkillList),\
            
            ClassData("Dissector", "Covered in blood, Dissector walks among the bodies looking for a new test subject.",\
            PlayerData("Dissector", "Dissector", 100, 100, 15, 15, 5, 3, 6, 0, [], [], [["Bloody Jabs", 0]], [], [], 2,\
            "user does some on-site practice!", True),\
            dissectorSkillList),\

            ClassData("Qi Master", "Never fight a Qi Master head-on, for they are hard to hit and will hit back harder.",\
            PlayerData("Qi Master", "Qi Master", 100, 100, 10, 10, 5, 5, 5, 0, [], [], [["On Guard", 0]], [], [], 2,\
            "user decides to talk with their fist!", True),\
            qiMasterSkillList),\
                
            ClassData("Raven", "Once upon a midnight dreary, while I waited weak and weary, Ravens come to feed and spread a plague I haven't seen before.",\
            PlayerData("Raven", "Raven", 90, 90, 15, 15, 4, 2, 7, 0, [], [], [["Velocity", 0]], [], [], 2,\
            "user rushes in, dagger in hand!", True),\
            ravenSkillList),\
            
            ClassData("Shaman", "Like nature, Shamans are able to hit you from everywhere",\
            PlayerData("Shaman", "Shaman", 80, 80, 25, 25, 4, 2, 5, 0, [], [], [["Slippery Sand", 0]], [], [], 2,\
            "user whacks target with their staff!" ,True),\
            shamanSkillList),\
            
            ClassData("Bard", "The true MOTHERFUCKER!",\
            PlayerData("Bard", "Bard", 100, 100, 10, 10, 5, 2, 5, 0, [], [], [["Foul Language", 0]], [], [], 2,\
            "user slaps target!", True),\
            bardSkillList)]