from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class SkillData:
    id: str
    juiceCost: int
    targets: bool #True if the skill targets your mates, #False if otherwise
    self: bool #True if the skill targets yourself, #False if otherwise
    AOE: bool #True if AOE, False if otherwise
    randomTargets: bool
    multi: int #how many times?
    acc: str
    info: List
    desc: str
    actualDesc: str
    useText: Tuple  #some cool on use text, [["-", default], [skillcon, text based on skillcon]]
    price: int
    image: str
    def load_from(self, other: "SkillData"):
        self.__dict__.update(other.__dict__)

#all info refs: damage: "damage", "which stat", "* how much", "damage variation"
#die: "die"
#ammo: "ammo", "increase/ decrease ammo count"
#reload: "reload"
#chant: "chant", "no of turns"
#summon: "summon", creature name
#drunk: "drunk", "applychance", "stacks", "stackChange", "Duration". drunk increases atk but decreases acc
#bleed: "bleed", "applychance", "stacks". bleed deals dmg = stacks and halves itself, also increases by 10% of damage dealt.
#plague: "plague", "applychance", "stacks".
#infuse: "infuse", uses max mana, buffs last forever, can take back
#cleanse: "cleanse", "stacks". removes debuffs. duh.
#cantrip: "cantrip", increases
#buff: "buff", "thing you wanna buff", "amount", rinse and repeat, "buffEnd" buff effects SHOULD last as long as buff is active
#neutralSkills are all enemy skills and skills anyone could have 

neutralSkillName =\
["Attack", "Reload", "Counter"]
neutralSkillList =\
[SkillData("Attack", 0, False, False, False, False, 1, 0.8, ["damage", "str", 2, 0.2],\
"The simplest of strikes, the most basic form of offense, yet slays foes every time.",\
"Deal damageAmount damage.",\
[["-", "user goes for a strike at target!"]], 0, ""),\
SkillData("Reload", 0, False, True, False, False, 1, 100, ["reload"],\
"Remember kids, switching to another skill is faster than reloading.",\
"Reload.",\
["-", "user reloads, ready for another shot."], 0, ""),\
SkillData("Counter", 0, False, False, False, False, 1, 100, ["damage", "str", 1, 0.2],\
"Rebellion at it's essence.",\
"Deal damageAmount damage back at the attacker.",\
[["-", "user strikes back at target!"]], 0, "")]

beeSkillName =\
["Kamikaze", "Overtime"]
beeSkillList =\
[SkillData("Kamikaze", 10, False, False, False, False, 1, 0.8, ["damage", "str", 4, 0.2, "die"],\
"FREEEEEEEEEDOOOOOOOOOM! Kills the user.",\
"Deal damageAmount damage, then die.",\
[["-", "user goes out with a suicidal charge towards target!"]], 0, ""),
SkillData("Overtime", 30, False, True, False, False, 1, 100, ["undying", 1],\
"Even in death, unpaid overtime exists.",\
"Gain undyingAmount UNDYING",\
[["-", "user takes up another shift!"]], 0, "")]

cultistSkillName =\
["The Calling", "Prayer"]
cultistSkillList =\
[SkillData("The Calling", 40, False, False, True, False, 1, 100, ["damage", "FAITH", 2, 0.2, "faith", "loseAll"],\
"Get ready to convert, cause your God can't save you now.",\
"Deal damageAmount damage to all enemies. Lose all FAITH",\
[["-", "user blasts a beam of faith!"]], 0, ""),
SkillData("Prayer", 20, False, True, False, False, 1, 100, ["pray", 10],\
"[Prayer removed for your safety]",\
"Pray prayAmount.",\
[["-", "user mutters the holy texts!"]], 0, "")]

pirateSkillName =\
["Pistol Shot", "Cannon Call", "Drinks Up!", "Lay Low"]
pirateSkillList =\
[SkillData("Pistol Shot", 10, False, False, False, False, 1, 1.25, ["damage", "str", 4, 0.2, "ammo", -1],\
"Gunfire is not to be taken lightly. Reloading Necessary.",\
"Deal damageAmount damage. Uses ammoAmount ammo.",\
[["-", "user shoots target with a trusty pistol!"]], 40, ""),\
SkillData("Cannon Call", 10, False, True, False, False, 1, 100, ["chant", 2, "summon", "Cannon"],\
"What's a pirate without a gun and a larger one?",\
"Chant chantAmount. Summon summoned.",\
[["-","user mutters some unknown words."], ["chant", "A Cannon drops from the sky!"]], 80, ""),\
SkillData("Drinks Up!", 5, False, True, False, False, 1, 100, ["drunk", 1, 1, 0, 3],\
"All drinks taste better in a fight!",\
"User gains drunkDuration turns of DRUNK drunkStacks.",\
[["-", "user chugs down a cup of rum, feeling a bit tipsy after."]], 50, ""),\
SkillData("Lay Low", 15, False, True, False, False, 1, 100, ["stealth", 1],\
"The must-take lesson for any Pirate: How to not get caught",\
"Gain STEALTH stealthAmount",\
[["-", "user lays low!"]], 50, "")]

dissectorSkillName =\
["Bloody Jabs", "Bandages", "Puncture", "Trade Blows", "Open Wound", "Messy Healing", "Transplant"]
dissectorSkillList =\
[SkillData("Bloody Jabs", 10, False, False, False, False, 3, 0.7, ["damage", "str", 0.75, 0.2, "bleed", 0.5, 1],
"Strikes-a-plenty, Blood-a-plenty!",
"Deals damageAmount damage multi times and each strike has a bleedApplyChance chance to inflict BLEED bleedStacks.",
[["-", "user jabs, aiming for the vessels!"]], 50, ""),
SkillData("Bandages", 5, True, False, False, False, 1, 0.9, ["heal", 10, ""],
"Bandages, the medical equivalent of duct tape",
"Heals target for healAmount.",
[["-", "user bandages target up!"]], 60, ""),
SkillData("Puncture", 20, False, False, False, False, 1, 0.8, ["damage", "str", 3.0, 0.2, "buffDuration", "", "buff", "def", -2, "buffEnd"],
"Also used as a replacement for hole punchers.",
"Deals damageAmount damage. Reduce the target's DEF by defAmount.",
[["-", "user thrusts precisely, aiming to cripple defense!"]],  70, ""),
SkillData("Trade Blows", 15, False, False, False, False, 1, 0.8, 
["cantrip", "selfDamage", "str", 2.0, 0.2, "damage", "str", 3.0, 0.2], 
"Ow for me, more Ows for you!", 
"Cantrip. Deal selfDamageAmount damage to self, then deal damageAmount damage.", 
[["-", "user trades injuries for a stronger strike!"]], 70, ""),
SkillData("Open Wound", 25, False, False, False, False, 1, 0.8, ["bleed", 1.0, 10, "hemotoxin", 1.0, 1], 
"More blood for the special guy~", 
"Inflicts bleedStacks BLEED and hemotoxinAmount HEMOTOXIN..", 
[["-", "user opens a wound which is hard to heal!"]], 100, ""),
SkillData("Messy Healing", 15, True, False, False, False, 1, 100, ["bleed", 1.0, 5, "heal", 20, ""],
"WDYM 'Heal better'? There's monsters EVERYWHERE!",
"Applies bleedAmount BLEED to an ally and heal them for healAmount.",
[["-", "user applies a painful remedy!"]], 70, ""),
SkillData("Transplant", 35, True, False, False, False, 1, 100, ["selfDamage", "max", 10, "", "heal", ["lastDamage", "user", "lastDamage", "user"], "max"],
"Hurt my life, save a life.",
"Deal selfDamageAmount damage to self and lose that much MAXHP, then heal target for twice the damage received and they gain that much MAXHP.",
[["-", "User cuts off some of themself and transplants it on target!"]], 180, "")]

qiMasterSkillName =\
["Crimson Infusion", "Cobalt Infusion", "On Guard"]
qiMasterSkillList =\
[SkillData("Crimson Infusion", 5, False, True, False, False, 1, 100, ["cantrip", "infuse", "buff", "str", 1, "crimson", 1, "buffEnd"],\
"Fists becomes redder, punches becomes stronger. Simple.",\
"Cantrip. Infuse. Gain strAmount strength and Crimson crimsonAmount.",\
[["-", "target's fists glow red!"]], 50, ""),\
SkillData("Cobalt Infusion", 5, False, True, False, False, 1, 100, ["cantrip", "infuse", "buff", "def", 1, "cobalt", 1, "buffEnd"],\
"Protects your insides. Always handy.",\
"Cantrip. Infuse. Gains defAmount defense and Cobalt cobaltAmount.",\
[["-", "target's body glows blue!"]], 50, ""),\
SkillData("On Guard", 5, False, True, False, False, 1, 100, ["cantrip", "counter", 1],\
"As one becomes aware of their surroundings, they can notice attacks from a mile away.",\
"User gains counterAmount COUNTER.",\
[["-", "user becomes alerted!"]], 50, "")]

ravenSkillName =\
["Velocity", "Rusty Graze", "Breadcrumbs"]
ravenSkillList =\
[SkillData("Velocity", 5, False, False, False, False, 1, 0.8, ["damage", "spd", 2, 0.2],\
"'Well, this is way over the speed limit.'",\
"Deal damageAmount damage. Uses Speed instead of Strength.",\
[["-", "user runs into the target!"]], 50, ""),\
SkillData("Rusty Graze", 10, False, False, False, False, 1, 0.8, ["damage", "str", 2, 0.2, "plague", 1, 1],\
"Does not come with the vaccine.",\
"Deal damageAmount damage. Inflict PLAGUE plagueStacks.",\
[["-", "user cuts target with a rusty knife!"]], 60, ""),\
SkillData("Breadcrumbs", 5, False, True, False, False, 1, 100, ["cantrip", "summon", "Birb"],\
"What's the worst one Birb can do? What do you mean there's more?",\
"Cantrip. Summon ummoned.",\
[["-", "user convinces Birbs to fight for them using bread!"]], 70, "")]

shamanSkillName =\
["Bolt", "Chilling Air", "Slippery Sand"]
shamanSkillList =\
[SkillData("Bolt", 10, False, False, True, False, 1, 0.8, ["chant", 1, "damage", "str", 2, 0.2],\
"Zip! Zap! Zop!.",\
"Deal damageAmount damage to all enemies.",\
[["-", "user mutters some words."], ["chant", "user summons LIGHTNING!"]], 50, ""),\
SkillData("Chilling Air", 15, False, False, True, False, 1, 100, ["buffDuration", "", "buff", "str", -1, "spd", -1, "buffEnd"],\
"Ey! Who turned on the AC?",\
"Aall enemies receive strAmount STR and spdAmount SPD",\
[["-", "The air gets colder..."]], 60, ""),\
SkillData("Slippery Sand", 15, False, True, False, False, 1, 100, ["chant", 1, "summon", "Slippery Sand"],\
"Beware: Sand is slippery.",\
"Chant chantAmount. Summon summoned.",\
[["-", "user mutters some words."], ["chant", "user conjures some Slippery Sand!"]], 40, "")]

bardSkillName =\
["Foul Language", "Leer", "Fancy Feet"]
bardSkillList =\
[SkillData("Foul Language", 5, False, True, False, False, 1, 100, ["cantrip", "randomTarget", "damage", "str", 3, 0.2],\
"'**** ******.'",\
"deal damageAmount damage to a random target. (Excluding yourself)",\
[["-", "'Your Mother.'"]], 50, ""),\
SkillData("Leer", 10, False, False, False, False, 1, 100, ["taunt", 1, 2],\
"'Even a look pisses you off? Sheesh!'",\
"Inflict TAUNT tauntStacks.",\
[["-", "user looks at target slyly!"]], 40, ""),\
SkillData("Fancy Feet", 10, False, True, False, False, 1, 100, ["buffDuration", 2, "buff", "dodge", 0.25, "buffEnd"],\
"Can be countered by someone wielding Fancier Feet.",\
"gain dodgeAmount DODGE for buffDuration turns.",\
[["-", "user shows off some footwork!"]], 40, "")]

skillName = neutralSkillName + beeSkillName + cultistSkillName + pirateSkillName + dissectorSkillName + qiMasterSkillName + ravenSkillName +\
shamanSkillName + bardSkillName
skillList = neutralSkillList + beeSkillList + cultistSkillList + pirateSkillList + dissectorSkillList + qiMasterSkillList + ravenSkillList +\
shamanSkillList + bardSkillList