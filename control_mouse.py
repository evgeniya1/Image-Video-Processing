import pyautogui

position = pyautogui.position()
print(position)
# pyautogui.moveTo(131,607, duration=1)
# pyautogui.move(100, 0, duration=1)

#pyautogui.click(clicks=2)
#pyautogui.doubleClick()

# #click to specific location
# pyautogui.click(131,607, clicks=2)

##right click on windows
#pyautogui.click(131,607,button='right')

# ##right click on mac
# pyautogui.click(131,607)
# pyautogui.dragTo(131,607,button='right')

#draw using: https://jspaint.app/#local:1cf34024529e6

pyautogui.click(1035,500, clicks=2)
pyautogui.drag(150,0,duration=1,button='left')
pyautogui.drag(0,-150,duration=1,button='left')
pyautogui.drag(-150,0,duration=1,button='left')
pyautogui.drag(0,150,duration=1,button='left')


