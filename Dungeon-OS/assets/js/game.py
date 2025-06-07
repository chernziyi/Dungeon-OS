from ui import generateWindow, generateStatusWindow, generateBagWindow, generateOSScreen,\
setPosition, choose, Notification, addText, addDescriptionToImage, makeIconDraggable, generateSaveWindow,\
generateShopWindow, effectNumber, animlocateFrame, animAdd, animStart, animLoad, updateHp, updateJuice, animSeekAndDestroy,\
WaitForAnimFinished
from player import PlayerData, classes, classList
from enemy import EnemyData, enemyStats, enemyName
from level import LevelData, combatZone1, combatZone0
from skills import SkillData, skillName, skillList, pirateSkillList, dissectorSkillList, qiMasterSkillList,\
ravenSkillList, shamanSkillList, bardSkillList
from traits import TraitData, traitName, traitList, pirateTraitList, dissectorTraitList, qiMasterTraitList,\
ravenTraitList, shamanTraitList, bardTraitList
from item import ItemData, itemName, itemList
from upgrades import upgradeTable
from animchart import animName, animList

from pyodide.ffi import create_proxy # type: ignore
from dataclasses import asdict
import random, asyncio, math, json, copy, ui
from js import document, Blob, URL, FileReader, window, setTimeout

window_width = window.innerWidth
window_height = window.innerHeight

classChoice = []

partyNumber = 0
partyList = []
player1 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
player2 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
player3 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
player4 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)

playerVisual1 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
playerVisual2 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
playerVisual3 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
playerVisual4 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)

clone1 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
clone2 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
clone3 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)
clone4 = PlayerData("", "", 0, 0, 0, 0, 0, 0, 0, 0, [], [], [], [], [], 0, "", False)

party = [None, player1, player2, player3, player4]
cloneParty = [None, clone1, clone2, clone3, clone4]

summonNumber = 0
summonList = []
summon1 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
summon2 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
summon3 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
summon4 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)

summonVisual1 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
summonVisual2 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
summonVisual3 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
summonVisual4 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)

summonParty = [None, summon1, summon2, summon3, summon4]

enemyNumber = 0
enemyList = []
enemy1 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
enemy2 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
enemy3 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
enemy4 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)

enemyVisual1 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
enemyVisual2 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
enemyVisual3 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)
enemyVisual4 = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)

enemyParty = [None, enemy1, enemy2, enemy3, enemy4]

allEntities = [player1, player2, player3, player4, summon1, summon2, summon3, summon4, enemy1, enemy2, enemy3, enemy4]
allVisuals = [playerVisual1, playerVisual2, playerVisual3, playerVisual4, summonVisual1, summonVisual2, summonVisual3, summonVisual4,\
enemyVisual1, enemyVisual2, enemyVisual3, enemyVisual4]
recordingLastDamage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

statusStacksApplied = 0

bag = []
lastSwap = ["", ""]
coins = 0

abilitiesForSale = []
abilitiesForSaleCost = []

state = ""

roomNumber = 0
roomList = ["", "Combat", "Combat"]
currentLevel = LevelData(0, [])
difficulty = 0
zone = 0
deceased = ""
combatEnd = True

override = False
overrideContext = ""
overrideTarget = ""

outofJuice = False

skillCondition = "-"

cantrip = False
cantripUsed = False

infusion = True
buffDuration = ""
buffData = []
buffDataCollecting = True

combatOrder = []
combatant = ""
targetables = []

summonFaction = ""
swarm = False

animFrame = 0

async def Main():
    setPosition("Choice.exe", "0px", "0px", "center")
    generateOSScreen(CallbackShop=Shop, CallbackBag=Bag, CallbackSave=generateSaveWindow,\
    CallbackSaveUpload=SaveUpload, CallbackSaveDownload=SaveDownload)
    await MainMenu()

async def Start():
    await classgen(3)
    await Hallway()

def Narrate(text):
    Notification(text)

async def classgen(number):
    global state, classChoice

    state = "classChoosing"
    classChoice.clear()
    carrier = classes.copy()
    for i in range(number):
        hoi = carrier[random.randint(0, len(carrier)-1)]
        classChoice.append(hoi)
        carrier.remove(hoi)
    choiceResult = await choose(classChoice, "Choice.exe", "Antivirus", "Choose one for the road", False)
    addCharacter(classList[classes.index(choiceResult)].stats)
    state = ""

def addCharacter(idk):
    global partyList, partyNumber, allEntities, allVisuals, playerVisual1, playerVisual2, playerVisual3, playerVisual4
    partyNumber += 1

    player = party[partyNumber]
    player.load_from(idk)
    partyList.append(player)

    playerVisual = allVisuals[allEntities.index(player)]
    playerVisual.load_from(player)

    generateWindow(playerVisual, "player", callbackUse=useItem, callbackGetTarget=getTargetFromDiv)
    screen = document.getElementById(player.id)
    def addStatus():
        statusButton = screen.querySelector("#button2")
        statusButton.innerHTML = "i"

        if statusButton:
            def onClick(event=None):
                generateStatusWindow(next((s for s in partyList if s.id == player.id)), "player")
            
            proxyClickStatus = create_proxy(onClick)
            statusButton.addEventListener("click", proxyClickStatus)
        else:
            print("where?")
    
    setTimeout(create_proxy(addStatus), 0)

def addEnemy(idk):
    global enemyList, enemyNumber, swarm, summonFaction, allEntities, allVisuals, enemyVisual1, enemyVisual2, enemyVisual3, enemyVisual4

    enemyData = enemyStats[enemyName.index(idk)]

    enemyNumber += 1
    swarm = False
    summonFaction = "enemy"

    enemy = enemyParty[enemyNumber]
    enemy.load_from(enemyData)
    enemyList.append(enemy)

    for i in range(len(enemyList) - 1):
        if enemyList[i].id == enemy.id:
            if isinstance(enemy.id[-2], int):
                enemy.id[-2] = enemy.id[-2] + 1
            else:
                enemy.id = f"{enemy.id} (1)"

    for i in range(len(enemyData.traits)):
        traitInfo = traitList[traitName.index(enemyData.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "onSummon":
                traitEffect(enemyData, enemyData, traitInfo, j, "onSummon")
    
    if not swarm:
        enemyVisual = allVisuals[allEntities.index(enemy)]
        enemyVisual.load_from(enemy)
        generateWindow(enemyVisual, "enemy", callbackUse=useItem, callbackGetTarget=getTargetFromDiv)
        screen = document.getElementById(enemy.id)
        def addStatus():
            statusButton = screen.querySelector("#button2")
            statusButton.innerHTML = "i"

            if statusButton:
                def onClick(event=None):
                    print("hi")
                    generateStatusWindow(next((s for s in enemyList if s.id == enemy.id)), "enemy")
                
                proxyClickStatus = create_proxy(onClick)
                statusButton.addEventListener("click", proxyClickStatus)
            else:
                print("where?")
        
        setTimeout(create_proxy(addStatus), 0)
    else:
        enemyNumber -= 1
        enemyList.remove(enemy)

def addSummon(summoner, idk):
    global summonList, summonNumber, swarm, summonFaction, allEntities, allVisuals, summonVisual1, summonVisual2, summonVisual3, summonVisual4
    summonData = enemyStats[enemyName.index(idk)]

    summonNumber += 1
    swarm = False
    summonFaction = "summon"

    summon = summonParty[summonNumber]
    summon.load_from(summonData)
    summon.counter = summoner.counter
    summon.summon = True
    summonList.append(summon)
    for i in range(len(summonData.traits)):
        traitInfo = traitList[traitName.index(summonData.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "onSummon":
                traitEffect(summonData, summonData, traitInfo, j, "onSummon")
    
    if not swarm:
        summonVisual = allVisuals[allEntities.index(summon)]
        summonVisual.load_from(summon)
        generateWindow(summonVisual, "summon", callbackUse=useItem, callbackGetTarget=getTargetFromDiv)
        screen = document.getElementById(summon.id)
        def addStatus():
            statusButton = screen.querySelector("#button2")
            statusButton.innerHTML = "i"

            if statusButton:
                def onClick(event=None):
                    print("hi")
                    generateStatusWindow(next((s for s in summonList if s.id == summon.id)), "summon")
                
                proxyClickStatus = create_proxy(onClick)
                statusButton.addEventListener("click", proxyClickStatus)
            else:
                print("where?")
        
        setTimeout(create_proxy(addStatus), 0)
    else:
        summonNumber -= 1
        summonList.remove(summon)

async def Hallway():
    global state, roomNumber

    state = "Hallway"
    choiceResult = await choose(["Onward!"], "Idle.exe", "Idle.exe", "What to do, user?", False)
    if choiceResult == "Onward!":
        roomNumber += 1
        if roomList[roomNumber] == "Combat":
            await combatRoomGen()
            await startOfCombat()
            await Combat(True)

async def startOfCombat():
    global combatEnd, recordingLastDamage

    recordingLastDamage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    combatEnd = False
    for player in partyList:
        for skill in player.skills:
            skillInfo = skillList[skillName.index(skill[0])]
            if "ammo" in skillInfo.info:
                Reload(player)
    
    for i in partyList + enemyList + summonList:
        for j in i.traits:
            trait = traitList[traitName.index(j[0])]
            if trait.secondaryText == "usesPerTurn" or trait.secondaryText == "usesPerCombat":
                applyStatus(i, i, f"{trait.id}: Uses", j[1], 0, "", "", False)

async def endOfCombat():
    global bag, enemyList, summonList, player1, player2, player3, player4, enemyNumber, summonNumber, allEntities, allVisuals

    Narrate(f"The dust settles...")

    cloneParty = [None, clone1, clone2, clone3, clone4]
    party = [None, player1, player2, player3, player4]

    for i in range(len(partyList)):
        clone = cloneParty[party.index(partyList[i])]
        visual = allVisuals[allEntities.index(partyList[i])]
        placeholder = PlayerData(partyList[i].id, partyList[i].classId, partyList[i].hp, clone.maxhp, clone.juice,\
        clone.maxjuice, clone.strength, clone.defense, clone.speed, clone.counter, clone.specialStats,\
        clone.traits, clone.skills, clone.status, clone.equipment, clone.equipmentSlots, clone.attackText, partyList[i].alive)
        partyList[i].load_from(placeholder)
        visual.load_from(partyList[i])

    for i in range(len(currentLevel.enemyRoster)):
        looted = enemyList[enemyName.index(currentLevel.enemyRoster[i])]
        Loot(looted, "-")
    
    removables = enemyList + summonList
    for i in range(len(removables)):
        characterDiv = document.getElementById(removables[i].id)
        characterDiv.remove()
        removables[i] = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)

    for i in partyList:
        await upgrade(i, 3)
    
    enemyList = []
    enemyNumber = 0
    summonList = []
    summonNumber = 0
    
    await Hallway()

async def upgrade(player, number):
    global player1, player2, player3, player4

    upgradeListPlaceholder = []
    upgradeNameList = []
    upgradeChoiceList = []

    upgradeList = upgradeTable[classes.index(player.classId)][difficulty - 1]

    for i in upgradeList.table:
        for j in range(i[2]):
            upgradeListPlaceholder.append(i)
    
    for i in range(number):
        carrier = random.choice(upgradeListPlaceholder)
        upgradeChoiceList.append(carrier)
        for i in upgradeListPlaceholder.copy():
            if carrier == i:
                upgradeListPlaceholder.remove(i)
    
    for i in upgradeChoiceList:
        if i[1] == 0:
            upgradeNameList.append(f"{i[0]}")
        else:
            upgradeNameList.append(f"{i[0]} +{i[1]}")
    
    upgradeChosenName = await choose(upgradeNameList, "Upgrade", "Update Alert", f"Whatcha choosing for your {player.id}?", False)
    upgradeChosen = upgradeChoiceList[upgradeNameList.index(upgradeChosenName)]

    if upgradeChosen[0] == "STR":
        player.strength += upgradeChosen[1]
    elif upgradeChosen[0] == "SPD":
        player.speed += upgradeChosen[1]
    elif upgradeChosen[0] == "DEF":
        player.defense += upgradeChosen[1]
    elif upgradeChosen[0] == "HP":
        player.maxhp += upgradeChosen[1]
        player.hp += upgradeChosen[1]
    elif upgradeChosen[0] == "JUICE":
        player.maxjuice += upgradeChosen[1]
        player.juice += upgradeChosen[1]
    elif upgradeChosen[0] in ["ACCURACY", "HEALBONUS", "DODGE"]:
        applyStats(player, player, upgradeChosen[0].upper(), upgradeChosen[1])
    elif upgradeChosen[0] in traitName:
        applyTrait(player, player, upgradeChosen[0], 0)
    elif upgradeChosen[0] in skillName:
        player.skills.append([upgradeChosen[0], 0])

def Loot(target, type):
    global coins
    lootPool = []

    if target.summon == False:
        for i in range(len(target.lootTable)):
            if type == "-":
                if target.lootTable[i][0] == "Coins":
                    coins += target.lootTable[i][1]
                    Narrate(f"You found {target.lootTable[i][1]} coins!")
                else:
                    for j in range(target.lootTable[i][1]):
                        lootPool.append(target.lootTable[i][0])
            elif type == "coins":
                updateCoins(target)
                Narrate(f"You found {target} coins!")
            else:
                if not target.lootTable[i][0] == "Nope" or "Coins":
                    itemInfo = itemList[itemName.index(target.lootTable[i][0])]
                    if itemInfo.type == type:
                        for j in range(target.lootTable[i][1]):
                            lootPool.append(target.lootTable[i][0])
        
        lootReceived = random.choice(lootPool)

        Narrate(f"You found a {lootReceived}!")
        if not lootReceived == "Nope":
            getItem(lootReceived, 1)

def Reload(user):
    applyStatus(user, user, "AMMO", next((s for s in user.specialStats if s[0] == "MAX AMMO"), [0, 0, 0])[1], 0, "", "-", False)

def speedSort():
    global combatOrder
    for i in range(len(partyList + enemyList + summonList)):
        if (partyList + enemyList + summonList)[i].counter == 0:
            (partyList + enemyList + summonList)[i].counter += 1/(partyList + enemyList + summonList)[i].speed
    
    combatOrder = sorted(partyList + enemyList + summonList, key=lambda x: x.counter)
    combatOrder[0].counter += 1/combatOrder[0].speed
            
async def Combat(nextTurn):
    global combatOrder, currentLevel, override, cantrip, state, combatant
    state = "combat"

    await WaitForAnimFinished()

    if not combatEnd:
        if nextTurn:
            speedSort()
        combatant = combatOrder[0]
        carrier = []

        if combatant.alive:
            if nextTurn:
                await StartOfTurn(combatant)
            if not override:
                if isinstance (combatant, PlayerData):
                    choiceResult = await choose(["ATTACK", "SKILL"], "BattleControls", "BattleControls", "What to do, user?", False) 
                    if choiceResult == "ATTACK":
                        await useSkill(combatant, "player", "Attack")
                    elif choiceResult == "SKILL":
                        for i in range(len(combatant.skills)):
                            if "ammo" in skillList[skillName.index(combatant.skills[i][0])].info and any(s[0] == "AMMO" and s[1] == 0 for s in combatant.status):
                                carrier.append("Reload")
                            else:
                                carrier.append(combatant.skills[i][0])
                        choiceResult = await choose(carrier, "BattleControls", "BattleControls", "What to do, user?", False)
                        await useSkill(combatant, "player", choiceResult)
                elif isinstance (combatant, EnemyData):
                    enemyIntent(combatant)
                    if not combatant.intent == "":
                        if combatant in enemyList:
                            await useSkill(combatant, "enemy", combatant.intent)
                        elif combatant in summonList:
                            await useSkill(combatant, "summon", combatant.intent)
            else:
                override = False

                if overrideContext == "stillChanting":
                    for i in range(len(combatant.traits)):
                        traitInfo = traitList[traitName.index(combatant.traits[i][0])]
                        for i in traitInfo.info:
                            if i[0] == "onChant":
                                traitEffect(combatant, combatant, traitInfo, i, "onChant")
                    Narrate(f"{combatant.id} is still chanting!")

                else:
                    if skillCondition == "chant":
                        Narrate(f"{combatant.id} finishes chanting!")

                    if isinstance (combatant, PlayerData):
                        await useSkill(combatant, "player", overrideContext)
                    elif isinstance (combatant, EnemyData):
                        if combatant in enemyList:
                            await useSkill(combatant, "enemy", overrideContext)
                        elif combatant in summonList:
                            await useSkill(combatant, "summon", overrideContext)

        if cantrip:
            cantrip = False
            await Combat(False)
        elif outofJuice:
            await Combat(False)
        else:
            await EndOfTurn(combatant)
            await Combat(True)
    else:
        await endOfCombat()
  
async def EndOfTurn(user):
    carrier = user.status.copy()

    for i in range(len(carrier)):
        if carrier[i][0] == "DRUNK":
            applyStatus(user, user, "DRUNK",0 ,0, -1, "-", False)
    
    if isinstance (user, PlayerData):
        updateJuice(user, math.ceil(user.juice * 0.1))

async def StartOfTurn(user):
    global override, overrideContext, skillCondition, cantripUsed

    carrier = user.status.copy()
    skillCondition = "-"
    cantripUsed = False

    for i in range(len(user.traits)):
        traitInfo = traitList[traitName.index(user.traits[i][0])]
        if traitInfo.secondaryText == "usesPerTurn":
            applyStatus(user, user, f"{traitInfo.id}: Uses", user.traits[i][1], 0, "", "", False)
        for j in traitInfo.info:
            if j[0] == "startOfTurn":
                traitEffect(user, user, traitInfo, j, "startOfTurn")

    for i in range(len(carrier)):
        if carrier[i][0] == "BLEED":
            hurt(user, user, carrier[i][1], "bleed")
            if next((s for s in user.status if s[0] == "HEMOTOXIN"), [0, 0, 0])[1] > 0:
                applyStatus(user, user, "HEMOTOXIN", 0, -1, "", "-", False)
            else:
                applyStatus(user, user, "BLEED", 0, math.ceil(carrier[i][1] * -0.5), "", "-", False)
        elif carrier[i][0] == "PLAGUE":
            applyStatus(user, user, "PLAGUE", 0, 1, "", "-", False)
        elif not (carrier[i][2] == "" or "INFUSE"):
            applyStatus(user, user, carrier[i][0], 0, 0, -1, "-", False)

def traitEffect(user, target, actualTrait, actualTraitInfo, traitCondition):
    trait = copy.deepcopy(actualTrait)
    traitInfo = copy.deepcopy(actualTraitInfo)
    triggerSuccess = True
    if "triggerChance" in traitInfo:
        if random.uniform(0, 1) >= traitInfo[traitInfo.index("triggerChance") + 1]:
            triggerSuccess = True
        else:
            triggerSuccess = False
    
    if trait.secondaryText == "usesPerTurn" or trait.secondaryText == "usesPerCombat":
        if next((s for s in user.status if s[0] == f"{trait.id}: Uses"), [0, 0, 0])[1] > 0:
            applyStatus(user, user, f"{trait.id}: Uses", 0, -1, "", "", False)
            triggerSuccess = True
        else:
            triggerSuccess = False

    if triggerSuccess:
        voiceline (user, target, trait.id, trait.useText, traitCondition)

        mates = []
        notMates = []
        targets = []

        if isinstance(user, PlayerData):
            mates = partyList + summonList
            notMates = enemyList
        elif isinstance(user, EnemyData):
            if user in summonList:
                mates = partyList + summonList
                notMates = enemyList
            elif user in enemyList:
                mates = enemyList
                notMates = partyList + summonList
        
        if traitInfo[1]:
            Effect(user, user, trait.id, traitInfo, 0)
        else:
            targets = mates if traitInfo[2] else notMates
            if traitInfo[3]:
                for i in range(len(targets)):
                    Effect(user, targets[i], trait.id, traitInfo, 0)
            else:
                Effect(user, target, trait.id, traitInfo, 0)

async def useSkill(user, faction, skill):
    global targetables, outofJuice, infusion
    targetables = []

    skillInfo = skillList[skillName.index(skill)]
    outofJuice = False
    infusion = True

    if skillInfo.self: 
        if faction == "player": 
            if "infuse" in skillInfo.info:
                choiceResult = await choose(["Infuse", "Extract"], "BattleControls", "BattleControls", "So, Infuse or Extract?", False)
                if choiceResult == "Infuse":
                    infusion = True
                else:
                    infusion = False           
            if user.juice >= skillInfo.juiceCost or skillCondition == "chant" or not infusion:
                skillEffect(user, user, skillInfo, False)

            else:
                Narrate(f"Out of juice... too... tired...")
                outofJuice = True
        else:
            skillEffect(user, user, skillInfo, False)
    else:
        if faction == "player":
            if "infuse" in skillInfo.info:
                choiceResult = await choose(["Infuse", "Extract"], "BattleControls", "BattleControls", "So, Infuse or Extract?", False)
                if choiceResult == "Infuse":
                    infusion = True
                else:
                    infusion = False

            if user.juice >= skillInfo.juiceCost or skillCondition == "chant" or not infusion:
                targetablesNames = []
                if skillInfo.targets:
                    for i in range(len(partyList)):
                        targetables.append(partyList[i])
                        targetablesNames.append(partyList[i].id)
                    for i in range(len(summonList)):
                        targetables.append(summonList[i])
                        targetablesNames.append(summonList[i].id)
                else:
                    for i in range(len(enemyList)):
                        targetables.append(enemyList[i])
                        targetablesNames.append(enemyList[i].id)
                if skillInfo.AOE:
                    skillEffect(user, targetables, skillInfo, True)
                else:
                    choiceResult = await choose(targetablesNames, "BattleControls", "BattleControls", "Who to target...", False)
                    target = targetables[targetablesNames.index(choiceResult)]
                    skillEffect(user, target, skillInfo, False)
            else:
                Narrate(f"Out of juice... too... tired...")
                outofJuice = True
        elif faction == "enemy":
            if skillInfo.targets:
                targetables = enemyList
            else:
                targetables = partyList + summonList
            if skillInfo.AOE:
                skillEffect(user, targetables, skillInfo, True)
            else:
                if not next((s for s in user.status if s[0] == "TAUNT"), [0, 0, 0, 0])[1] == 0:
                    for i in (partyList + summonList + enemyList):
                        if i.id == next((s for s in user.status if s[0] == "TAUNT"), [0, 0, 0, 0])[3]:
                            targetables = [i]
                            applyStatus(user, user, "TAUNT", 0, -1, "", i.id, False)
                for i in targetables:
                    if next((s for s in i.status if s[0] == "STEALTH"), [0, 0, 0, 0])[2] > 0:
                        targetables.remove(i)
                if not len(targetables) == 0:
                    target = random.choice(targetables)
                    skillEffect(user, target, skillInfo, False)
                else:
                    Narrate("No one can be found? But that's impossible!")
        elif faction == "summon":
            if skillInfo.targets:
                targetables = partyList + summonList
            else:
                targetables = enemyList
            if skillInfo.AOE:
                skillEffect(user, targetables, skillInfo, True)
            else:
                if not next((s for s in user.status if s[0] == "TAUNT"), [0, 0, 0, 0])[1] == 0:
                    for i in (partyList + summonList + enemyList):
                        if i.id == next((s for s in user.status if s[0] == "TAUNT"), [0, 0, 0, 0])[3]:
                            targetables = [i]
                            applyStatus(user, user, "TAUNT", 0, -1, "", i.id, False)
                for i in targetables:
                    if next((s for s in i.status if s[0] == "STEALTH"), [0, 0, 0, 0])[2] > 0:
                        targetables.remove(i)
                if not len(targetables) == 0:
                    target = random.choice(targetables)
                    skillEffect(user, target, skillInfo, False)
                else:
                    Narrate("No one can be found? But that's impossible!")
    for i in targetables: 
        for j in range(len(i.traits)):
            traitInfo = traitList[traitName.index(i.traits[j][0])]
            for k in traitInfo.info:
                if k[0] == "onEnemyUseSkill" and skillInfo.targets == False:
                    traitEffect(target, user, traitInfo, k, "onEnemyUseSkill")

def skillEffect(user, target, skillInfo, AOE):
    global skillCondition, cantrip, cantripUsed, buffDuration, buffData, buffDataCollecting, animFrame

    userDiv = document.getElementById(user.id)

    buffData.clear()
    buffDataCollecting = False
    buffDuration = ""

    if isinstance(user, PlayerData):
        currentAnimName = f"{user.classId}UseSkill{skillInfo.id}"
    elif isinstance(user, EnemyData):
        currentAnimName = f"{user.id}UseSkill{skillInfo.id}"
    
    if currentAnimName in animName:
        animChart = animList[animName.index(currentAnimName)]

        for i in animChart.info:
            print(i)
            animLoad(currentAnimName, i, userDiv, animFrame)
            animFrame += 1
    else:
        currentAnimName = None

    if infusion and skillCondition != "chant" and isinstance(user, PlayerData):
        updateJuice(user, -skillInfo.juiceCost)
    
    for i in range(len(user.traits)):
        traitInfo = copy.deepcopy(traitList[traitName.index(user.traits[i][0])])
        for j in traitInfo.info:
            if [0] == "beforeSkillUse":
                if j[4] == skillInfo.id or "any":
                    traitEffect(user, target, traitInfo, j, "beforeSkillUse")

    if AOE:
        voiceline(user, user, skillInfo.id, skillInfo.useText, skillCondition)
    else:
        voiceline(user, target, skillInfo.id, skillInfo.useText, skillCondition)

    for times in range(skillInfo.multi):
        if AOE:
            for i in range(len(target)):
                dodge = next((s for s in target[i].specialStats if s[0] == "DODGE"), [0, 0, 0])[1]
                accuracy = random.uniform(0, 1) + skillInfo.acc + (next((s for s in user.specialStats if s[0] == "ACCURACY"), [0, 0, 0])[1]) - dodge
                if accuracy >= 1:
                    Effect(user, target[i], skillInfo.id, skillInfo.info, skillInfo.juiceCost, respectiveAnimName=currentAnimName)  
                else:
                    Narrate(f"{user.id} missed!")
                    for i in range(len(target.traits)):
                        traitInfo = traitList[traitName.index(target.traits[i][0])]
                        for i in traitInfo.info:
                            if i[0] == "onEnemyMiss":
                                traitEffect(user, target, traitInfo, i, "onEnemyMiss")

        else:
            dodge = next((s for s in target.specialStats if s[0] == "dodge"), [0, 0, 0])[1]
            accuracy = random.uniform(0, 1) + skillInfo.acc + (next((s for s in user.specialStats if s[0] == "ACCURACY"), [0, 0, 0])[1]) - dodge
            if accuracy >= 1:
                Effect(user, target, skillInfo.id, skillInfo.info, skillInfo.juiceCost, respectiveAnimName=currentAnimName)         
            else:
                Narrate(f"{user.id} missed!")
    
    animStart()

def voiceline(user, target, name, useText, condition):
    if infusion:
        if name == "Attack":
            voiceline = user.attackText
        else:
            voiceline = next((s for s in useText.copy() if s[0] == condition), None)[1]
        voiceline = voiceline.replace("user", user.id)
        voiceline = voiceline.replace("target", target.id)
        Narrate(f"{voiceline}")

def Effect(user, target, name, info, cost, respectiveAnimName=None):
    global skillCondition, cantrip, cantripUsed, buffDuration, buffData, buffDataCollecting, swarm
    userMates = partyList + summonList if user in partyList or summonList else enemyList
    userNotMates = enemyList if user in partyList or summonList else partyList + summonList
    targetMates = partyList + summonList if target in partyList or summonList else enemyList
    targetNotMates = enemyList if target in partyList or summonList else partyList + summonList

    for i in range(len(info)):
        if info[i] == "userToTarget":
            user = target
        if info[i] == "randomTarget":
            targetables = partyList + enemyList + summonList
            targetables.remove(user)
            target = random.choice(targetables)
        if info[i] == "damage":
            info = updateInfo(info, i, 4, target, user, name)
            if next((s for s in user.specialStats if s[0] == "VIOLET"), [0, 0])[1] > 0:
                applyStats(user, user, "VIOLET", -1)
                violet = 2
            else:
                violet = 1
            if info[i + 1] in ["fixed", "max"]:
                damage = math.ceil(info[i + 2] * (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1)
                * violet)
            else:
                penetration = next((s for s in user.specialStats if s[0] == "penetration"), [0, 0, 0])[1]
                if penetration >= 1:
                    penetration = 1

                if info[i + 1] == "str":
                    damage = user.strength
                elif info[i + 1] == "spd":
                    damage = user.speed
                elif info[i + 1] == "def":
                    damage = user.defense
                elif info[i + 1] == "FAITH":
                    damage = next((s for s in user.status if s[0] == "FAITH"), [0, 0, 0, 0])[1]

                damage = damage * info[i + 2] *\
                (1 + random.uniform(-info[i + 3], info[i + 3])) *\
                (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1) * violet -\
                target.defense * (1 - penetration)

            if damage <= 0:
                damage = 1
            damage = math.ceil(damage)
            hurt(user, target, damage, "damage", respectiveAnimName=respectiveAnimName)
            if info[i + 1] == "max":
                target.maxhp -= damage

            for i in range(len(user.traits)):
                traitInfo = traitList[traitName.index(user.traits[i][0])]
                for j in traitInfo.info:
                    if j[0] == "onDamage":
                        traitEffect(user, target, traitInfo, j, "onDamage")

            if next((s for s in target.status if s[0] == "BLEED"), [0, 0, 0])[1] > 0:
                applyStatus(user, target, "BLEED", 0, math.ceil(damage * 0.1) + next((s for s in user.specialStats if s[0] == "BLEEDBONUS"), [0, 0, 0])[1], "", "-", False)
            if next((s for s in target.status if s[0] == "FAITH"), [0, 0, 0])[1] > 0:
                applyStatus(user, target, "FAITH", 0, -math.ceil(damage * 0.25), "", "-", False)

            thorns = next((s for s in target.specialStats if s[0] == "thorns"), [0, 0, 0])[1]
            if thorns > 0:
                hurt(target, user, thorns)

            if next((s for s in target.status if s[0] == "COUNTER"), [0, 0, 0])[1] > 0:
                applyStatus(target, target, "COUNTER", 0, -1, "", "", False)
                skillCondition = "-"
                skillEffect(target, user, skillList[skillName.index("Counter")], False)
        if info[i] == "selfDamage":
            info = updateInfo(info, i, 4, target, user, name)
            if next((s for s in user.specialStats if s[0] == "VIOLET"), [0, 0])[1] > 0:
                applyStats(user, user, "VIOLET", -1)
                violet = 2
            else:
                violet = 1
            if info[i + 1] in ["fixed", "max"]:
                damage = math.ceil(info[i + 2] * (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1)
                * violet)
            else:
                penetration = next((s for s in user.specialStats if s[0] == "penetration"), [0, 0, 0])[1]
                if penetration >= 1:
                    penetration = 1

                if info[i + 1] == "str":
                    damage = user.strength
                elif info[i + 1] == "spd":
                    damage = user.speed
                elif info[i + 1] == "def":
                    damage = user.defense
                elif info[i + 1] == "faith":
                    damage = next((s for s in user.status if s[0] == "FAITH"), [0, 0, 0, 0])[1]

                damage = damage * info[i + 2] *\
                (1 + random.uniform(-info[i + 3], info[i + 3])) *\
                (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1) * violet -\
                user.defense * (1 - penetration)

            if damage <= 0:
                damage = 1
            damage = math.ceil(damage)
            hurt(user, user, damage, "selfDamage", respectiveAnimName=respectiveAnimName)
            if info[i + 1] == "max":
                user.maxhp -= damage

            if next((s for s in user.status if s[0] == "BLEED"), [0, 0, 0])[1] > 0:
                applyStatus(user, user, "BLEED", 0, math.ceil(damage * 0.1) + next((s for s in user.specialStats if s[0] == "BLEEDBONUS"), [0, 0, 0])[1], "", "-", False)
            if next((s for s in user.status if s[0] == "FAITH"), [0, 0, 0])[1] > 0:
                applyStatus(user, user, "FAITH", 0, -math.ceil(damage * 0.25), "", "-", False)
        if info[i] == "heal":
            info = updateInfo(info, i, 3, target, user, name)
            healBonus = next((s for s in user.specialStats if s[0] == "HEALBONUS"), [0, 0, 0])[1]
            if info[i + 2] == "max":
                target.maxhp += info[i + 1] + healBonus
            heal(user, target, info[i + 1] + healBonus)
        if info[i] == "die":
            hurt(user, user, user.hp, "die", respectiveAnimName=respectiveAnimName)
        if info[i] == "ammo":
            info = updateInfo(info, i, 2, target, user, name)
            applyStatus(user, user, "AMMO", 0, info[i + 1], "", "-", False)
        if info[i] == "reload":
            Reload(user)
        if info[i] == "chant":
            info = updateInfo(info, i, 2, target, user, name)
            if skillCondition != "chant":
                for i in range(len(user.traits)):
                    traitInfo = traitList[traitName.index(user.traits[i][0])]
                    for j in traitInfo.info:
                        if j[0] == "onChant":
                            traitEffect(user, user, traitInfo, j, "onChant")
                applyStatus(user, user, "CHANT", 0, 0, info[i + 1], name, False)
                break
            else:
                skillCondition = "-"
        if info[i] == "summon":
            addSummon(user, info[i + 1])
        if info[i] == "drunk":
            info = updateInfo(info, i, 4, target, user, name)
            if random.uniform(0, 1) + info[i + 1] >= 1:
                applyStatus(user, target, "DRUNK", info[i + 2], info[i + 3], info[i + 4], "-", False)
        if info[i] == "bleed":
            info = updateInfo(info, i, 3, target, user, name)
            if random.uniform(0, 1) + info[i + 1] >= 1:
                applyStatus(user, target, "BLEED", 0, info[i + 2] + next((s for s in user.specialStats if s[0] == "BLEEDBONUS"), [0, 0, 0])[1], "", "-", False)
        if info[i] == "hemotoxin":
            info = updateInfo(info, i, 3, target, user, name)
            if random.uniform(0, 1) + info[i + 1] >= 1:
                applyStatus(user, target, "HEMOTOXIN", 0, info[i + 2], "", "-", False)
        if info[i] == "plague":
            info = updateInfo(info, i, 3, target, user, name)
            if random.uniform(0, 1) + info[i + 1] >= 1:
                applyStatus(user, target, "PLAGUE", 0, info[i + 2], "", "-", False)
        if info[i] == "taunt":
            info = updateInfo(info, i, 3, target, user, name)
            if random.uniform(0, 1) + info[i + 1] >= 1:
                applyStatus(user, target, "TAUNT", 0, info[i + 2], "", user.id, False)
        if info[i] == "stealth":
            info = updateInfo(info, i, 2, target, user, name)
            applyStatus(user, target, "STEALTH", 1, 0, info[i + 1], user.id, False)
        if info[i] == "pray":
            info = updateInfo(info, i, 2, target, user, name)
            for j in (userMates + userNotMates):
                for k in j.traits:
                    traitInfo = traitList[traitName.index(k[0])]
                    for l in traitInfo.info:
                        if l[0] == "conduit":
                            print(info[i + 1])
                            applyStatus(user, j, "FAITH", 0, info[i + 1], "", user.id, False)
        if info[i] == "cantrip":
            if cantripUsed == False:
                cantrip = True
                cantripUsed = True
        if info[i] == "buffDuration":
            info = updateInfo(info, i, 2, target, user, name)
            buffDuration = info[i + 1]
        if info[i] == "infuse":
            buffDuration = "infuse"
            if isinstance (user, PlayerData):
                if infusion:
                    user.maxjuice -= cost
                else:
                    if next((s for s in target.status if s[0] == name), [0, 0, 0, 0])[1] > 0:
                        user.maxjuice += next((s for s in target.status if s[0] == name), [0, 0, 0, 0])[1] * cost
                        user.juice += next((s for s in target.status if s[0] == name), [0, 0, 0, 0])[1] * cost
                        Narrate(f"Extraction complete.")
                    else:
                        Narrate(f"Nothing was extracted.")
                updateJuice(user, 0)
        if info[i] == "buff":
            info = updateInfo(info, i, info.index("buffEnd") - i + 1, target, user, name)
            buffDataCollecting = True
        if info[i] == "buffEnd":
            buffDataCollecting = False
            if infusion:
                Buff(user, target, name, buffData, 1, True)
            else:
                if next((s for s in target.status if s[0] == name), [0, 0, 0])[1] > 0:
                    Buff(user, target, name, buffData, -next((s for s in target.status if s[0] == name), [0, 0, 0])[1], True)
        if info[i] == "counter":
            info = updateInfo(info, i, 2, target, user, name)
            applyStatus(user, user, "COUNTER", 0, info[i + 1], "", "-", False)
        if info[i] == "undying":
            info = updateInfo(info, i, 2, target, user, name)
            applyStatus(user, user, "UNDYING", 0, info[i + 1], "", "-", False)
        if info[i] == "faith":
            info = updateInfo(info, i, 2, target, user, name)
            if info[i + 1] == "loseAll":
                applyStatus(user, user, "FAITH", 0, -next((s for s in user.status if s[0] == "FAITH"), [0, 0, 0, 0])[1], "", "-", False)
            else:
                applyStatus(user, user, "FAITH", 0, info[i + 1], "", "-", False)
        if info[i] == "loot":
            info = updateInfo(info, i, 3, target, user, name)
            if info[i + 1] == "coins":
                Loot(info[i + 2], "coins")
            elif info[i + 1] in itemName:
                getItem(info[i + 1], info[i + 2])
            else: 
                for j in range(info[i + 2]):
                    Loot(deceased, info[i + 1])
        if info[i] == "swarm":
            if summonFaction == "summon":
                if sum(1 for s in summonList if s.id == user.id) > 1:
                    swarm = True
                victim = next((s for s in summonList if s.id == user.id), None)
                bodies = info[i + 1]
            elif summonFaction == "enemy":
                if sum(1 for s in enemyList if s.id == user.id) > 1:
                    swarm = True
                victim = next((s for s in enemyList if s.id == user.id), None)
                bodies = info[i + 1]
            if next((s for s in victim.status if s[0] == "SWARM"), [0, 0, 0, 0])[1] == 0:
                modifier = -1
            else:
                modifier = 0
            victim.maxhp += user.maxhp * (bodies + modifier)
            victim.hp += user.hp * (bodies + modifier)
            victim.strength += user.strength * (bodies + modifier)
            applyStatus(user, victim, "SWARM", 0, bodies, "", "-", False)
        if info[i] == "cleanse":
            info = updateInfo(info, i, 2, target, user, name)
            cleansables = []
            for i in ["DRUNK", "BLEED", "PLAGUE", "HEMOTOXIN"]:
                if next((s for s in target.status if s[0] == i), [0, 0, 0, 0])[1] > 0:
                    cleansables.append(next((s for s in target.status if s[0] == i), [0, 0, 0, 0])[0])
            print(cleansables)
            if len(cleansables) > 0:
                applyStatus(user, target, random.choice(cleansables), 0, -info[i + 1], "-", False)
        if info[i] == "useSkill":
            info = updateInfo(info, i, 2, target, user, name)
            if isinstance(info[i + 1], int):
                idk = user.skills[info[i + 1]][0]
            else:
                idk = info[i + 1]
            mates = partyList + summonList if isinstance (user, PlayerData) else enemyList
            notMates = enemyList if isinstance (user, PlayerData) else partyList + summonList
            skillInfo = skillList[skillName.index(idk)]
            targets = mates if skillInfo.targets else notMates
            if skillInfo.AOE:
                targets = mates if skillInfo.targets else notMates
                skillEffect(user, targets, skillInfo, True)
            elif target not in targets:
                target = random.choice(targets)
                skillEffect(user, target, skillInfo, False)
        if info[i] == "triggerGain":
            info = updateInfo(info, i, 2, target, user, name)
            for j in user.traits:
                trait = traitList[traitName.index(j[0])]
                if j[0] == name:
                    j[1] += info[i + 1]
                    for k in trait.info:
                        if k[0] == "onTrigger":
                            if not k[4] == "":
                                if j[1] >= k[4]:
                                    j[1] -= k[4]
                                    traitEffect(user, target, trait, k, "onTrigger")
        if info[i] == "checkStacks":
            info = updateInfo(info, i, 4, target, user, name)
            currentStacks = next((s for s in target.status if s[0] == info[i + 1]), [0, 0, 0, 0])[1]
            targetStacks = info[i + 3]
            if info[i + 2] == "reach":
                if currentStacks < targetStacks:
                    break
            if info[i + 2] == "under":
                if currentStacks >= targetStacks:
                    break
        if info[i] == "trigger":
            for j in user.traits:
                trait = traitList[traitName.index(j[0])]
                if j[0] == name:
                    for k in trait.info:
                        if k[0] == "onTrigger":
                            traitEffect(user, target, trait, k, "onTrigger")

        if buffDataCollecting:
            buffData.append(info[i])
        
        if info[i] in ["damage", "bleed"]:
            animSeekAndDestroy(respectiveAnimName, info[i])

def updateInfo(info, startingNumber, total, target, user, name):
    for i in range(total):
        if isinstance(info[startingNumber + i], list):
            carrier = 0
            for j in range(len(info[startingNumber + i])):
                if info[startingNumber + i][j] == "lastDamage":
                    if info[startingNumber + i][j + 1] == "target":
                        info[startingNumber + i][j] = recordingLastDamage[allEntities.index(target)] 
                    elif info[startingNumber + i][j + 1] == "user":
                        info[startingNumber + i][j] = recordingLastDamage[allEntities.index(user)]
                if info[startingNumber + i][j] == "statusStacksApplied":
                    info[startingNumber + i][j] = statusStacksApplied
                if info[startingNumber + i][j] == "secondaryNumber":
                    info[startingNumber + i][j] = next((s for s in user.skills + user.traits if s[0] == name), [0, 0])[1]
                if (isinstance(info[startingNumber + i][j], int) or isinstance(info[startingNumber + i][j], float)): 
                    carrier += info[startingNumber + i][j]
                else:
                    carrier += 0
            info[startingNumber + i] = math.ceil(carrier)
    return info

def Buff(user, target, buffName, buffData, buffStacks, buffStatus):
    global buffDuration

    for i in range(len(buffData)):
        if buffData[i] == "str":
            target.strength += buffData[buffData.index("str") + 1] * buffStacks
            if target.strength <= 0:
                target.strength = 1
        if buffData[i] == "spd":
            target.speed += buffData[buffData.index("spd") + 1] * buffStacks
            if target.speed <= 0:
                target.speed = 1
        if buffData[i] == "def":
            target.defense += buffData[buffData.index("def") + 1] * buffStacks
            if target.defense <= 0:
                target.defense = 1
        if buffData[i] in ["penetration", "thorns", "damageUp", "accuracy", "dodge", "healBonus", "bleedBonus",\
        "crimson", "cobalt", "violet"]:
            applyStats(user, target, buffData[i].upper(), buffData[i + 1] * buffStacks)
        if buffData[i] == "trait":
            applyTrait(user, target, buffData[buffData.index("trait") + 1], buffData[buffData.index("trait") + 2] * buffStacks)

    if buffStatus:
        if buffDuration == "infuse":
            applyStatus(user, target, buffName, 0, buffStacks, "INFUSE", user.id, False)
        elif not buffDuration == "":
            applyStatus(user, target, buffName, 0, buffStacks, buffDuration, user.id, False)

def applyStatus(user, target, status, stacks, stacksChange, duration, text, replaceOriginal):
    global override, overrideContext, skillCondition, buffDataCollecting, statusStacksApplied

    carrier = False
    hitList = []
    unhitList = ["AMMO"]
    
    for i in range(len(target.status)):
        if target.status[i][0] == status:
            statusStacksApplied = stacksChange
            target.status[i][1] += stacksChange
            if target.status[i][1] <= stacks:
                statusStacksApplied = stacks
                target.status[i][1] = stacks
            if not target.status[i][2] == "" or "INFUSE":
                target.status[i][2] += duration
            if target.status[i][1] <= 0 or (isinstance(target.status[i][2], int) and target.status[i][2] <= 0):
                hitList.append(target.status[i][0])
            carrier = True

    if not carrier:
        statusStacksApplied = stacks + stacksChange
        target.status.append([status, stacks + stacksChange, duration, text])
    
    if replaceOriginal:
        next((s for s in target.status if s[0] == "CHANT"), [0, 0, 0, 0])[3] = text

    if status == "CHANT" and duration < 0:
        override = True
        overrideContext = "stillChanting"
        skillCondition = "chant"
    
    if status == "PLAGUE" and next((s for s in target.status if s[0] == "PLAGUE"), None)[1] >= target.hp * 5:
        hurt(target, target, (next((s for s in target.status if s[0] == "PLAGUE"), None)[1]) * 5, "plague")
        applyStatus(user, target, "PLAGUE", 0, -(next((s for s in target.status if s[0] == "PLAGUE"), None)[1]), "", "-", False)

    for i in range(len(hitList)):
        if hitList[i] == "CHANT":
            override = True
            overrideContext = next((s for s in target.status if s[0] == "CHANT"), None)[3]
            skillCondition = "chant"

        if hitList[i] == "DRUNK":
            applyStats(user, target, "DAMAGEUP", 0.25 * next((s for s in target.status if s[0] == "CHANT"), None)[1])
            applyStats(user, target, "ACCURACY", -0.25 * next((s for s in target.status if s[0] == "CHANT"), None)[1])
        
        if hitList[i] in skillName + traitName + itemName:
            buffData = []
            buffDataCollecting = True
            skill = next((s for s in (skillList + traitList + itemList) if s.id == hitList[i]), None)
            if skill:
                buffer = (next((s for s in (partyList + enemyList + summonList) if s.id == next((s for s in target.status if s[0] == hitList[i]), [0, 0, 0, 0])[3]), None))
                info = skill.info
                if not next((s for s in target.status if s[0] == hitList[i]), [0, 0, 0, 0])[2] == "INFUSE":
                    for j in range(len(info)):
                        if info[j] == "buff":
                            buffDataCollecting = True
                        if info[j] == "buffEnd":
                            buffDataCollecting = False
                            Buff(buffer, target, hitList[i], buffData, -next((s for s in target.status if s[0] == hitList[i]), [0, 0, 0, 0])[1], False)
                        if buffDataCollecting:
                            buffData.append(info[j])
        
        if hitList[i] not in unhitList:
            target.status.remove(next((s for s in target.status if s[0] == hitList[i]), None))

    if status == "DRUNK" :
        applyStats(user, target, "DAMAGEUP", 0.25 * stacksChange)
        applyStats(user, target, "ACCURACY", -0.25 * stacksChange)
    
    for i in range(len(user.traits)):
        traitInfo = traitList[traitName.index(user.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "onApplyStatus":
                if j[4] == status.upper():
                    traitEffect(user, target, traitInfo, j, "onApplyStatus")
    
    for i in range(len(target.traits)):
        traitInfo = traitList[traitName.index(target.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "onGainStatus":
                if j[4] == status.upper():
                    traitEffect(target, user, traitInfo, j, "onGainStatus")

def applyStats(user, target, stat, val):
    carrier = False
    hitList = []
    unhitList = []
    
    for i in range(len(target.specialStats)):
        if target.specialStats[i][0] == stat:
            target.specialStats[i][1] += val
            if target.specialStats[i][1] <= 0:
                hitList.append(target.specialStats[i][0])
            carrier = True

    if not carrier:
        target.specialStats.append([stat, val])

    if next((s for s in target.specialStats if s[0] == "CRIMSON"), [0, 0])[1] > 0 and next((s for s in target.specialStats if s[0] == "COBALT"), [0, 0])[1] > 0:
        idk = min(next((s for s in target.specialStats if s[0] == "CRIMSON"), [0, 0])[1], next((s for s in target.specialStats if s[0] == "COBALT"), [0, 0])[1])
        next((s for s in target.specialStats if s[0] == "CRIMSON"), [0, 0])[1] -= idk
        next((s for s in target.specialStats if s[0] == "COBALT"), [0, 0])[1] -= idk
        applyStats(target, target, "VIOLET", idk)

    for i in range(len(hitList)):    
        if hitList[i] not in unhitList:
            target.specialStats.remove(next((s for s in target.specialStats if s[0] == hitList[i]), None))

def applyTrait(user, target, trait, val):
    carrier = False
    
    for i in range(len(target.traits)):
        if target.traits[i][0] == trait:
            target.traits[i][1] += val
            carrier = True

    if not carrier:
        if val == 0:
            val = traitList[traitName.index(trait)].secondaryText
        target.traits.append([trait, val])

def hurt(user, target, damage, cause, respectiveAnimName=None):
    global recordingLastDamage, allEntities, allVisuals

    userMates = partyList + summonList if user in partyList or summonList else enemyList
    userNotMates = enemyList if user in partyList or summonList else partyList + summonList
    targetMates = partyList + summonList if target in partyList or summonList else enemyList
    targetNotMates = enemyList if target in partyList or summonList else partyList + summonList

    userVisual = allVisuals[allEntities.index(user)]
    targetVisual = allVisuals[allEntities.index(target)]
    userDiv = document.getElementById(userVisual.id)
    targetDiv = document.getElementById(targetVisual.id)

    hoi = False
    for i in range(len(target.traits)):
        traitInfo = traitList[traitName.index(target.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "invulnerable":
                hoi = True
    if not hoi:
        target.hp -= damage
        if respectiveAnimName:
            locatedFrame = animlocateFrame(respectiveAnimName, cause)
            animAdd(updateHp(targetVisual, -damage), locatedFrame, False)
            if cause in ["damage", "selfDamage", "bleed"]:
                animAdd(effectNumber(damage, targetDiv, "red", 1000), locatedFrame, False)
            elif cause in ["plague"]:
                animAdd(effectNumber(damage, targetDiv, "green", 1000), locatedFrame, False)
            elif cause in ["die"]:
                animAdd(effectNumber(damage, targetDiv, "black", 1000), locatedFrame, False)
        allEntities = [player1, player2, player3, player4, summon1, summon2, summon3, summon4, enemy1, enemy2, enemy3, enemy4]
        recordingLastDamage[allEntities.index(target)] = damage
        carrier = next((s for s in target.status if s[0] == "SWARM"), [0, 0, 0, 0])[1]
        for i in range(len(target.traits)):
            traitInfo = traitList[traitName.index(target.traits[i][0])]
            for j in traitInfo.info:
                if j[0] == "onHurt":
                    traitEffect(target, user, traitInfo, j, "onHurt")
        for i in targetMates: 
            for j in range(len(i.traits)):
                traitInfo = traitList[traitName.index(i.traits[j][0])]
                for k in traitInfo.info:
                    if k[0] == "onAllyHurt":
                        traitEffect(i, target, traitInfo, k, "onAllyHurt")
        if carrier > 1:
            if target.hp / target.maxhp <= carrier-1 / carrier:
                difference = math.floor((target.maxhp - target.hp) / (target.maxhp / carrier))
                target.maxhp -= math.floor(target.maxhp / carrier * difference)
                target.strength -= math.floor(target.strength / carrier * difference)
                applyStatus(user, target, "SWARM", 0, -difference, "", "-", False)
    
    deathCheck(user)

def heal(user, target, heal):
    hoi = False
    for i in range(len(target.traits)):
        traitInfo = traitList[traitName.index(target.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "invulnerable":
                hoi = True
    if not hoi:
        target.hp += heal
        if target.hp > target.maxhp:
            target.hp = target.maxhp

def updateCoins(amount):
    coins += amount
    coinDiv = document.getElementById(coins)
    coinDiv.innerHTML = f"COINS: {coins}"

def UpdateBagAdd(item, number):
    screen = document.getElementById("BagWindow")
    grid = document.getElementById("BagGrid")

    if screen:
        itemInfo = itemList[itemName.index(item)]
        item = document.createElement("div")
        item.className = "itemIcon"
        # Sanitize ID to avoid spaces
        item.id = f"{itemInfo.id.replace(' ', '-')}"
            
        placeholder = document.createElement("div")
        placeholder.id = f"{itemInfo.id.replace(' ', '-')}-desc"
        placeholder.className = "descriptionWindow"
        screen.appendChild(placeholder)

        placeholderWindow = document.createElement("div")
        placeholderWindow.className = "windowBody"
        placeholder.appendChild(placeholderWindow)
            
        addText(placeholderWindow, f"desc-text-{itemInfo.id.replace(' ', '-')}", f"{item} x{number}")
        addDescriptionToImage(item, itemInfo.id, itemInfo.image, placeholderWindow)
        makeIconDraggable(item, grid, "Bag", UpdateBagSwap)
        grid.appendChild(item)

def UpdateBagSwap(old, new):
    global bag, lastSwap
    if not old == lastSwap[0] and not new == lastSwap[1]:
        lastSwap = [old, new]
        old = next((s for s in bag if s[0] == old), None)
        new = next((s for s in bag if s[0] == new), None)
        oldPos = bag.index(old)
        newPos = bag.index(new)
        bag[oldPos] = new
        bag[newPos] = old

def deathCheck(killer):
    global combatEnd, deceased
    hoi = False

    existingEntities = partyList + enemyList + summonList
    for i in range(len(existingEntities)):
        for j in range(len(existingEntities[i].traits)):
            traitInfo = traitList[traitName.index(existingEntities[i].traits[j][0])]
            for k in traitInfo.info:
                if k[0] == "invulnerable":
                    hoi = True
        if not hoi:           
            if existingEntities[i].hp <= 0:
                if existingEntities[i].alive:
                    deceased = existingEntities[i]
                    deceased.alive = False
                    Narrate(f"{deceased.id} dies!")

                    if deceased in enemyList:
                        carrier = partyList + summonList
                    elif deceased in partyList or summonList:
                        carrier = enemyList
                            
                    for j in range(len(carrier)):
                        for k in range(len(carrier[j].traits)):
                            traitInfo = traitList[traitName.index(carrier[j].traits[k][0])]
                            for l in traitInfo.info:
                                if l[0] == "onEnemyDeath":
                                    traitEffect(carrier[i], deceased, traitInfo, l, "onEnemyDeath")
                    
                    if next((s for s in deceased.status if s[0] == "UNDYING"), [0, 0, 0, 0])[1] > 0:
                        deceased.hp = 1
                        deceased.alive = True
                        deceased.summon = True
                        applyStatus(deceased, deceased, "UNDYING", 0, -1, "", "", False)
                        Narrate(f"{deceased.id} rises from the dead!")
        hoi = False
    
    carrier = partyList + summonList
    alive = 0   
    for i in range(len(carrier)):
        for j in range(len(carrier[i].traits)):
            traitInfo = traitList[traitName.index(carrier[i].traits[j][0])]
            for k in traitInfo.info:
                if k[0] == "invulnerable":
                    hoi = True
        if carrier[i].alive == True and hoi == False:
            alive += 1
    if alive == 0:
        combatEnd = True
    
    carrier = enemyList
    alive = 0   
    for i in range(len(carrier)):
        for j in range(len(carrier[i].traits)):
            traitInfo = traitList[traitName.index(carrier[i].traits[j][0])]
            for k in traitInfo.info:
                if k[0] == "invulnerable":
                    hoi = True
        if carrier[i].alive == True and hoi == False:
            alive += 1
    if alive == 0:
        combatEnd = True

def enemyIntent(idk):
    chart = idk.intentChart
    decided = False
    if "none" in chart:
        decided = True
        intent = ""
    if "notSummon" in chart:
        if idk.summon == False:
            print("notSummon")
            intent = idk.skills[random.choice(chart[chart.index("notSummon") + 1])][0]
            decided = True
    if "hpBelow" in chart:
        if idk.hp <= idk.maxhp * chart[chart.index("hpBelow") + 1]:
            intent = idk.skills[random.choice(chart[chart.index("hpBelow") + 2])][0]
            decided = True
    if decided == False:
        intent = idk.skills[random.choice(chart[chart.index("default") + 1])][0]
                 
    idk.intent = intent    
            
async def combatRoomGen():
    global partyNumber, enemyNumber, enemyList, currentLevel, clone1, clone2, clone3, clone4, difficulty
    clone1 = copy.deepcopy(player1)
    clone2 = copy.deepcopy(player2)
    clone3 = copy.deepcopy(player3)
    clone4 = copy.deepcopy(player4)

    if zone == 0:
        currentLevel = combatZone0[random.randint(0, len(combatZone0) - 1)]
    if zone == 1:
        currentLevel = combatZone1[random.randint(0, len(combatZone1) - 1)]

    enemyNumber = 0
    enemyList = []

    carrier = [enemy1, enemy2, enemy3, enemy4]
    for i in range(len(carrier)):
       carrier[i] = EnemyData("", 0, 0, 0, 0, 0, 0, [], [], [], [], [], [], [], [], "", True, False)

    difficulty = currentLevel.difficulty

    for i in range(len(currentLevel.enemyRoster)):
        addEnemy(currentLevel.enemyRoster[i])

def Bag():
    print("hi")
    generateBagWindow(bag, coins, callbackSwap=UpdateBagSwap)

def getItem(item, number):
    global bag

    hitList = []
    carrier = False
    
    for i in range(len(bag)):
        if bag[i][0] == item:
            bag[i][1] += number
            if bag[i][1] == 0:
                hitList.append(bag[i][0])
            carrier = True

    if not carrier:
        bag.append([item, number])
        UpdateBagAdd(item, number)

    for i in range(len(hitList)):
        bag.remove(next((s for s in bag if s[0] == hitList[i]), None))

def useItem(item, target): 
    global allEntities, allVisuals 
    target = allEntities[allVisuals.index(target)]
    itemInfo = copy.deepcopy(itemList[itemName.index(item)])
    mates = partyList + summonList
    notMates = enemyList
    targets = []
    used = False

    if itemInfo.type == "potion":
        targets = mates if itemInfo.targets else notMates

        if not (state == "combat" or itemInfo.self or itemInfo.targets):
            Narrate(f"You wouldn't wanna use it on yourself.")
            return

        if itemInfo.self:
            voiceline(target, target, itemInfo.id, [["-", itemInfo.useText]], "-")
            Effect(target, target, itemInfo.id, itemInfo.info, 0)
        else:
            if itemInfo.AOE:
                voiceline(target, targets[0], itemInfo.id, [["-", itemInfo.useText]], "-")
                for i in targets:
                    Effect(target, i, itemInfo.id, itemInfo.info, 0)
            else:
                voiceline(target, target, itemInfo.id, [["-", itemInfo.useText]], "-")
                Effect(target, target, itemInfo.id, itemInfo.info, 0)

        used = True
    if itemInfo.type == "weapon" or "relic":
        equipSuccess = equip(item, target)
        if equipSuccess:
            voiceline(target, target, itemInfo.id, [["-", itemInfo.useText]], "-")
            used = True
        else:
            Narrate(f"Sorry, pockets/appendages full.")
            used = False
    else:
        Narrate(f"How would you even do that?")
        used = False

    if used:
        getItem(item, -1)

    print(item)

def equip(item, target):
    itemInfo = itemList[itemName.index(item)]
    equipSuccess = False
    if len(target.equipment) >= target.equipmentSlots:
        equipSuccess = False
    else:
        target.equipment.append(item)
        Buff(target, target, item, itemInfo.info, 1, False)
        equipSuccess = True
    
    return equipSuccess

def getTargetFromDiv(div):
    return(next((s for s in (partyList + enemyList + summonList) if s.id == div.id), None))
            
async def MainMenu():
    choiceResult = await choose(["New Game", "Load Save"], "Choice.exe", "Choice.exe", "", False)
    
    if choiceResult == "New Game":
        await Start()
    elif choiceResult == "Load Save": 
        generateSaveWindow(CallbackSaveUpload=SaveUpload, CallbackSaveDownload=SaveDownload)
        await Hallway()

def SaveUpload():
    def handle_file(event):
        file = event.target.files.item(0)
        reader = FileReader.new() # type: ignore

        def onload(e):
            global bag, coins
            text = e.target.result
            save_data = json.loads(text)
            print("Loaded save file:", save_data)

            idk = [player1, player2, player3, player4]

            for i in range(len(idk)):
                carrier = save_data["party"][i]
                idk[i] = PlayerData(carrier["id"], carrier["classId"], carrier["hp"], carrier["maxhp"], carrier["juice"],\
                        carrier["maxjuice"], carrier["strength"], carrier["defense"], carrier["speed"], carrier["counter"],\
                        carrier["specialStats"], carrier["traits"], carrier["skills"], carrier["status"], carrier["equipment"], carrier["equipmentSlots"],\
                        carrier["attackText"], carrier["alive"])
                if idk[i].alive:
                    addCharacter(idk[i])
            bag = save_data["bag"]
            coins = save_data["coins"]
            
        reader.onload = create_proxy(onload)
        reader.readAsText(file)

    upload_input = document.getElementById("upload")
    upload_input.addEventListener("change", create_proxy(handle_file))

def SaveDownload():
    def download_save_file(*args):
        save_data = {
            "party": [asdict(p) for p in [player1, player2, player3, player4]],
            "level": roomNumber,
            "bag": bag,
            "coins": coins
        }

        json_str = json.dumps(save_data, indent=4)

        blob = Blob.new([json_str], { "type": "application/json" })
        url = URL.createObjectURL(blob)

        link = document.createElement("a")
        link.href = url
        link.download = "save.json"
        link.click()
        proxyDownload.destroy()
    
    proxyDownload = create_proxy(download_save_file)

    document.getElementById("download").addEventListener("click", proxyDownload)

def RestockShop():
    global abilitiesForSale, abilitiesForSaleCost

    classes = ["Pirate", "Dissector", "Qi Master", "Raven", "Shaman", "Bard"]
    partyClasses = []
    skills = [pirateSkillList, dissectorSkillList, qiMasterSkillList, ravenSkillList, shamanSkillList, bardSkillList]
    traits = [pirateTraitList, dissectorTraitList, qiMasterTraitList, ravenTraitList, shamanTraitList, bardTraitList]
    unusableStock = []

    abilitiesForSale = []
    abilitiesForSaleCost = []

    for i in range(4):
        if i < len(partyList):
            partyClasses.append(partyList[i].classId)
        else:
            partyClasses.append(random.choice(partyClasses))
    
    for i in partyClasses:
        unusableStock = []
        stock = skills[classes.index(i)] + traits[classes.index(i)]
        for j in partyList:
            for k in j.traits + j.skills:
                unusableStock.append(k[0])
        for j in stock:
            if j in unusableStock:
                stock.remove(j) 
        chosenItem = random.choice(stock)
        abilitiesForSale.append(chosenItem)
        abilitiesForSaleCost.append(math.ceil(chosenItem.price * random.uniform(0.8, 1.2)))
    
    return [abilitiesForSale]

def Shop():
    generateShopWindow([abilitiesForSale], CallbackBuy=Buy, CallbackRestock=RestockShop)

def Buy(item, itemDiv, vendor):
    global coins, bag

    vendorDiv = document.getElementById(vendor)

    classes = ["Pirate", "Dissector", "Qi Master", "Raven", "Shaman", "Bard"]
    partyClasses = []
    skills = [pirateSkillList, dissectorSkillList, qiMasterSkillList, ravenSkillList, shamanSkillList, bardSkillList]
    traits = [pirateTraitList, dissectorTraitList, qiMasterTraitList, ravenTraitList, shamanTraitList, bardTraitList]

    if vendor == "abilityVendor":
        itemInfo = next((s for s in (abilitiesForSale) if s.id == item), None)
        itemCost = abilitiesForSaleCost[abilitiesForSale.index(itemInfo)]
    if itemCost > coins:
        print("Damn. Poverty is a huge pain, eh?")
    else:
        coins -= itemCost
        if isinstance(itemInfo, SkillData):
            for i in skills:
                if itemInfo in i:
                    target = classes[skills.index(i)]
                print(target)
            for i in partyList:
                if i.classId == target:
                    i.skills.append([item, 0])
                    cloneParty[party.index(i)].skills.append([item, 0])
        if isinstance(itemInfo, TraitData):
            for i in traits:
                if itemInfo in i:
                    target = classes[traits.index(i)]
            for i in partyList:
                if i.classId == target:
                    applyTrait(i, i, item, 0)
                    applyTrait(cloneParty[party.index(i)], cloneParty[party.index(i)], item, 0)
        if isinstance(itemInfo, ItemData):
            print("hi")
        itemDiv.remove()

asyncio.ensure_future(Main())