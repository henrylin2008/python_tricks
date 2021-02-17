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
# pyautogui.locateOnScreen("image", greyscale=True)
# Returns (left, top, width, height) coordinate of first found instance of the image on the screen; Raises I
# mageNotFoundException if not found on the screen.
# greyscale=True; locate functions to give a slight speedup (about 30%-ish).

# pyautogui.locateCenterOnScreen("image") # locate the center of file/image on the screen; Raises
                                          # ImageNotFoundException if not found on the screen.
# pyautogui.locateAllOnScreen(): function will return a generator for all the locations it is found on the screen
pyautogui.screenshot(region=(0, 0, 300, 400))  # region=(left, top, width, height)
pyautogui.screenshot().getpixel((100, 200))    # (130, 135, 144), RGB color of a pixel in a screenshot
pyautogui.pixelMatchesColor(100, 200, (130, 135, 144))  # True; verify a single pixel matches a given pixel
pyautogui.pixelMatchesColor(100, 200, (140, 125, 134), tolerance=10)    # True;
# tolerance keyword argument specifies how much each of the red, green, and blue values can vary while still matching


# Message Box functions
pyautogui.alert(text='', title='', button='OK')
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])  # text display on the screen; title of the window;
pyautogui.prompt(text='text', title='title', default='sweet')  # 'little mango'; default = default text
pyautogui.password(text='password', title='window', default='pw123', mask='*')
# text: text display on the screen; title: window title; default password; mask: * as characters
