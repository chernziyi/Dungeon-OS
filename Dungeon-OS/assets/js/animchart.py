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
"PirateUseSkillDrinks Up!", "PirateUseSkillLay Low", "PirateUseSkillAdditional Firepower"]
pirateAnimUseSkillList =\
[AnimData("PirateUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("PirateUseSkillReload", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["reload"]]]),\
AnimData("PirateUseSkillCannon Call", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["chant"]]]),\
AnimData("PirateUseSkillCannon CallChanting", [["replaceImage", "frame1", 210, ["chant"]]]),\
AnimData("PirateUseSkillCannon CallSuccess", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["summon"]]]),\
AnimData("PirateUseSkillDrinks Up!", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["drunk"]]]),
AnimData("PirateUseSkillLay Low!", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["stealth"]]]),
AnimData("PirateUseSkillAdditional Firepower", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 210, ["AOE", "buff"]]])]

pirateAnimUseTraitName =\
["PirateUseTraitPlunderer onEnemyDeath"]
pirateAnimUseTraitList =\
[AnimData("PirateUseTraitPlunderer onEnemyDeath", [["replaceImage", "arr", 210, ["useTrait"]], ["replaceImage", "rra", 1440, ["loot"]]])]

pirateAnimMiscName =\
["PirateStartOfTurn", "PirateDeath", "PirateRebirth"]
pirateAnimMiscList =\
[AnimData("PirateStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("PirateDeath", [["replaceImage", "frame1", 210, ["death"]]]),\
AnimData("PirateRebirth", [["replaceImage", "frame1", 210, ["rebirth"]]])]

pirateAnimName = pirateAnimUseSkillName + pirateAnimUseTraitName + pirateAnimMiscName
pirateAnimList = pirateAnimUseSkillList + pirateAnimUseTraitList + pirateAnimMiscList

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

dissectorAnimUseTraitName =\
["DissectorUseTraitPharmacy onEnemyDeath", "DissectorUseTraitBand-Aid Pro onAllyHurt", "DissectorUseTraitFlight Or Flight onHurt",\
"DissectorUseTraitSneaky Cuts onDamage", "DissectorUseTraitHaemocollector onApplyStatus", "DissectorUseTraitHaemocollector onTrigger"]
dissectorAnimUseTraitList =\
[AnimData("DissectorUseTraitPharmacy onEnemyDeath", [["replaceImage", "glubb", 210, ["useTrait"]], ["replaceImage", "glub glub", 1440, ["loot"]]]),\
AnimData("DissectorUseTraitBand-Aid Pro onAllyHurt", [["replaceImage", "glubb", 210, ["useTrait"]], ["replaceImage", "glub glub", 1440, ["heal"]]]),\
AnimData("DissectorUseTraitFlight Or Flight onHurt", [["replaceImage", "glubb", 210, ["useTrait"]], ["replaceImage", "glub glub", 1440, ["buff"]]]),\
AnimData("DissectorUseTraitSneaky Cuts onDamage", [["replaceImage", "glubb", 210, ["useTrait"]], ["replaceImage", "glub glub", 1440, ["damage"]]]),\
AnimData("DissectorUseTraitHaemocollector onApplyStatus", [["replaceImage", "glubb", 210, ["useTrait"]], ["replaceImage", "glub glub", 1440, ["triggerGain", "trigger"]]]),\
AnimData("DissectorUseTraitHaemocollector onTrigger", [["replaceImage", "glubb", 210, ["useTrait"]], ["replaceImage", "glub glub", 1440, ["loot"]]])]

dissectorAnimMiscName =\
["DissectorStartOfTurn", "DissectorDeath", "DissectorRebirth"]
dissectorAnimMiscList =\
[AnimData("DissectorStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("DissectoreDeath", [["replaceImage", "frame1", 210, ["death"]]]),\
AnimData("DissectorRebirth", [["replaceImage", "frame1", 210, ["rebirth"]]])]

dissectorAnimName = dissectorAnimUseSkillName + dissectorAnimUseTraitName + dissectorAnimMiscName
dissectorAnimList = dissectorAnimUseSkillList + dissectorAnimUseTraitList + dissectorAnimMiscList

qiMasterAnimUseSkillName =\
["Qi MasterUseSkillAttack", "Qi MasterUseSkillCounter", "Qi MasterUseSkillCrimson Infusion", "Qi MasterUseSkillCobalt Infusion",\
"Qi MasterUseSkillOn Guard"]
qiMasterAnimUseSkillList =\
[AnimData("Qi MasterUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("Qi MasterUseSkillCounter", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("Qi MasterUseSkillCrimson Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["buff"]]]),\
AnimData("Qi MasterUseSkillCobalt Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["buff"]]]),\
AnimData("Qi MasterUseSkillCobalt Infusion", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1000, ["counter"]]])]

qiMasterAnimUseTraitName =\
["Qi MasterUseTraitPunching Mastery beforeSkillUse"]
qiMasterAnimUseTraitList =\
[AnimData("Qi MasterUseTraitPunching Mastery beforeSkillUse", [["replaceImage", "kapew", 210, ["useTrait"]], ["replaceImage", "kapow", 1440, ["buff"]]])]

qiMasterAnimMiscName =\
["Qi MasterStartOfTurn", "Qi MasterDeath", "Qi MasterRebirth"]
qiMasterAnimMiscList =\
[AnimData("Qi MasterStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("Qi MasterDeath", [["replaceImage", "frame1", 210, ["death"]]]),\
AnimData("Qi MasterRebirth", [["replaceImage", "frame1", 210, ["rebirth"]]])]

qiMasterAnimName = qiMasterAnimUseSkillName + qiMasterAnimUseTraitName + qiMasterAnimMiscName
qiMasterAnimList = qiMasterAnimUseSkillList + qiMasterAnimUseTraitList + qiMasterAnimMiscList

ravenAnimUseSkillName =\
["RavenUseSkillAttack", "RavenUseSkillVelocity", "RavenUseSkillRusty Graze", "RavenUseSkillBreadcrumbs"]
ravenAnimUseSkillList =\
[AnimData("RavenUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("RavenUseSkillVelocity", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("RavenUseSkillRusty Graze", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "plague"]]]),\
AnimData("RavenUseSkillBreadcrumbs", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "summon"]]])]

ravenAnimUseTraitName =\
["RavenUseTraitAcceleration startOfTurn"]
ravenAnimUseTraitList =\
[AnimData("RavenUseTraitAcceleration startOfTurn", [["replaceImage", "zip", 210, ["useTrait"]], ["replaceImage", "fly", 1440, ["buff"]]])]

ravenAnimMiscName =\
["RavenStartOfTurn", "RavenDeath", "RavenRebirth"]
ravenAnimMiscList =\
[AnimData("RavenStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("RavenDeath", [["replaceImage", "frame1", 210, ["death"]]]),\
AnimData("RavenRebirth", [["replaceImage", "frame1", 210, ["rebirth"]]])]

ravenAnimName =\
ravenAnimUseSkillName + ravenAnimUseTraitName + ravenAnimMiscName
ravenAnimList =\
ravenAnimUseSkillList + ravenAnimUseTraitList + ravenAnimMiscList

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

shamanAnimUseTraitName =\
["ShamanUseTraitHealing Prayer onChant"]
shamanAnimUseTraitList =\
[AnimData("ShamanUseTraitHealing Prayer onChant", [["replaceImage", "alalala", 210, ["useTrait"]], ["replaceImage", "lalalal", 1440, ["AOE", "heal"]]])]

shamanAnimMiscName =\
["ShamanStartOfTurn", "ShamanDeath", "ShamanRebirth"]
shamanAnimMiscList =\
[AnimData("ShamanStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("ShamanDeath", [["replaceImage", "frame1", 210, ["death"]]]),\
AnimData("ShamanRebirth", [["replaceImage", "frame1", 210, ["rebirth"]]])]

shamanAnimName =\
shamanAnimUseSkillName + shamanAnimUseTraitName + shamanAnimMiscName
shamanAnimList =\
shamanAnimUseSkillList + shamanAnimUseTraitList + shamanAnimMiscList

bardAnimUseSkillName =\
["BardUseSkillAttack", "BardUseSkillFoul Language", "BardUseSkillLeer", "BardUseSkillFancy Feet"]
bardAnimUseSkillList =\
[AnimData("BardUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("BardUseSkillFoul Language", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),\
AnimData("BardUseSkillLeer", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["buff"]]]),\
AnimData("BardUseSkillFancy Feet", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["buff"]]])]

bardAnimUseTraitName =\
["BardUseTraitDancer onEnemyMiss"]
bardAnimUseTraitList =\
[AnimData("BardUseTraitDancer onEnemyMiss", [["replaceImage", "heeheeheeha", 210, ["useTrait"]], ["replaceImage", "hahahahee", 1440, ["damage"]]])]

bardAnimMiscName =\
["BardStartOfTurn", "BardDeath", "BardRebirth"]
bardAnimMiscList =\
[AnimData("BardStartOfTurn", [["replaceImage", "frame1", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("BardDeath", [["replaceImage", "frame1", 210, ["death"]]]),\
AnimData("BardRebirth", [["replaceImage", "frame1", 210, ["rebirth"]]])]

bardAnimName =\
bardAnimUseSkillName + bardAnimUseTraitName + bardAnimMiscName
bardAnimList =\
bardAnimUseSkillList + bardAnimUseTraitList + bardAnimMiscList

honeybeeAnimUseSkillName =\
["HoneybeeUseSkillAttack", "HoneybeeUseSkillKamikaze"]
honeybeeAnimUseSkillList =\
[AnimData("HoneybeeUseSkillAttack", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage"]]]),
AnimData("HoneybeeUseSkillKamikaze", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["damage", "die"]]])]

honeybeeAnimMiscName =\
["HoneybeeStartOfTurn", "HoneybeeDeath", "HoneybeeRebirth"]
honeybeeAnimMiscList =\
[AnimData("HoneybeeStartOfTurn", [["replaceImage", "poyo!", 210, ["effect", "bleedTrigger", "plagueTrigger"]]]),\
AnimData("HoneybeeDeath", [["replaceImage", "death", 210, ["death"]]]),\
AnimData("HoneybeeRebirth", [["replaceImage", "rebirth", 210, ["rebirth"]]])]

honeybeeAnimName = honeybeeAnimUseSkillName + honeybeeAnimMiscName
honeybeeAnimList = honeybeeAnimUseSkillList + honeybeeAnimMiscList

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

mindlessRootsAnimUseSkillName = ["Mindless RootsUseSkillAttack"]
mindlessRootsAnimUseSkillList = [AnimData("Mindless RootsUseSkillAttack", [["replaceImage", "frame1", 210, ["useTrait"]], ["replaceImage", "frame2", 1440, ["damage"]]])]

mindlessRootsAnimUseTraitName = ["Mindless RootsUseTraitEnroaching Roots startOfTurn"]
mindlessRootsAnimUseTraitList = [AnimData("Mindless RootsUseTraitEnroaching Roots startOfTurn", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["AOE", "buff"]]])]

mindlessRootsAnimName = mindlessRootsAnimUseSkillName + mindlessRootsAnimUseTraitName
mindlessRootsAnimList = mindlessRootsAnimUseSkillList + mindlessRootsAnimUseTraitList

plantAnimName =\
mindlessRootsAnimName
plantAnimList =\
mindlessRootsAnimList

obeliskAnimUseSkillName = ["ObeliskUseSkillThe Calling"]
obeliskAnimUseSkillList = [AnimData("ObeliskUseSkillThe Calling", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["AOE", "damage"]]])]

obeliskAnimUseTraitName =\
["ObeliskUseTraitFaith-fueled onTrigger", "ObeliskUseTraitFaith-fueled onGainStatus"]
obeliskAnimUseTraitList =\
[AnimData("ObeliskUseTraitFaith-fueled onTrigger", [["replaceImage", "frame1", 210, ["useTrait"]], ["replaceImage", "frame2", 1440, ["useSkill"]]]),\
AnimData("ObeliskUseTraitFaith-fueled onGainStatus", [["replaceImage", "frame1", 210, ["useTrait"]], ["replaceImage", "frame2", 1440, ["trigger"]]])]

obeliskAnimName = obeliskAnimUseSkillName + obeliskAnimUseTraitName
obeliskAnimList = obeliskAnimUseSkillList + obeliskAnimUseTraitList

cultistAnimUseSkillName = ["CultistUseSkillPrayer"]
cultistAnimUseSkillList = [AnimData("CultistUseSkillPrayer", [["replaceImage", "frame1", 210, ["useSkill"]], ["replaceImage", "frame2", 1440, ["pray"]]])]

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