from keywords import keywordName, keywordList
from skills import skillName, skillList
from traits import traitName, traitList
from item import itemName, itemList

from html import escape
from js import document, requestAnimationFrame, window, setTimeout, setInterval, clearInterval
import random, asyncio, re, math, copy, threading
from pyodide.ffi import create_proxy  # type: ignore
from pyodide.http import pyfetch # type: ignore

dragged_item = None
placeholder_counter = 0

NotificationNumber = 0

animQueue = []
animStorage = []
animKeyFrames = []
animRunning = False
animEnded = True

highestZ = 1

def indexLast(list, item):
    return len(list) - 1 - list[::-1].index(item)

def clearDiv(div):
    document.getElementById(div).innerHTML = ""

def hideDiv(div):
    document.getElementById(div).style.visibility = "hidden"

def getCenterCoords(div):
    rect = div.getBoundingClientRect()

    centerX = rect.left + rect.width / 2
    centerY = rect.top + rect.height / 2

    return centerX, centerY

def updateProgressBar(bar, percent):
    if percent <= 0:
        percent = 0
    bar.style.setProperty("--progress", f"{percent * 100}%")

def setPosition(div, positionX, positionY, override):
    ui = document.getElementById(div)
    if not ui:
        return

    if override == "center":
        def centerDiv():
            rect = ui.getBoundingClientRect()
            window_width = window.innerWidth
            window_height = window.innerHeight

            ui.style.position = "absolute"
            ui.style.left = f"{(window_width - rect.width) / 2}px"
            ui.style.top = f"{(window_height - rect.height) / 2}px"

        window.requestAnimationFrame(create_proxy(lambda *_: centerDiv()))
    else:
        def positionDiv():
            ui.style.position = "absolute"
            ui.style.left = positionX
            ui.style.top = positionY

        window.requestAnimationFrame(create_proxy(lambda *_: positionDiv()))

def addText(div, name, text):
    textbox = document.createElement("div")
    textbox.id = name
    textbox.innerHTML = text
    div.appendChild(textbox)

def addDescription(div, text, description):
    originalText = div.innerHTML
    newText = originalText.replace(text, f'<span class="hoverWrapper"><span class="hoverText">{text}</span><span class="descriptionWindow">{description.innerHTML}</span></span>')
    div.innerHTML = newText

def addDescriptionToImage(div, imageAltText, link, description):
    div.innerHTML = ""

    wrapper = document.createElement("span")
    wrapper.className = "hoverWrapper"

    img = document.createElement("img")
    img.id = "image"
    img.src = link
    img.alt = imageAltText
    img.className = "hoverText"
    wrapper.appendChild(img)

    descSpan = document.createElement("span")
    descSpan.className = "descriptionWindow"
    descSpan.appendChild(description)
    wrapper.appendChild(descSpan)

    div.appendChild(wrapper)

def addBar(div, name, barMax, barValue, color):
    if barMax == 0:
        barMax = 1
    barFrame = document.createElement("div")
    barFrame.id = f"{name}BarFrame"
    barFrame.className = "progressBarFrame"
    div.appendChild(barFrame)

    bar = document.createElement("div")
    bar.id = f"{name}Bar"
    bar.className = "progressBar"
    bar.style.backgroundColor = color
    updateProgressBar(bar, barValue / barMax)
    barFrame.appendChild(bar)

def addHp(div, subject):
    hpWindow = document.createElement("div")
    hpWindow.id = "hpWindow"
    hpWindow.className = "windowBody"
    div.appendChild(hpWindow)

    addText(hpWindow, "hp", f"HP: {subject.hp} / {subject.maxhp}")
    addBar(hpWindow, "hp", subject.maxhp, subject.hp, "#b32d2d")

def addJuice(div, subject):
    juiceWindow = document.createElement("div")
    juiceWindow.id = "juiceWindow"
    juiceWindow.className = "windowBody"
    div.appendChild(juiceWindow)

    addText(juiceWindow, "juice", f"JUICE: {subject.juice} / {subject.maxjuice}")
    addBar(juiceWindow, "juice", subject.maxjuice, subject.juice, "#2d4eb3")

def addTitle(div, titleName, X, future, secondaryButton):
    screen = document.getElementById(div)

    if not screen:
        screen = document.createElement("div")
        screen.id = div
        document.body.appendChild(screen)
    else:
        screen.style.display = ""
        screen.innerHTML = ""

    title = document.createElement("div")
    title.className = "title"
    screen.appendChild(title)

    titleText = document.createElement("div")
    titleText.className = "titleText"
    titleText.innerHTML = titleName
    title.appendChild(titleText)

    titleControls = document.createElement("div")
    titleControls.className = "titleControls"
    title.appendChild(titleControls)

    offsetX, offsetY = 0, 0
    dragging = {"active": False}
    currentX, currentY = screen.style.left, screen.style.top

    def pointerdown(e):
        global highestZ
        highestZ += 1
        screen.style.zIndex = highestZ
        if e.target.className != "titleButton":
            dragging["active"] = True
            title.setPointerCapture(e.pointerId)
            nonlocal offsetX, offsetY
            offsetX = e.clientX - screen.getBoundingClientRect().left
            offsetY = e.clientY - screen.getBoundingClientRect().top

    def pointermove(e):
        nonlocal currentX, currentY
        if dragging["active"]:
            currentX = e.clientX - offsetX
            currentY = e.clientY - offsetY

    def pointerup(e):
        dragging["active"] = False
        title.releasePointerCapture(e.pointerId)

    proxies = []
    if X:
        xButton = document.createElement("button")
        xButton.innerHTML = "X"
        xButton.className = "titleButton"
        xButton.setAttribute("aria-label", "Close")

        def onClick(event=None):
            event.stopPropagation()
            if future is not None:
                if not future.done():
                    future.set_result("Exit")
                for i in proxies:
                    i.destroy()
            screen.style.visibility = "hidden"

        proxyClickX = create_proxy(onClick)
        xButton.addEventListener("click", proxyClickX)
        titleControls.appendChild(xButton)
        proxies.append(proxyClickX)
    
    if secondaryButton:
        button2 = document.createElement("button")
        button2.className = "titleButton"
        button2.id = "button2"
        button2.setAttribute("aria-label", "Close")
        titleControls.appendChild(button2)

    def animate(timestamp=None):
        if dragging["active"]:
            screen.style.left = f"{currentX}px"
            screen.style.top = f"{currentY}px"
        requestAnimationFrame(create_proxy(animate))

    proxyDown = create_proxy(pointerdown)
    title.addEventListener("pointerdown", proxyDown)
    proxies.append(proxyDown)
    proxyMove = create_proxy(pointermove)
    screen.addEventListener("pointermove", proxyMove)
    proxies.append(proxyMove)
    proxyUp = create_proxy(pointerup)
    screen.addEventListener("pointerup", proxyUp)
    proxies.append(proxyUp)

    requestAnimationFrame(create_proxy(animate))

    # Return proxies for cleanup
    return proxies

async def WaitForAnimFinished():
    while animRunning:
        await asyncio.sleep(0.01)

def animLoad(animName, info, div, frame, self, targets, AOE, matesList, notMatesList):
    global animStorage, animKeyFrames

    if targets:
        targetList = matesList
    else:
        targetList = notMatesList

    if info[0] == "replaceImage":
        anim = replaceImage(div, info[1], info[2])
        animAdd(anim, frame, True)
        animStorage.append(anim)
        carrier = info[3]
        if "AOE" in carrier:
            carrier.remove("AOE")
            carrier * len(targetList)
        animKeyFrames.append([animName, carrier])

def animlocateFrame(animName, keyframe):
    #print(animKeyFrames, animName, keyframe)
    anim = None
    targetKeyframeId = next((i for i, x in reversed(list(enumerate(animKeyFrames))) if x[0] == animName and keyframe in x[1]), None)
    if not (targetKeyframeId == None):
        anim = animStorage[targetKeyframeId]
    idk = False
    if anim:
        for i in animQueue:
            for j in i:
                if j == anim:
                    idk = True
                    return indexLast(animQueue, i)
        if idk == False:
            return None
    else:
        return None

def animlocateName(frame, keyframe):
    idk = False
    for i in animQueue[frame]:
        if i in animStorage:
            if keyframe in animKeyFrames[animStorage.index(i)][1]:
                idk = True
                return(animKeyFrames[animStorage.index(i)][0])
                break

    if idk == False:
        return None

def animSeekAndDestroy(animName, keyframe):
    global animKeyFrames
    for i in animKeyFrames:
        if i[0] == animName and keyframe in i[1]:
            i[1].remove(keyframe)
            print(animKeyFrames)            
            break

def animAdd(anim, frame, insertNewFrame):
    global animQueue
    if insertNewFrame:
        animQueue.insert(frame, [anim])
    else:
        animQueue[frame].append(anim)
        
def animStart():
    global animEnded, animStorage, animKeyFrames, animRunning
    if animEnded == True and len(animQueue) > 0:
        animEnded = False
        animRunning = True
        animRun()
        
def animRun():
    global animQueue, animEnded, animStorage, animKeyFrames, animRunning

    if len(animQueue) == 0:
        print("Hiyer")
        animEnded = True
        animRunning = False
        animStorage = []
        animKeyFrames = []
        return

    currentFrame = animQueue.pop(0)  # get and remove first frame
    remaining = len(currentFrame)

    def oneDone():
        nonlocal remaining
        remaining -= 1
        if remaining == 0:
            animRun()
            return  # go to next frame

    # Start each anim, passing in one_done callback
    for animFunc in currentFrame:
        animFunc(oneDone)   

def updateHp(target, hp, max): 
    def anim(done):
        characterDiv = document.getElementById(target.id)
        hpDiv = characterDiv.querySelector("#hp")
        if hpDiv:
            target.hp += hp
            if max:
                target.maxhp += hp
            if target.hp > target.maxhp:
                target.hp = target.maxhp
            hpDiv.innerHTML = f"HP: {target.hp} / {target.maxhp}"

            hpBarDiv = characterDiv.querySelector("#hpBar")
            if target.maxhp == 0:
                updateProgressBar(hpBarDiv, 0)
            else:
                updateProgressBar(hpBarDiv, target.hp / target.maxhp)
        setTimeout(create_proxy(lambda: done()), 0)
    return anim
    
def updateJuice(target, juice, max=False):
    def anim(done):
        target.juice += juice
        if max:
                target.maxjuice += juice
        if target.juice > target.maxjuice:
            target.juice = target.maxjuice
        characterDiv = document.getElementById(target.id)
        juiceDiv = characterDiv.querySelector("#juice")
        juiceDiv.innerHTML = f"JUICE: {target.juice} / {target.maxjuice}"

        juiceBarDiv = characterDiv.querySelector("#juiceBar")
        if target.maxjuice == 0:
            updateProgressBar(juiceBarDiv, 0)
        else:
            updateProgressBar(juiceBarDiv, target.juice / target.maxjuice)
        setTimeout(create_proxy(lambda: done()), 0)
    return anim

def updateStatusAdd(target, status):
    def anim(done):
        target.status.append(status)
        characterDiv = document.getElementById(target.id)
        statusDiv = characterDiv.querySelector("#statusEffects")
        grid = statusDiv.querySelector("#statusGrid")

        keywordInfo = keywordList[keywordName.index(status[0])]
        
        iconDiv = document.createElement("div")
        iconDiv.className = "statusIcon"
        iconDiv.id = status[0]

        image = document.createElement("img")
        image.id = "image"
        iconDiv.appendChild(image)
        if isinstance(status[1], int):
            if len(keywordInfo.icon) == 1:
                image.src = keywordInfo.icon[0]
            else:
                if keywordInfo.iconCriteria == "stacks":
                    if status[1] >= len(keywordInfo.icon):
                        image.src = keywordInfo.icon[len(keywordInfo.icon) - 1]
                    else:
                        image.src = keywordInfo.icon[status[1] - 1]
            stacks = document.createElement("div")
            stacks.className = "stacksNumber"
            stacks.id = "stacks"
            stacks.textContent = status[1]
            iconDiv.appendChild(stacks)
        grid.append(iconDiv)
        setTimeout(create_proxy(lambda: done()), 0)
    return anim

def updateStatusChange(target, original, new):
    def anim(done):
        for i in range(len(target.status)):
            if target.status[i] == original:
                target.status[i] == new
        characterDiv = document.getElementById(target.id)
        statusDiv = characterDiv.querySelector("#statusEffects")
        grid = statusDiv.querySelector("#statusGrid")
        iconDiv = statusDiv.querySelector(f"#{new[0]}")
        if iconDiv:
            image = iconDiv.querySelector(f"#image")
            stacks = iconDiv.querySelector(f"#stacks")

            keywordInfo = keywordList[keywordName.index(new[0])]

            if isinstance(new[1], int):
                if len(keywordInfo.icon) == 1:
                    image.src = keywordInfo.icon[0]
                else:
                    if keywordInfo.iconCriteria == "stacks":
                        if new[1] >= len(keywordInfo.icon):
                            image.src = keywordInfo.icon[len(keywordInfo.icon) - 1]
                        else:
                            image.src = keywordInfo.icon[new[1] - 1]
                if stacks:
                    stacks.textContent = new[1]
            grid.append(iconDiv)
        setTimeout(create_proxy(lambda: done()), 0)
    return anim

def updateStatusRemove(target, statusName):
    def anim(done):
        for i in copy.deepcopy(target.status):
            if i[0] == statusName:
                target.status.remove(i)
        characterDiv = document.getElementById(target.id)
        statusDiv = characterDiv.querySelector("#statusEffects")
        grid = statusDiv.querySelector("#statusGrid")
        iconDiv = statusDiv.querySelector(f"#{statusName}")
        iconDiv.remove()

        setTimeout(create_proxy(lambda: done()), 0)
    return anim

def effectNumber(number, div, color, duration):
    def anim(done):
        global highestZ
        x, y = getCenterCoords(div)
        effectDiv = document.createElement("div")
        effectDiv.className = "effectNumber"
        effectDiv.textContent = str(number)
        effectDiv.style.position = "absolute"
        effectDiv.style.left = f"{x}px"
        effectDiv.style.top = f"{y}px"
        effectDiv.style.color = color
        highestZ += 1
        effectDiv.style.zIndex = highestZ
        document.body.appendChild(effectDiv)

        setTimeout(create_proxy(lambda: done()), 0)

        def cleanup():
            if effectDiv.parentNode:
                effectDiv.remove()
        setTimeout(create_proxy(lambda: cleanup()), duration)
    return anim

def replaceImage(div, imageLink, duration):
    def anim(done):
        #imageDiv = div.querySelector("#image")
        #imageDiv.src = imageLink
        print(imageLink)
        setTimeout(create_proxy(lambda: done()), duration)
    return anim

def generateWindow(subject, faction, callbackUse=None, callbackGetTarget=None):
    global highestZ
    hoi = False 
    screen = document.createElement("div")
    screen.className = "window"
    screen.id = subject.id
    screen.setAttribute("draggable", "false")  # Prevent window dragging
    document.body.appendChild(screen)
    highestZ += 1
    screen.style.zIndex = highestZ
    
    addTitle(subject.id, f"{subject.id}.chr", False, None, True)
    for i in range(len(subject.traits)):
        traitInfo = traitList[traitName.index(subject.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "invulnerable":
                hoi = True

    if not hoi:  
        addHp(screen, subject)

    if faction == "player":
        addJuice(screen, subject)

    statusEffectsWindow = document.createElement("div")
    statusEffectsWindow.id = "statusEffects"
    statusEffectsWindow.className = "windowBody"
    screen.appendChild(statusEffectsWindow)

    statusGrid = document.createElement("div")
    statusGrid.id = "statusGrid"
    statusGrid.className = "statusGrid"
    statusEffectsWindow.appendChild(statusGrid)

    viewport_width = window.innerWidth
    viewport_height = window.innerHeight
    window_width = screen.offsetWidth
    window_height = screen.offsetHeight

    max_left = viewport_width - window_width
    max_top = viewport_height - window_height

    random_left = random.randint(0, max(0, max_left))
    random_top = random.randint(0, max(0, max_top))

    screen.style.left = f"{random_left}px"
    screen.style.top = f"{random_top}px"

    # Add dragover and drop handlers to character window
    def on_dragover(event):
        try:
            event.preventDefault()
            event.dataTransfer.dropEffect = "move"
        except Exception as e:
            print(f"Character dragover error: {str(e)}")

    def on_drop(event):
        global dragged_item
        try:
            event.preventDefault()
            targetDiv = document.elementFromPoint(event.clientX, event.clientY)
            windowDiv = targetDiv.closest('.window') if targetDiv else None
            target = callbackGetTarget(windowDiv) if windowDiv else None
            if target and callbackUse:
                callbackUse(f"{dragged_item.id.replace('-', ' ')}", target)
        except Exception as e:
            print(f"Character drop error for {screen.id}: {str(e)}")

    try:
        screen.addEventListener("dragover", create_proxy(on_dragover))
        screen.addEventListener("drop", create_proxy(on_drop))
    except Exception as e:
        print(f"Error binding character window events: {str(e)}")

def generateStatusWindow(subject, faction):
    global highestZ
    hoi = False
    Xpos = "0px"
    Ypos = "0px"

    screen = document.getElementById(f"{subject.id}Status")
    if screen:
        tadaa = True
        # Get the computed position of the div
        rect = screen.getBoundingClientRect()
        Xpos = f"{rect.left}px"
        Ypos = f"{rect.top}px"
        screen.innerHTML = ""
    else:
        tadaa = False
        screen = document.createElement("div")
        screen.className = "window"
        screen.id = f"{subject.id}Status"
        document.body.appendChild(screen)
    
    addTitle(f"{subject.id}Status", f"Status ({subject.id})", True, None, False)

    for i in range(len(subject.traits)):
        traitInfo = traitList[traitName.index(subject.traits[i][0])]
        for j in traitInfo.info:
            if j[0] == "invulnerable":
                hoi = True

    if not hoi:  
        addHp(screen, subject)

    if faction == "player":
        addJuice(screen, subject)

    statWindow = document.createElement("div")
    statWindow.id = "statWindow"
    statWindow.className = "windowBody"
    screen.appendChild(statWindow)

    addText(statWindow, "physStats", f"PHYSICAL STATS: STR: {subject.strength} DEF: {subject.defense} SPD: {subject.speed}")
    addText(statWindow, "specialStats", f"SPECIAL STATS: {' '.join([f'{s[0]}: {s[1]}' for s in subject.specialStats])}")
    texts = []
    for i in subject.status:
        if i[2] == "" or "None":
            texts.append("".join(f"{i[0]} ({i[1]})"))
        else:
            texts.append("".join(f"{i[0]} ({i[1]}), {i[2]} TURNS"))
    text = ",".join(texts)
    addText(statWindow, "status", f"STATUS: {text}")
    texts = []
    for i in subject.skills:
        texts.append(i[0])
    addText(statWindow, "skills", f"SKILLS: {", ".join(texts)}")
    texts = []
    for i in subject.traits:
        texts.append(i[0])
    if faction == "player":
        addText(statWindow, "equipment", f"EQUIPMENT({len(subject.equipment)}/{subject.equipmentSlots}): {", ".join(subject.equipment)}")

    for i in ["STR", "DEF", "SPD"]:
        keywordInfo = keywordList[keywordName.index(i)]

        placeholder = document.createElement("div")
        placeholder.id = i
        placeholder.className = "descriptionWindow"
        screen.appendChild(placeholder)

        placeholderWindow = document.createElement("div")
        placeholderWindow.className = "windowBody"
        placeholder.appendChild(placeholderWindow)

        addText(placeholderWindow, "desc", f"{keywordInfo.desc}")

        addDescription(statWindow.querySelector("#physStats"), i, placeholder)

    for i in range(len(subject.specialStats)):
        keywordInfo = keywordList[keywordName.index(subject.specialStats[i][0])]

        placeholder = document.createElement("div")
        placeholder.id = i
        placeholder.className = "descriptionWindow"
        screen.appendChild(placeholder)

        placeholderWindow = document.createElement("div")
        placeholderWindow.className = "windowBody"
        placeholder.appendChild(placeholderWindow)

        text = f"{keywordInfo.desc}"
        text = text.replace("stacks percent", f"{subject.specialStats[i][1] * 100}%")
        text = text.replace("stacks", f"{subject.specialStats[i][1]}")

        addText(placeholderWindow, "desc", text)

        addDescription(statWindow.querySelector("#specialStats"), subject.specialStats[i][0], placeholder)

    for i in range(len(subject.status)):
        if subject.status[i][0] in keywordName:
            try:
                keywordInfo = keywordList[keywordName.index(subject.status[i][0])]

                placeholder = document.createElement("div")
                placeholder.id = i
                placeholder.className = "descriptionWindow"
                screen.appendChild(placeholder)

                placeholderWindow = document.createElement("div")
                placeholderWindow.className = "windowBody"
                placeholder.appendChild(placeholderWindow)

                text = f"{keywordInfo.desc}"
                text = text.replace("stacks percent", f"{subject.status[i][1] * 100}%")
                text = text.replace("stacks", f"{subject.status[i][1]}")

                addText(placeholderWindow, "desc", text)

                addDescription(statWindow.querySelector("#status"), subject.status[i][0], placeholder)
            except Exception as e:
                placeholder_counter += 0

    addText(statWindow, "traits", f"TRAITS: {", ".join(texts)}")
    for i in subject.traits:
        traitInfo = traitList[traitName.index(i[0])]

        placeholder = document.createElement("div")
        placeholder.id = i[0]
        placeholder.className = "descriptionWindow"
        screen.appendChild(placeholder)

        placeholderWindow = document.createElement("div")
        placeholderWindow.className = "windowBody"
        placeholder.appendChild(placeholderWindow)

        text = createSkillDesc(subject, i[0])

        addText(placeholderWindow, "desc", f"{text}")

        addDescription(statWindow.querySelector("#traits"), i[0], placeholder)

    for i in subject.skills:
        skillInfo = skillList[skillName.index(i[0])]

        placeholder = document.createElement("div")
        placeholder.id = i[0]
        placeholder.className = "descriptionWindow"
        screen.appendChild(placeholder)

        placeholderWindow = document.createElement("div")
        placeholderWindow.className = "windowBody"
        placeholder.appendChild(placeholderWindow)

        text = createSkillDesc(subject, i[0])

        addText(placeholderWindow, "desc", text)

        if faction == "player":
            addText(placeholderWindow, "juiceCost", f"Juice required: {skillInfo.juiceCost}")
        addText(placeholderWindow, "accuracy",  f"Accuracy: {skillInfo.acc * 100}%")

        addDescription(statWindow.querySelector("#skills"), i[0], placeholder)
    
    if faction == "player":
        for i in subject.equipment:
            itemInfo = itemList[itemName.index(i)]

            placeholder = document.createElement("div")
            placeholder.id = i
            placeholder.className = "descriptionWindow"
            screen.appendChild(placeholder)

            placeholderWindow = document.createElement("div")
            placeholderWindow.className = "windowBody"
            placeholder.appendChild(placeholderWindow)

            text = createSkillDesc(subject, i)

            addText(placeholderWindow, "desc", f"{text}")

            addDescription(statWindow.querySelector("#equipment"), i, placeholder)

    highestZ += 1
    screen.style.zIndex = highestZ

    if not tadaa:
        viewport_width = window.innerWidth
        viewport_height = window.innerHeight
        window_width = screen.offsetWidth or 200  # Fallback if offsetWidth is 0
        window_height = screen.offsetHeight or 200  # Fallback if offsetHeight is 0
        max_left = viewport_width - window_width
        max_top = viewport_height - window_height
        Xpos = f"{random.randint(0, max(0, max_left))}px"
        Ypos = f"{random.randint(0, max(0, max_top))}px"

    # Apply the position immediately
    setPosition(f"{subject.id}Status", Xpos, Ypos, "")
    
    screen.style.visibility = ""

async def choose(options, div, title, content, Exit):
    global future, highestZ
    future = asyncio.Future()
    Xpos = "0px"
    Ypos = "0px"

    Exit = Exit.lower() == "true" if isinstance(Exit, str) else bool(Exit)

    container = document.getElementById(div)
    if container:
        tadaa = True
        # Get the computed position of the div
        rect = container.getBoundingClientRect()
        Xpos = f"{rect.left}px"
        Ypos = f"{rect.top}px"
        container.innerHTML = ""
    else:
        tadaa = False
        container = document.createElement("div")
        container.id = div
        container.className = "window"
        document.body.appendChild(container)

    # Title first
    addTitle(div, title, Exit, future, False)


    if content:
        windowBody = document.createElement("div")
        windowBody.className = "windowBody"
        windowBody.innerHTML = content
        container.appendChild(windowBody)

    button_proxies = []
    for value in options:
        btn = document.createElement("button")
        btn.innerHTML = value

        def onClick(event=None, val=value):
            if not future.done():
                future.set_result(val)

        proxyClick = create_proxy(onClick)
        btn.addEventListener("click", proxyClick)
        button_proxies.append(proxyClick)
        container.appendChild(btn)

    highestZ += 1
    container.style.zIndex = highestZ

    if not tadaa:
        viewport_width = window.innerWidth
        viewport_height = window.innerHeight
        window_width = container.offsetWidth or 200  # Fallback if offsetWidth is 0
        window_height = container.offsetHeight or 200  # Fallback if offsetHeight is 0
        max_left = viewport_width - window_width
        max_top = viewport_height - window_height
        Xpos = f"{random.randint(0, max(0, max_left))}px"
        Ypos = f"{random.randint(0, max(0, max_top))}px"

    # Apply the position immediately
    setPosition(div, Xpos, Ypos, "")

    container.style.visibility = "visible"

    result = await future

    # Clean up all proxies
    for proxy in button_proxies:
        try:
            proxy.destroy()
        except Exception:
            pass

    container.style.visibility = "hidden"

    return result

def makeIconDraggable(item, grid, gridName, callbackSwap=None, callbackClick=None, callbackSaveUpload=None, callbackSaveDownload=None):
    global dragged_item, placeholder_counter

    def on_dragstart(event):
        global dragged_item, placeholder_counter
        if gridName == "Bag" or "App":
            if dragged_item:
                event.preventDefault()
                return
            dragged_item = item
            event.dataTransfer.setData("text/plain", item.id)
            event.dataTransfer.effectAllowed = "move"
            item.classList.add("dragging")
            def add_placeholder():
                global placeholder_counter
                safe_id = item.id.replace(" ", "-")
                old_placeholders = grid.querySelectorAll(f"[id^=placeholder-{safe_id}-]")
                for old in old_placeholders:
                    if old.parentNode:
                        old.remove()
                placeholder_counter += 1
                placeholder_id = f"placeholder-{safe_id}-{placeholder_counter}"
                placeholder = document.createElement("div")
                placeholder.className = "placeholder"
                placeholder.id = placeholder_id
                if item.parentNode == grid:
                    grid.replaceChild(placeholder, item)
                else:
                    grid.appendChild(placeholder)
            setTimeout(create_proxy(add_placeholder), 0)

    def on_dragover(event):
        global dragged_item
        if gridName == "Bag" or "App":
            event.preventDefault()
            event.dataTransfer.dropEffect = "move"
            if not dragged_item:
                return
            safe_id = dragged_item.id.replace(" ", "-")
            placeholder = grid.querySelector(f"[id^=placeholder-{safe_id}-]")
            if not placeholder:
                return
            target = document.elementFromPoint(event.clientX, event.clientY)
            if target:
                targetIcon = target.closest('.itemIcon')
                if targetIcon and target != dragged_item:
                    if gridName == "Bag":
                        callbackSwap(f"{dragged_item.id.replace('-', ' ')}" , f"{targetIcon.id.replace('-', ' ')}")
                if target.classList.contains("itemIcon") and target != dragged_item:
                    grid.insertBefore(placeholder, target)
                elif target.classList.contains("placeholder"):
                    pass
                else:
                    grid.appendChild(placeholder)

    def on_dragend(event):
        global dragged_item
        if gridName == "Bag" or "App":
            item.classList.remove("dragging")
            if not dragged_item:
                return
            safe_id = dragged_item.id.replace(" ", "-")
            placeholder = grid.querySelector(f"[id^=placeholder-{safe_id}-]")
            if placeholder and placeholder.parentNode == grid:
                grid.replaceChild(dragged_item, placeholder)
            else:
                grid.appendChild(dragged_item)
            old_placeholders = grid.querySelectorAll(f"[id^=placeholder-{safe_id}-]")
            for old in old_placeholders:
                if old.parentNode:
                    old.remove()
            dragged_item = None

    def on_drop(event):
        global dragged_item
        if gridName == "Bag" or "App":
            try:
                event.preventDefault()
            except Exception as e:
                print(f"Drop error for {item.id}: {str(e)}")
    
    def on_click(event):
        if callbackClick:
            if callbackSaveUpload and callbackSaveDownload:
                callbackClick(callbackSaveUpload, callbackSaveDownload)
            elif gridName == "Shop":
                callbackClick(item.id.replace('-', ' '), item, item.parentNode.parentNode.id)
            else:
                callbackClick()

    if gridName == "Bag" or "App":
        item.setAttribute("draggable", "true")
        item.addEventListener("dragstart", create_proxy(on_dragstart))
        item.addEventListener("dragover", create_proxy(on_dragover))
        item.addEventListener("dragend", create_proxy(on_dragend))
        item.addEventListener("drop", create_proxy(on_drop))
    item.addEventListener("click", create_proxy(on_click))

def generateBagWindow(bag, coinAmount, callbackSwap=None):
    global highestZ
    Xpos = "0px"
    Ypos = "0px"

    screen = document.getElementById(f"BagWindow")
    if screen:
        tadaa = True
        # Get the computed position of the div
        rect = screen.getBoundingClientRect()
        Xpos = f"{rect.left}px"
        Ypos = f"{rect.top}px"
        screen.innerHTML = ""
    else:
        tadaa = False
        screen = document.createElement("div")
        screen.id = "BagWindow"
        screen.className = "window"
        document.body.appendChild(screen)
    
    addTitle("BagWindow", "Bag", True, None, False)

    coins = document.createElement("div")
    coins.className = "windowBody"
    coins.id = "Coins"
    coins.innerHTML = f"COINS: {coinAmount}"
    screen.appendChild(coins)

    items = document.createElement("div")
    items.className = "windowBody"
    items.id = "Items"
    screen.appendChild(items)

    grid = document.createElement("div")
    grid.className = "itemGrid"
    grid.id = "BagGrid"
    items.appendChild(grid)
    
    for i in bag:
        itemInfo = itemList[itemName.index(i[0])]
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
        
        addText(placeholderWindow, f"desc-text-{itemInfo.id.replace(' ', '-')}", f"{i[0]} x{i[1]}")
        addDescriptionToImage(item, itemInfo.id, itemInfo.image, placeholderWindow)
        makeIconDraggable(item, grid, "Bag", callbackSwap, None, None, None)
        grid.appendChild(item)


    if not tadaa:
        viewport_width = window.innerWidth
        viewport_height = window.innerHeight
        window_width = screen.offsetWidth or 200  # Fallback if offsetWidth is 0
        window_height = screen.offsetHeight or 200  # Fallback if offsetHeight is 0
        max_left = viewport_width - window_width
        max_top = viewport_height - window_height
        Xpos = f"{random.randint(0, max(0, max_left))}px"
        Ypos = f"{random.randint(0, max(0, max_top))}px"

    # Apply the position immediately
    setPosition("BagWindow", Xpos, Ypos, "")

    highestZ += 1
    screen.style.zIndex = highestZ
    screen.style.visibility = "visible"

def Notification(text):
    global NotificationNumber, highestZ
    NotificationNumber += 1
    container = document.createElement("div")
    container.id = f"Notification {NotificationNumber}"
    container.className = "window"
    document.body.appendChild(container)
    # Randomize position for new divs
    viewport_width = window.innerWidth
    viewport_height = window.innerHeight
    viewport_height = window.innerHeight
    window_width = container.offsetWidth or 200  # Fallback if offsetWidth is 0
    window_height = container.offsetHeight or 200  # Fallback if offsetHeight is 0
    max_left = viewport_width - window_width
    max_top = viewport_height - window_height
    Xpos = f"{random.randint(0, max(0, max_left))}px"
    Ypos = f"{random.randint(0, max(0, max_top))}px"

    # Title first
    addTitle(container.id, "Notification", True, None, False)

    # Apply the position immediately
    setPosition(container.id, Xpos, Ypos, "")

    windowBody = document.createElement("div")
    windowBody.className = "windowBody"
    windowBody.innerHTML = text
    container.appendChild(windowBody)
    highestZ += 1
    container.style.zIndex = highestZ

def createSkillDesc(user, hoi):
    buffing = False
    text = ""
    if hoi in skillName:
        skillData = copy.deepcopy(skillList[skillName.index(hoi)])
        idk = skillData.info
        text = skillData.actualDesc
        if skillData.multi > 1:
            text = re.sub(r'\bmulti\b', f"{skillData.multi}", text, count=1)
    elif hoi in traitName:
        skillData = copy.deepcopy(traitList[traitName.index(hoi)])
        idk = skillData.info
        text = skillData.actualDesc
        secondaryNumber = next((s for s in user.traits if s[0] == hoi), [0, 0])[1]
        text = re.sub(r'\bsecondaryNumber\b', f"{secondaryNumber}", text, count=1)
    elif hoi in itemName:
        skillData = copy.deepcopy(itemList[itemName.index(hoi)])
        idk = skillData.info
        text = skillData.actualDesc
        if skillData.type == "weapon" or "relic":
            buffing = True

    if not (isinstance(idk[0], tuple) or isinstance(idk[0], list)):
        idk = [idk]

    for info in idk: 
        for i in range(len(info)):
            if isinstance(info[i], list):
                carrier = 0
                for j in range(len(info[i])):
                    if info[i][j] == "secondaryNumber":
                        info[i][j] = next((s for s in user.skills + user.traits if s[0] == hoi), [0, 0])[1]
                    if (isinstance(info[i][j], int) or isinstance(info[i][j], float)): 
                        carrier += info[i][j]
                    else:
                        carrier += 0
                info[i] = math.ceil(carrier)

    for info in idk: 
        for i in range(len(info)):
            if info[i] == "damage":
                if next((s for s in user.specialStats if s[0] == "VIOLET"), [0, 0])[1] > 0:
                    violet = 2
                else:
                    violet = 1
                if info[i + 1] in ["fixed", "max"]:
                    maxDamage = math.ceil(info[i + 2] * (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1)
                    * violet)
                    minDamage = math.ceil(info[i + 2] * (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1)
                    * violet)
                else:

                    if info[i + 1] == "str":
                        damage = user.strength
                    elif info[i + 1] == "spd":
                        damage = user.speed
                    elif info[i + 1] == "def":
                        damage = user.defense
                    elif info[i + 1] == "FAITH":
                        damage = next((s for s in user.status if s[0] == "FAITH"), [0, 0, 0, 0])[1]

                    maxDamage = math.ceil(damage * info[i + 2] *\
                    (1 + info[i + 3]) *\
                    (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1) * violet)

                    if maxDamage <= 0:
                        maxDamage = 1
                    
                    minDamage = math.ceil(damage * info[i + 2] *\
                    (1 - info[i + 3]) *\
                    (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1) * violet)

                    if minDamage <= 0:
                        minDamage = 1
                
                if maxDamage == minDamage:
                    text = re.sub(r'\bdamageAmount\b', f"{maxDamage}", text, count=1)
                else:
                    text = re.sub(r'\bdamageAmount\b', f"{minDamage}-{maxDamage}", text, count=1)
            if info[i] == "selfDamage":
                if next((s for s in user.specialStats if s[0] == "VIOLET"), [0, 0])[1] > 0:
                    violet = 2
                else:
                    violet = 1
                if info[i + 1] in ["fixed", "max"]:
                    maxDamage = math.ceil(info[i + 2] * (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1)
                    * violet)
                    minDamage = math.ceil(info[i + 2] * (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1)
                    * violet)
                else:
                    if next((s for s in user.specialStats if s[0] == "VIOLET"), [0, 0])[1] > 0:
                        violet = 2
                    else:
                        violet = 1

                    if info[i + 1] == "str":
                        damage = user.strength
                    elif info[i + 1] == "spd":
                        damage = user.speed
                    elif info[i + 1] == "def":
                        damage = user.defense
                    elif info[i + 1] == "FAITH":
                        damage = next((s for s in user.status if s[0] == "FAITH"), [0, 0, 0, 0])[1]

                    maxDamage = math.ceil(damage * info[i + 2] *\
                    (1 + info[i + 3]) *\
                    (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1) * violet)

                    if maxDamage <= 0:
                        maxDamage = 1
                    
                    minDamage = math.ceil(damage * info[i + 2] *\
                    (1 - info[i + 3]) *\
                    (next((s for s in user.specialStats if s[0] == "DAMAGEUP"), [0, 0, 0])[1] + 1) * violet)

                    if minDamage <= 0:
                        minDamage = 1
                
                if maxDamage == minDamage:
                    text = re.sub(r'\bselfDamageAmount\b', f"{maxDamage}", text, count=1)
                else:
                    text = re.sub(r'\bselfDamageAmount\b', f"{minDamage}-{maxDamage}", text, count=1)            
            if info[i] == "heal":
                healBonus = next((s for s in user.specialStats if s[0] == "HEALBONUS"), [0, 0, 0])[1]
                healAmount = info[info.index("heal") + 1] + healBonus
                text.replace("healAmount", f"{healAmount}")
                text = re.sub(r'\bhealAmount\b', f"{healAmount}", text, count=1)
            if info[i] == "ammo":
                ammoAmount = info[info.index("ammo") + 1]
                text = re.sub(r'\bammoAmount\b', f"{-ammoAmount}", text, count=1)
            if info[i] == "chant":
                chantAmount = info[info.index("chant") + 1]
                text = re.sub(r'\bchantAmount\b', f"{chantAmount}", text, count=1)
            if info[i] == "summon":
                summonned = info[info.index("summon") + 1]
                text = re.sub(r'\bsummonned\b', f"{summonned}", text, count=1)
            if info[i] == "drunk":
                drunkApplyChance = info[info.index("drunk") + 1]
                drunkStacks = info[info.index("drunk") + 2]
                drunkStacksChange = info[info.index("drunk") + 3]
                drunkDuration = info[info.index("drunk") + 4]
                
                text = re.sub(r"\bdrunkApplyChance\b", f"{drunkApplyChance * 100}%", text, count=1)
                text = re.sub(r"\bdrunkStacks\b", f"{drunkStacks}", text, count=1)
                text = re.sub(r"\bdrunkStacksChange\b", f"{drunkStacksChange}", text, count=1)
                text = re.sub(r"\bdrunkDuration\b", f"{drunkDuration}", text, count=1)
            if info[i] == "bleed":
                bleedApplyChance = info[info.index("bleed") + 1]
                bleedStacks = info[info.index("bleed") + 2]
                
                text = re.sub(r"\bbleedApplyChance\b", f"{bleedApplyChance * 100}%", text, count=1)
                text = re.sub(r"\bbleedStacks\b", f"{bleedStacks}", text, count=1)
            if info[i] == "hemotoxin":
                hemotoxinApplyChance = info[info.index("hemotoxin") + 1]
                hemotoxinStacks = info[info.index("hemotoxin") + 2]
                
                text = re.sub(r"\bhemotoxinApplyChance\b", f"{hemotoxinApplyChance * 100}%", text, count=1)
                text = re.sub(r"\bhemotoxinStacks\b", f"{hemotoxinStacks}", text, count=1)
            if info[i] == "plague":
                plagueApplyChance = info[info.index("plague") + 1]
                plagueStacks = info[info.index("plague") + 2]
                
                text = re.sub(r"\bplagueApplyChance\b", f"{plagueApplyChance * 100}%", text, count=1)
                text = re.sub(r"\bplagueStacks\b", f"{plagueStacks}", text, count=1)
            if info[i] == "taunt":
                tauntApplyChance = info[info.index("taunt") + 1]
                tauntStacks = info[info.index("taunt") + 2]
                
                text = re.sub(r"\btauntApplyChance\b", f"{tauntApplyChance * 100}%", text, count=1)
                text = re.sub(r"\btauntStacks\b", f"{tauntStacks}", text, count=1)
            if info[i] == "stars":
                starsAmount = info[info.index("stars") + 1]
                text = re.sub(r"\bstarsAmount\b", f"{starsAmount}", text, count=1)
            if info[i] == "stealth":
                stealthAmount = info[i + 1]
                text = re.sub(r"\bstealthAmount\b", f"{stealthAmount}", text, count=1)
            if info[i] == "faith":
                if isinstance(info[i + 1], int):
                    faithAmount = info[i + 1]
                    text = re.sub(r"\bstealthAmount\b", f"{stealthAmount}", text, count=1)
            if info[i] == "buffDuration":
                buffDuration = info[i + 1]
                text = re.sub(r"\bbuffDuration\b", f"{buffDuration}", text, count=1)
            if info[i] == "counter":
                counterAmount = info[info.index("counter") + 1]
                text = re.sub(r"\bcounterAmount\b", f"{counterAmount}", text, count=1)
            if info[i] == "loot":
                lootType = info[info.index("loot") + 1]
                lootAmount = info[info.index("loot") + 2]

                text = re.sub(r"\blootType\b", f"{lootType}", text, count=1)
                text = re.sub(r"\blootAmount\b", f"{lootAmount}", text, count=1)
            if info[i] == "swarm":
                swarmAmount = info[info.index("swarm") + 1]
                text = re.sub(r"\bswarmAmount\b", f"{swarmAmount}", text, count=1)
            if info[i] == "cleanse":
                cleanseAmount = info[info.index("cleanse") + 1]
                text = re.sub(r"\bcleanseAmount\b", f"{cleanseAmount}", text, count=1)
            if info[i] == "useSkill":
                if isinstance(info[i + 1], int):
                    skillUsed = user.skills[info[i + 1]]
                else:
                    skillUsed = info[i + 1]
                text = re.sub(r"\bskillUsed\b", f"{skillUsed}", text, count=1)
            if info[i] == "checkStacks":
                stacksRequired = info[i + 3]
                text = re.sub(r"\bstacksRequired\b", f"{stacksRequired}", text, count=1)
            if info[i] == "buff":
                buffing = True
            if info[i] == "buffEnd":
                buffing = False
            if info[i] == "str" and buffing:
                strAmount = info[info.index("str") + 1]
                text = re.sub(r"\bstrAmount\b", f"{strAmount}", text, count=1)        
            if info[i] == "spd" and buffing:
                spdAmount = info[info.index("spd") + 1]
                text = re.sub(r"\bspdAmount\b", f"{spdAmount}", text, count=1)        
            if info[i] == "def" and buffing:
                defAmount = info[info.index("def") + 1]
                text = re.sub(r"\bdefAmount\b", f"{defAmount}", text, count=1)
            if info[i] == "penetration" and buffing:
                penetrationAmount = info[info.index("penetration") + 1]
                text = re.sub(r"\bpenetrationAmount\b", f"{penetrationAmount * 100}%", text, count=1)
            if info[i] == "thorns" and buffing:
                thornsAmount = info[info.index("thorns") + 1]
                text = re.sub(r"\bthornsAmount\b", f"{thornsAmount}", text, count=1)
            if info[i] == "dodge" and buffing:
                dodgeAmount = info[info.index("dodge") + 1]
                text = re.sub(r"\bdodgeAmount\b", f"{dodgeAmount * 100}%", text, count=1)        
            if info[i] == "crimson" and buffing:
                crimsonAmount = info[info.index("crimson") + 1]
                text = re.sub(r"\bcrimsonAmount\b", f"{crimsonAmount}", text, count=1)
            if info[i] == "cobalt" and buffing:
                cobaltAmount = info[info.index("cobalt") + 1]
                text = re.sub(r"\bcobaltAmount\b", f"{cobaltAmount}", text, count=1)
            if info[i] == "violet" and buffing:
                violetAmount = info[info.index("violet") + 1]
                text = re.sub(r"\bvioletAmount\b", f"{violetAmount}", text, count=1) 
            if info[i] == "damageUp" and buffing:
                damageUpAmount = info[info.index("damageUp") + 1]
                text = re.sub(r"\bdamageUpAmount\b", f"{damageUpAmount * 100}%", text, count=1)  
            if info[i] == "bleedBonus" and buffing:
                bleedBonusAmount = info[info.index("bleedBonus") + 1]
                text = re.sub(r"\bbleedBonusAmount\b", f"{bleedBonusAmount}", text, count=1)  
            if info[i] == "healBonus" and buffing:
                violetAmount = info[info.index("healBonus") + 1]
                text = re.sub(r"\bhealBonus\b", f"{healBonus}", text, count=1)
            if info[i] == "trait" and buffing:
                traitAmount = info[info.index("trait") + 2]
                text = re.sub(r"\btraitAmount\b", f"{traitAmount}", text, count=1)     
    return text

def generateOSScreen(CallbackShop=None, CallbackBag=None, CallbackSave=None, CallbackSaveUpload=None, CallbackSaveDownload=None):
    screen = document.createElement("div")
    screen.id = "AppManager"
    document.body.appendChild(screen)

    grid = document.createElement("div")
    grid.className = "appGrid"
    grid.id = "Apps"
    screen.appendChild(grid)

    apps = ["BLK-M4K3T", "Bag", "Archiver"]
    appCallbacks = [CallbackShop, CallbackBag, CallbackSave]
    for i in apps:
        app = document.createElement("div")
        app.className = "appIcon"
        # Sanitize ID to avoid spaces
        app.id = f"{i}"
        app.innerHTML = f"{i}"

        if i == "Archiver":
            makeIconDraggable(app, grid, "App", None, callbackClick=appCallbacks[apps.index(i)], callbackSaveUpload=CallbackSaveUpload, callbackSaveDownload=CallbackSaveDownload)
        else: 
            makeIconDraggable(app, grid, "App", None, callbackClick=appCallbacks[apps.index(i)], callbackSaveUpload=None, callbackSaveDownload=None)
        grid.appendChild(app)

def generateSaveWindow(CallbackSaveUpload=None, CallbackSaveDownload=None):
    global highestZ
    Xpos = "0px"
    Ypos = "0px"

    screen = document.getElementById(f"SaveManager")
    if screen:
        tadaa = True
        # Get the computed position of the div
        rect = screen.getBoundingClientRect()
        Xpos = f"{rect.left}px"
        Ypos = f"{rect.top}px"
        screen.innerHTML = ""
    else:
        tadaa = False
        screen = document.createElement("div")
        screen.id = "SaveManager"
        screen.className = "window"
        document.body.appendChild(screen)
    
    addTitle("SaveManager", "Archiver", True, None, False)

    windowBody = document.createElement("div")
    windowBody.className = "windowBody"
    windowBody.innerHTML = "Welcome to Archiver! Your files are safe with us! We hope."
    screen.appendChild(windowBody)

    uploadButton = document.createElement("input")
    uploadButton.type = "file"
    uploadButton.id = "upload"
    uploadButton.style.visibility = "hidden"
    windowBody.appendChild(uploadButton)

    uploadLabel = document.createElement("label")
    uploadLabel.htmlFor = "upload"
    uploadLabel.id = "uploadLabel"
    uploadLabel.innerText = "Click to upload."
    windowBody.appendChild(uploadLabel)

    CallbackSaveUpload()

    downloadButton = document.createElement("button")
    downloadButton.id = "download"
    downloadButton.innerHTML = "Download Save File"
    windowBody.appendChild(downloadButton)

    CallbackSaveDownload()

    if not tadaa:
        viewport_width = window.innerWidth
        viewport_height = window.innerHeight
        window_width = screen.offsetWidth or 200  # Fallback if offsetWidth is 0
        window_height = screen.offsetHeight or 200  # Fallback if offsetHeight is 0
        max_left = viewport_width - window_width
        max_top = viewport_height - window_height
        Xpos = f"{random.randint(0, max(0, max_left))}px"
        Ypos = f"{random.randint(0, max(0, max_top))}px"

    # Apply the position immediately
    setPosition("SaveManager", Xpos, Ypos, "")
    highestZ += 1
    screen.style.zIndex = highestZ
    screen.style.visibility = "visible"

def generateShopWindow(shopDatabase, CallbackBuy=None, CallbackRestock=None):
    global highestZ
    Xpos = "0px"
    Ypos = "0px"

    screen = document.getElementById(f"ShopWindow")
    if screen:
        tadaa = True
        # Get the computed position of the div
        rect = screen.getBoundingClientRect()
        Xpos = f"{rect.left}px"
        Ypos = f"{rect.top}px"
        screen.innerHTML = ""
    else:
        tadaa = False
        screen = document.createElement("div")
        screen.id = "ShopWindow"
        screen.className = "window"
        document.body.appendChild(screen)
        shopDatabase = CallbackRestock()
    
    addTitle("ShopWindow", "BLK-M4K3T", True, None, False)
    highestZ += 1
    screen.style.zIndex = highestZ

    abilityVendor = document.createElement("div")
    abilityVendor.id = "abilityVendor"
    abilityVendor.className = "windowBody"
    screen.append(abilityVendor)

    abilityVendorGrid = document.createElement("div")
    abilityVendorGrid.className = "itemGrid"
    abilityVendorGrid.id = "abilityVendorGrid"
    abilityVendor.appendChild(abilityVendorGrid)

    for i in shopDatabase[0]:
        shopItem = document.createElement("div")
        shopItem.className = "itemIcon"
        # Sanitize ID to avoid spaces
        shopItem.id = f"{i.id.replace(' ', '-')}"
        shopItem.innerHTML = i.id
        
        placeholder = document.createElement("div")
        placeholder.id = f"{i.id.replace(' ', '-')}-desc"
        placeholder.className = "descriptionWindow"
        screen.appendChild(placeholder)

        placeholderWindow = document.createElement("div")
        placeholderWindow.className = "windowBody"
        placeholder.appendChild(placeholderWindow)
        
        addText(placeholderWindow, f"desc-text-{i.id.replace(' ', '-')}", f"{i.desc}")
        makeIconDraggable(shopItem, abilityVendorGrid, "Shop", None, CallbackBuy, None, None)
        addDescription(shopItem, i.id, placeholderWindow)
        abilityVendorGrid.appendChild(shopItem)
    
    if not tadaa:
        viewport_width = window.innerWidth
        viewport_height = window.innerHeight
        window_width = screen.offsetWidth or 200  # Fallback if offsetWidth is 0
        window_height = screen.offsetHeight or 200  # Fallback if offsetHeight is 0
        max_left = viewport_width - window_width
        max_top = viewport_height - window_height
        Xpos = f"{random.randint(0, max(0, max_left))}px"
        Ypos = f"{random.randint(0, max(0, max_top))}px"

    setPosition("ShopWindow", Xpos, Ypos, "")
    screen.style.visibility = "visible"