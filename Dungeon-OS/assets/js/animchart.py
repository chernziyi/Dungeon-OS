from dataclasses import dataclass
from typing import List
from typing import Tuple


@dataclass
class AnimData:
    id: str
    animChart: Tuple
    def load_from(self, other: "AnimData"):
        self.__dict__.update(other.__dict__)

["Pirate", "Dissector", "Qi Master", "Raven", "Shaman", "Bard"]
pirateAnimName =\
[]
pirateAnimList =\
[]

pirateAnimUseSkillName =\
["pirateUseSkillAttack"]
pirateAnimUseSkillList =\
[AnimData("pirateUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

dissectorAnimName =\
[]
dissectorAnimList =\
[]

qiMasterAnimName =\
[]
qiMasterAnimList =\
[]

ravenAnimName =\
[]
ravenAnimList =\
[]

shamanAnimName =\
[]
shamanAnimList =\
[]

bardAnimName =\
[]
bardAnimList =\
[]

animName = pirateAnimName + dissectorAnimName + qiMasterAnimName + ravenAnimName + shamanAnimName + bardAnimName
animList = pirateAnimList + dissectorAnimList + qiMasterAnimList + ravenAnimList + shamanAnimList + bardAnimList