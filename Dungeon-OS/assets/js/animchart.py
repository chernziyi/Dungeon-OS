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
["PirateUseSkillAttack", "PirateUseSkillReload", "PirateUseSkillCannon Call", "PirateUseSkillCannon CallChanting", "PirateUseSkillCannon CallSuccess",\
"PirateUseSkillDrinks Up!", "PirateUseSkillLay Low"]
pirateAnimUseSkillList =\
[AnimData("PirateUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("PirateUseSkillReload", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["reload"]]]),\
AnimData("PirateUseSkillCannon Call", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["chant"]]]),\
AnimData("PirateUseSkillCannon CallChanting", [["replaceImage", "frame1", 210, ["chant"]]]),\
AnimData("PirateUseSkillCannon CallSuccess", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["summon"]]]),\
AnimData("PirateUseSkillDrinks Up!", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["drunk"]]]),
AnimData("PirateUseSkillLay Low!", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["stealth"]]])]

pirateAnimMiscName =\
["PirateStartOfTurn"]
pirateAnimMiscList =\
[AnimData("PirateStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]])]

pirateAnimName = pirateAnimUseSkillName + pirateAnimMiscName
pirateAnimList = pirateAnimUseSkillList + pirateAnimMiscList

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

dissectorAnimMiscName =\
["DissectorStartOfTurn"]
dissectorAnimMiscList =\
[AnimData("DissectorStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]])]

dissectorAnimName = dissectorAnimUseSkillName + dissectorAnimMiscName
dissectorAnimList = dissectorAnimUseSkillList + dissectorAnimMiscList

qiMasterAnimUseSkillName =\
["Qi MasterUseSkillAttack", "Qi MasterUseSkillCounter", "Qi MasterUseSkillCrimson Infusion", "Qi MasterUseSkillCobalt Infusion",\
"Qi MasterUseSkillOn Guard"]
qiMasterAnimUseSkillList =\
[AnimData("Qi MasterUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("Qi MasterUseSkillCounter", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("Qi MasterUseSkillCrimson Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["buff"]]]),\
AnimData("Qi MasterUseSkillCobalt Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["buff"]]]),\
AnimData("Qi MasterUseSkillCobalt Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["counter"]]])]

qiMasterAnimMiscName =\
["Qi MasterStartOfTurn"]
qiMasterAnimMiscList =\
[AnimData("Qi MasterStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]])]

qiMasterAnimName = qiMasterAnimUseSkillName + qiMasterAnimMiscName
qiMasterAnimList = qiMasterAnimUseSkillList + qiMasterAnimMiscList

ravenAnimUseSkillName =\
["RavenUseSkillAttack", "RavenUseSkillVelocity", "RavenUseSkillRusty Graze", "RavenUseSkillBreadcrumbs"]
ravenAnimUseSkillList =\
[AnimData("RavenUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("RavenUseSkillVelocity", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("RavenUseSkillRusty Graze", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "plague"]]]),\
AnimData("RavenUseSkillBreadcrumbs", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "summon"]]])]

ravenAnimMiscName =\
["RavenStartOfTurn"]
ravenAnimMiscList =\
[AnimData("RavenStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]])]

ravenAnimName =\
ravenAnimUseSkillName + ravenAnimMiscName
ravenAnimList =\
ravenAnimUseSkillList + ravenAnimMiscList

shamanAnimUseSkillName =\
["ShamanUseSkillAttack", "ShamanUseSkillBolt", "ShamanUseSkillBoltChanting", "ShamanUseSkillBoltSuccess", "ShamanUseSkillChilling Air",\
"ShamanUseSkillSlippery Sand", "ShamanUseSkillSlippery SandChanting", "ShamanUseSkillSlippery SandSuccess"]
shamanAnimUseSkillList =\
[AnimData("ShamanUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("ShamanUseSkillBolt", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["chant"]]]),\
AnimData("ShamanUseSkillBoltChanting", [["replaceImage", "frame1", 1440, ["chant"]]]),\
AnimData("ShamanUseSkillBoltSuccess", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["AOE", "damage"]]]),\
AnimData("ShamanUseSkillChilling Air", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["AOE", "buff"]]]),\
AnimData("ShamanUseSkillSlippery Sand", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["chant"]]]),\
AnimData("ShamanUseSkillSlippery SandChanting", [["replaceImage", "frame1", 1440, ["chant"]]]),\
AnimData("ShamanUseSkillSlippery SandSuccess", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["summon"]]])]

shamanAnimMiscName =\
["ShamanStartOfTurn"]
shamanAnimMiscList =\
[AnimData("ShamanStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]])]

shamanAnimName =\
shamanAnimUseSkillName + shamanAnimMiscName
shamanAnimList =\
shamanAnimUseSkillList + shamanAnimMiscList

bardAnimUseSkillName =\
["BardUseSkillAttack", "BardUseSkillFoul Language", "BardUseSkillLeer", "BardUseSkillFancy Feet"]
bardAnimUseSkillList =\
[AnimData("BardUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("BardUseSkillFoul Language", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("BardUseSkillLeer", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["buff"]]]),\
AnimData("BardUseSkillFancy Feet", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["buff"]]])]

bardAnimMiscName =\
["bardStartOfTurn"]
bardAnimMiscList =\
[AnimData("bardStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]])]

bardAnimName =\
bardAnimUseSkillName + bardAnimMiscName
bardAnimList =\
bardAnimUseSkillList + bardAnimMiscList

honeybeeAnimUseSkillName =\
["HoneybeeUseSkillAttack", "HoneybeeUseSkillKamikaze"]
honeybeeAnimUseSkillList =\
[AnimData("HoneybeeUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),
AnimData("HoneybeeUseSkillKamikaze", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "die"]]])]

honeybeeAnimName = honeybeeAnimUseSkillName
honeybeeAnimList = honeybeeAnimUseSkillList

hardworkingBeeAnimUseSkillName =\
["Hardworking BeeUseSkillKamikaze", "Hardworking BeeUseSkillOvertime"]
hardworkingBeeAnimUseSkillList =\
[AnimData("Hardworking BeeUseSkillKamikaze", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "die"]]]),\
AnimData("Hardworking BeeUseSkillOvertime", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["undying"]]])]

hardworkingBeeAnimName = hardworkingBeeAnimUseSkillName
hardworkingBeeAnimList = hardworkingBeeAnimUseSkillList

beeAnimName =\
honeybeeAnimName + hardworkingBeeAnimName
beeAnimList =\
honeybeeAnimList + hardworkingBeeAnimList

mindlessRootsAnimUseSkillName =\
["Mindless RootsUseSkillAttack"]
mindlessRootsAnimUseSkillList =\
[AnimData("Mindless RootsUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

mindlessRootsAnimName = mindlessRootsAnimUseSkillName
mindlessRootsAnimList = mindlessRootsAnimUseSkillList

plantAnimName =\
mindlessRootsAnimName
plantAnimList =\
mindlessRootsAnimList

obeliskAnimUseSkillName = ["ObeliskUseSkillThe Calling"]
obeliskAnimUseSkillList = ["ObeliskUseSkillThe Calling", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["AOE", "damage"]]]]

obeliskAnimName = obeliskAnimUseSkillName
obeliskAnimList = obeliskAnimUseSkillList

cultistAnimUseSkillName = ["CultistUseSkillPrayer"]
cultistAnimUseSkillList = ["CultistUseSkillPrayer", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["pray"]]]]

cultistAnimName = cultistAnimUseSkillName
cultistAnimList = cultistAnimUseSkillList

cultAnimName =\
obeliskAnimName + cultistAnimName
cultAnimList =\
obeliskAnimList + cultistAnimList

cannonAnimUseSkillName = ["CannonUseSkillAttack"]
cannonAnimUseSkillList = [AnimData("CannonUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

cannonAnimName = cannonAnimUseSkillName
cannonAnimList = cannonAnimUseSkillList

pirateSummonAnimName =\
cannonAnimName
pirateSummonAnimList =\
cannonAnimList

birbAnimUseSkillName = ["BirbUseSkillAttack"]
birbAnimUseSkillList = [AnimData("BirbUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

birbAnimName = birbAnimUseSkillName
birbAnimList = birbAnimUseSkillList

ravenSummonAnimName =\
birbAnimName
ravenSummonAnimList =\
birbAnimList

slipperySandAnimUseTraitName = ["Slippery SandUseTraitSlippery onEnemyUseSkill"]
slipperySandAnimUseTraitList =\
[AnimData("Slippery SandUseTraitSlippery onEnemyUseSkill", [["replaceImage", "frame1", 210, ["useTrait"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

slipperySandAnimName = slipperySandAnimUseTraitName
slipperySandAnimList = slipperySandAnimUseTraitList

shamanSummonAnimName =\
slipperySandAnimName
shamanSummonAnimList =\
slipperySandAnimList

animName = pirateAnimName + dissectorAnimName + qiMasterAnimName + ravenAnimName + shamanAnimName + bardAnimName +\
beeAnimName + plantAnimName + cultAnimName + pirateSummonAnimName + ravenSummonAnimName + shamanSummonAnimName
animList = pirateAnimList + dissectorAnimList + qiMasterAnimList + ravenAnimList + shamanAnimList + bardAnimList +\
beeAnimList + plantAnimList + cultAnimList + pirateSummonAnimList + ravenSummonAnimList + shamanSummonAnimList