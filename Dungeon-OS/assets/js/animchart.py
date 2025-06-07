from dataclasses import dataclass
from typing import List
from typing import Tuple


@dataclass
class AnimData:
    id: str
    info: Tuple
    def load_from(self, other: "AnimData"):
        self.__dict__.update(other.__dict__)

["Pirate", "Dissector", "Qi Master", "Raven", "Shaman", "Bard"]

pirateAnimUseSkillName =\
["PirateUseSkillAttack"]
pirateAnimUseSkillList =\
[AnimData("PirateUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

pirateAnimName = pirateAnimUseSkillName
pirateAnimList = pirateAnimUseSkillList

dissectorAnimUseSkillName =\
["DissectorUseSkillBloody Jabs"]
dissectorAnimUseSkillList =\
[AnimData("DissectorUseSkillBloody Jabs", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 200, ["damage", "bleed"]],\
["replaceImage", "frame2", 200, ["damage", "bleed"]], ["replaceImage", "frame2", 200, ["damage", "bleed"]]])]

dissectorAnimName = dissectorAnimUseSkillName
dissectorAnimList = dissectorAnimUseSkillList

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