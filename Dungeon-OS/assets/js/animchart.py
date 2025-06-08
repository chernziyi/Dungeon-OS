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
["PirateUseSkillAttack", "PirateUseSkillCannon Call", "PirateUseSkillCannon CallChanting", "PirateUseSkillCannon CallSuccess",\
"PirateUseSkillDrinks Up!", "PirateUseSkillLay Low"]
pirateAnimUseSkillList =\
[AnimData("PirateUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("PirateUseSkillCannon Call", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["chant"]]]),\
AnimData("PirateUseSkillCannon CallChanting", [["replaceImage", "frame1", 210, ["chant"]]]),\
AnimData("PirateUseSkillCannon CallSuccess", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["summon"]]]),\
AnimData("PirateUseSkillDrinks Up!", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["drunk"]]]),
AnimData("PirateUseSkillLay Low!", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["stealth"]]])]

pirateAnimName = pirateAnimUseSkillName
pirateAnimList = pirateAnimUseSkillList

dissectorAnimUseSkillName =\
["DissectorUseSkillAttack", "DissectorUseSkillBloody Jabs", "DissectorUseSkillBandages", "DissectorUseSkillPuncture", "DissectorUseSkillTrade Blows",\
"DissectorUseSkillOpen Wound", "DissectorUseSkillMessy Healing", "DissectorUseSkillTransplant"]
dissectorAnimUseSkillList =\
[AnimData("DissectorUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("DissectorUseSkillBloody Jabs", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["damage", "bleed"]],\
["replaceImage", "frame3", 1000, ["damage", "bleed"]], ["replaceImage", "frame4", 1000, ["damage", "bleed"]]]),\
AnimData("DissectorUseSkillBandages", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 3000, ["heal"]]]),\
AnimData("DissectorUseSkillPuncture", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 2000, ["damage", "buff"]]]),\
AnimData("DissectorUseSkillTrade Blows", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 500, ["damage"]],\
["replaceImage", "frame3", 500, ["selfDamage"]]]),\
AnimData("DissectorUseSkillOpen Wound", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 500, ["bleed", "hemotoxin"]]]),\
AnimData("DissectorUseSkillMessy Healing", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 500, ["heal"]],\
["replaceImage", "frame3", 500, ["bleed"]]]),\
AnimData("DissectorUseSkillTransplant", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 500, ["selfDamage"]],\
["replaceImage", "frame3", 500, ["heal"]]])]

dissectorAnimName = dissectorAnimUseSkillName
dissectorAnimList = dissectorAnimUseSkillList

qiMasterAnimUseSkillName =\
["Qi MasterUseSkillCrimson Infusion", "Qi MasterUseSkillCobalt Infusion", ]
qiMasterAnimUseSkillList =\
[AnimData("Qi MasterUseSkillCrimson Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["buff"]]]),\
AnimData("Qi MasterUseSkillCobalt Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["buff"]]])]

qiMasterAnimName = qiMasterAnimUseSkillName
qiMasterAnimList = qiMasterAnimUseSkillList

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