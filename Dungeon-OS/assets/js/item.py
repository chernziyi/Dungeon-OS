from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class ItemData:
    id: str
    type: str
    targets: bool #True if the skill targets your mates, #False if otherwise
    self: bool #True if the skill targets yourself, #False if otherwise
    AOE: bool #True if AOE, False if otherwise
    info: List
    desc: str
    actualDesc: str
    image: str
    useText: str
    price: int
    def load_from(self, other: "ItemData"):
        self.__dict__.update(other.__dict__)
#all info refs: slow: "slow", slow amount, slow duration

potionNeutralName =\
["Honeypot", "Herbal Leaf"]
potionNeutralList =\
[ItemData("Honeypot", "potion", False, False, False, ["buffDuration", "", "buff", "spd", -2, "buffEnd"],\
"Honey so sticky electrons get stuck in it! Now for only 3 coins.",\
"assets/sprites/Items/Potions/Png/Honeypot.png",\
"Target receives spdAmount SPD.",
"user yeets the item at target, gumming them up!", 10),\
ItemData("Herbal Leaf", "potion", True, True, False, ["heal", 5],\
"This leaf means the diffrence between death and a delayed, minty death.",\
"Target heals by healAmount.",
"assets/sprites/Items/Potions/Png/Herbal Leaf.png",\
"target slaps the item on their wounds!", 10)]

potionName = potionNeutralName
potionList = potionNeutralList

weaponDissectorName =\
["Scalpel", "Balisong"]
weaponDissectorList =\
[ItemData("Scalpel", "weapon", False, False, False, ["str", 2, "bleedBonus", 1],\
"Scalpel, please?",\
"+strAmount STR, +bleedBonusAmount BLEEDBONUS",
"assets/sprites/Items/Potions/Png/Honeypot.png",\
"user equips Scalpel!", 30),
ItemData("Balisong", "weapon", False, False, False, 
["str", 1, "trait", "Sneaky Cuts", 1], 
"Also known as a butterfly knife, you can perform cool tricks with is, i guess.", 
"+strAmount STR, +traitAmount Sneaky Cuts.",
"assets/sprites/Items/Potions/Png/Honeypot.png", 
"user equips Balisong!", 200)]

weaponName = weaponDissectorName
weaponList = weaponDissectorList

relicDissectorName = \
["Healing For Dummies"]
relicDissectorList =\
[ItemData("Healing For Dummies", "relic", False, False, False, ["healBonus", 3],\
"A simple guide to not let people die that fast. Page 1: Use bandages.",\
"+healBonusAmount HEALBONUS.",
"assets/sprites/Items/Potions/Png/Honeypot.png",\
"user equips Healing For Dummies!", 50)]

relicName = relicDissectorName
relicList = relicDissectorList

itemName = potionName + weaponName + relicName
itemList = potionList + weaponList + relicList