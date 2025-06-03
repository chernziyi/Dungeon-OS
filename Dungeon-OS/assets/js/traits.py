from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class TraitData:
    id: str
    secondaryText: str
    startingUses: int
    info: Tuple
    desc: str
    actualDesc: str
    useText: Tuple
    price: int
    image: str
    def load_from(self, other: "TraitData"):
        self.__dict__.update(other.__dict__)

#all info refs: all should start with: self or not, mates or not, aoe or not.

neutralTraitName =\
["Enroaching Roots", "Swarm", "One With Nature", "Slippery"]
neutralTraitList =\
[TraitData("Enroaching Roots", "", 0, [["startOfTurn", False, False, True, "buffDuration", "", "buff", "spd", -1, "buffEnd"]],\
"Roots creeping, entangling all who come near.",\
"Start Of Turn: All enemies receive spdAmount SPD",
[["startOfTurn", "The roots resume their slow advance..."]], 0, ""),\
TraitData("Swarm", "", 0, [["onSummon", True, True, False, "swarm", 1]],\
"On Summon: gain 1 SWARM.",
"Teamwork makes the nightmare!",\
[["onSummon", "user joins its bretheren!"]], 0, ""),\
TraitData("One With Nature", "", 0, [["invulnerable"]],\
"Yeah, it can't die. Or get damaged. I mean...",\
"Immune to all damage and cannot die.",
[], 0, ""),\
TraitData("Slippery", "", 0, [["onEnemyUseSkill", False, False, False, "triggerChance", 0.5, "userToTarget", "selfDamage", "str", 0.5, 0]],\
"Whoopsies, I fell.",\
"When an enemy uses a skill: target deals damage to itself.",
[["onEnemyUseSkill", "target slips!"]], 0, "")]

pirateTraitName =\
["Plunderer"]
pirateTraitList =\
[TraitData("Plunderer", "", 0, [["onEnemyDeath", True, False, False, "loot", "coins", 5]],\
"Some extra gold for the road. How did they find it? Nobody knows!",\
"When an enemy dies: Gain lootAmount coins.",
[["onEnemyDeath", "user finds some coins from... somewhere..."]], 80, "")]

dissectorTraitName =\
["Pharmacy", "Band-Aid Pro", "Fight Or Flight", "Sneaky Cuts"]
dissectorTraitList =\
[TraitData("Pharmacy", "", 0, [["onEnemyDeath", True, False, False, "loot", "potion", 1]],\
"'What? I am a person of medicine, after all.",\
"When an enemy dies: Gain lootAmount potion.",
[["onEnemyDeath", "user concocts a vial from the remains!"]], 150, ""),
TraitData("Band-Aid Pro", "", 0, [["onAllyHurt", False, True, False, "heal", 1, ""]],
"Just like how my parents do it.",
"When an ally is hurt: heal them for healAmount",
[["onAllyHurt", "user slaps a band-aid on target's wound!"]], 200, ""),
TraitData("Fight or Flight", "", 0, [["onHurt", True, False, False, "buffDuration", 2, "buff", "spd", 1, "buffEnd"]],\
"People when they step on Legos:",\
"When you are hurt: Gain spdAmount SPD for buffDuration turns.",
[["onHurt", "user becomes stimulated!"]], 100, ""),
TraitData("Sneaky Cuts", "usesPerTurn", 1, 
[["onDamage", False, False, False, "damage", "fixed", 1, ""]], 
"Every strike brings a little extra pain.", 
"When you deal damage: deal damageAmount damage. Uses Per Turn: secondaryNumber.",
[["onDamage", "user slashes a little deeper!"]], 150, "")]

qiMasterTraitName =\
["Punching Mastery"]
qiMasterTraitList =\
[TraitData("Punching Mastery", "", 0, [["beforeSkillUse", True, False, False, "Attack", "buffDuration", 1, "buff", "damageUp", 0.2, "buffEnd"]],\
"'Just use your fists. It ain't that hard.'",\
"When Using Attack: Gain damageUpAmount DAMAGEUP for buffDuration turns.",
[["beforeSkillUse", "user's fists seem stronger!"]], 80, "")]

ravenTraitName =\
["Acceleration"]
ravenTraitList =\
[TraitData("Acceleration", "", 0, [["startOfTurn", True, False, False, "buff", "spd", 1, "buffEnd"]],\
"v = u + at",\
"Start Of Turn: Gain spdAmount SPD.",
[["startOfTurn", "user speeds up!"]], 150, "")]

shamanTraitName =\
["Healing Prayer"]
shamanTraitList =\
[TraitData("Healing Prayer", "", 0, [["onChant", False, True, True, "heal", 3]],\
"The voice of Luna shall comfort the wounded.",\
"On Chant: Heal all allies for healAmount.",
[["onChant", "user's chant heals some wounds!"]], 80, "")]
 
bardTraitName =\
["Dancer"]
bardTraitList =\
[TraitData("Dancer", "", 0, [["onEnemyMiss", False, False, False, "damage", "str", 0.5, 0.2]],\
"'Not my fault, just a skill issue.'",\
"When an enemy Misses: deal damageAmount damage to them.",
[["onEnemyMiss", "user pokes the incoming target!"]], 100, "")]

traitName = neutralTraitName + pirateTraitName + dissectorTraitName + qiMasterTraitName + ravenTraitName\
         + shamanTraitName + bardTraitName
traitList = neutralTraitList + pirateTraitList + dissectorTraitList + qiMasterTraitList + ravenTraitList\
         + shamanTraitList + bardTraitList