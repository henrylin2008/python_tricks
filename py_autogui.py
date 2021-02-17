import pyautogui

# General Functions
# move mouse over to the position, ctrl+shift+R to get the current mouse (x, y)
print(pyautogui.position())
# print(pyautogui.size())     # current screen resolution width and height
# pyautogui.onScreen(x, y)  # True if x & y are within the screen.

# Fail-Safes
# pyautogui.PAUSE = 2.5   # set up a 2.5 second pause
# pyautogui.FAILSAFE = True # moving the mouse to the upper-left will raise a pyautogui.FailSafeException that can
                            # abort your program

# Mouse Functions
# pyautogui.moveTo(348, 81, duration=1)  # move mouse to XY coordinates over num_second seconds
# pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
# pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
# pyautogui.dragTo(x, y, duration=num_seconds)  # drag mouse to XY
# pyautogui.dragRel(xOffset, yOffset, duration=num_seconds)  # drag mouse relative to its current position
pyautogui.click(348, 81, button='left')
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
# pyautogui.displayMousePosition()  # display Mouse position (X, Y) and RGB code (0, 0, 255)


# Keyboard Functions
pyautogui.typewrite('Hello World!\n')
# pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)  # useful for entering text, newline is Enter
pyautogui.typewrite(['enter'])
# pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=secs_between_keys)
# pyautogui.KEYBOARD_KEYS   # list of available keyboard keys on the current OS
# pyautogui.hotkey("command", "space")  # keyboard shortcuts
# pyautogui.hotkey('ctrl', 'c')  # ctrl-c to copy
# pyautogui.hotkey('ctrl', 'v')  # ctrl-v to paste
# pyautogui.keyDown(key_name)   # Button down
# pyautogui.keyUp(key_name)     # Button up
# pyautogui.press() # press a single key


# Screenshot Functions
# pyautogui.screenshot("/Users/hlin/Downloads/screenshot1.png") # screenshot with the file name and the location
# pyautogui.locateOnScreen("filename")  # look for picture (filename) on the screen; return (x, y, width, height)
# pyautogui.locateCenterOnScreen("filename") # locate the center of file/image on the screen
