from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class KeywordData:
    id: str
    desc: str
    triggerText: Tuple
    def load_from(self, other: "KeywordData"):
        self.__dict__.update(other.__dict__)

statusName =\
["AMMO", "CHANT", "DRUNK", "BLEED", "HEMOTOXIN", "INFUSE", "PLAGUE", "TAUNT", "STEALTH"]
statusList =\
[KeywordData("AMMO", "How many of those shots your gun can do. Use wisely!",\
[["gain", "user loads in some ammo!"], ["lose", "user used up stacks ammo!"]]),\
KeywordData("CHANT", "Time till your next skill. Cooldown, much?",\
[["lose", "target keeps on chanting!"]]),\
KeywordData("DRUNK", "Not a sin, just an addiction. +25% Attack, -25% Accuracy per stack, lose 1 stack at end of turn.",\
[["gain", "target feels a bit tipsy!"], ["lose", "user is slowly revovering!"]]),\
KeywordData("BLEED", "'Tis but a scratch.' Deal damage to self equal to stacks at the start of your turn and reduce stacks by half, gain 10% of damage dealt by attacks as bleed.",\
[["gain", "target starts bleeding!"], ["trigger", "target loses some blood!"]]),\
KeywordData("HEMOTOXIN", "Your next instance of bleed damage does not reduce BLEED by half.",\
[["trigger", "The wound won't heal!"]]),\
KeywordData("INFUSE", "Infuse buffs last forever! At the cost of your max juice, however.",\
[["extract", "Extraction Complete."]]),\
KeywordData("PLAGUE", "Increases by 1 at the start of each turn. When stacks exceed 5, BOOM! (Deals 5 damage per stack.)",\
[["gain", "target doesn't look good."], ["trigger", "An Outbreak!"]]),\
KeywordData("TAUNT", "'He's really had it out for yer!'",\
[["gain", "target looks... angrier?"]]),\
KeywordData("STEALTH", "You won't be a target. That is, until you strike...",\
[["gain", "target is now out of sight and mind!"], ["trigger", "target cannot wait any longer!"]])]

statsName =\
["STR", "DEF", "SPD", "PENETRATION", "THORNS", "STARS", "DAMAGEUP", "ACCURACY", "MAX AMMO", "DODGE", "HEALBONUS",\
"BLEEDBONUS", "CRIMSON", "COBALT", "VIOLET"]
statsList =\
[KeywordData("STR", "Strength. How hard you can hit things.", []),\
KeywordData("DEF", "Defense. The more you have, the lesser the pain feels!", []),\
KeywordData("SPD", "Speed. Become faster than light, my friend!", []),\
KeywordData("PENETRATION", "Your attacks ignore stacks percent Defense. No one can block you now.", []),\
KeywordData("THORNS", "He who attacks thou shall receive stacks damage straight back!", []),\
KeywordData("STARS", "An important resource for certain skills. May them guide your path to greatness!", []),\
KeywordData("DAMAGEUP", "Your attacks deal stacks percent more damage. Now go slap some people!", []),\
KeywordData("ACCURACY", "Your skills are now stacks percent more accurate. Headshots have never been easier.", []),\
KeywordData("MAX AMMO", "How much of those funny bullets your gun can hold.", []),\
KeywordData("DODGE", "I hope it never fails.", []),\
KeywordData("HEALBONUS", "Healing is now stacks points more effective. Eh, it's problably just the Placebo effect.", []),\
KeywordData("BLEEDBONUS", "More blood, more fun! Simple math.", []),\
KeywordData("CRIMSON", "Seems red. What if i combine it with cobalt?", []),\
KeywordData("COBALT", "Seems blue. What if i combine it with crimson?", []),\
KeywordData("VIOLET", "Your next stacks attack(s) deal DOUBLE DAMAGE", [])]


keywordName = statusName + statsName
keywordList = statusList + statsList