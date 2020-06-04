import pyautogui
import pydirectinput
import time
import mouse
import win32api, win32con

#  Toggles (True or False) for whether the mouse control is active
inputToggles = {
    'move_mouse'    : True,
    'click'         : True,
    'double_click'  : True,
    'drag'          : True,

}

#  Toggles (True or False) for whether the keyboard control is active
keyboardToggles = {
    'space'         : True,
    'up'            : True,
    'down'          : True,
    'left'          : True,
    'right'         : True,
    'w'             : True,
    'a'             : True,
    's'             : True,
    'd'             : True,
    'f'             : True,
    'g'             : True,
    'enter'         : True,
}

def checkMessageForInputToggles(message):
    message = message.lower()

    if "move_mouse" in message and inputToggles['move_mouse']:
        processMoveMouseCommand(message)
    elif "double_click" in message and inputToggles['double_click']:
        pyautogui.doubleClick()
    elif "click" in message and inputToggles['click']:
        pyautogui.click()
    elif "drag" in message and inputToggles['drag']:
        processDragCommand(message)
    else:
        for keyString in keyboardToggles:
            if keyString in message and keyboardToggles[keyString]:
                keyboardKeyTap(message)
                break

def processMoveMouseCommand(message):
    mouseMoveMessage = message.split(" ")
    if len(mouseMoveMessage) != 3:
        return 0
    
    #print("mouseMoveMessage: ")
    #print(mouseMoveMessage)
    if IsStringInt(mouseMoveMessage[1]) == False:
        return 0
        
    if IsStringInt(mouseMoveMessage[2]) == False:
        return 0
    
    #mouseMoveTest2(int(mouseMoveMessage[1]), int(mouseMoveMessage[2]))
    #mouseMoveTest1(int(mouseMoveMessage[1]), int(mouseMoveMessage[2]))
    moveMouse(int(mouseMoveMessage[1]), int(mouseMoveMessage[2]))

def processDragCommand(message):
    mouseDragMessage = message.split(" ")
    if len(mouseDragMessage) != 3:
        return 0
    
    #print("mouseDragMessage: ")
    #print(mouseDragMessage)
    if IsStringInt(mouseDragMessage[1]) == False:
        print("IsStringInt(mouseDragMessage[1]) == False")
        return 0
        
    if IsStringInt(mouseDragMessage[2]) == False:
        print("IsStringInt(mouseDragMessage[2]) == False")
        return 0
    
    dragMouse(int(mouseDragMessage[1]), int(mouseDragMessage[2]))

#  Standard keyboard key tap using pyautogui
def keyboardKeyTap(keystring):
    pyautogui.keyDown(keystring)
    pyautogui.keyUp(keystring)

#  Standard mouse drag using pyautogui with checks
def dragMouse(xDelta, yDelta):
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    #print(screenWidth, screenHeight, currentMouseX, currentMouseY, xDelta, yDelta)

    moveToX = currentMouseX + xDelta
    moveToY = currentMouseY + yDelta

    if moveToX >= screenWidth:
        moveToX = screenWidth - 1
    
    if moveToY >= screenHeight:
        moveToY = screenHeight - 1

    if moveToX <= 0:
        moveToX = 1

    if moveToY <= 0:
        moveToY = 1

    #print("moveToX:")
    #print(moveToX)
    #print("\n")
    #print("moveToY:")
    #print(moveToY)
    #print("\n")

    print("pyautogui.drag(xDelta, yDelta, duration=0.5)")
    pyautogui.drag(xDelta, yDelta, duration=0.5)
    
#  Standard mouse move using pyautogui with checks
def moveMouse(xDelta, yDelta):
    screenWidth, screenHeight = pyautogui.size()
    currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.
    #print(screenWidth, screenHeight, currentMouseX, currentMouseY, xDelta, yDelta)

    moveToX = currentMouseX + xDelta
    moveToY = currentMouseY + yDelta

    if moveToX >= screenWidth:
        moveToX = screenWidth - 1
    
    if moveToY >= screenHeight:
        moveToY = screenHeight - 1

    if moveToX <= 0:
        moveToX = 1

    if moveToY <= 0:
        moveToY = 1

    #print("moveToX:")
    #print(moveToX)
    #print("\n")
    #print("moveToY:")
    #print(moveToY)
    #print("\n")

    pyautogui.moveRel(xDelta, yDelta, duration=0.5)
    #pyautogui.moveTo(moveToX, moveToY)#, duration=2, tween=pyautogui.easeInOutQuad)

#  Testing moving itereatively
def mouseMoveTest1(xDelta, yDelta):
    #print(xDelta, yDelta)
    for i in range(40):
        #print(xDelta + i, yDelta + i)
        pyautogui.moveRel(10, 0, duration=0.05)
        pydirectinput.moveRel(xDelta + i, yDelta + i, 0.04)
        time.sleep(0.05)

#  Testing using pydirectinput
def mouseMoveTest2(xDelta, yDelta):
    #mouse.drag(0, 0, xDelta, yDelta, absolute=False, duration=0.1)
    #mouse.move(xDelta, yDelta, absolute=False, duration=0.4)
    #pydirectinput.move(xDelta, yDelta)
    pydirectinput.moveTo(xDelta, yDelta)

#  Testing using win32api
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#  Helper functions
def IsStringInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False