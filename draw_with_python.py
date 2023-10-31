import pyautogui
from mss import mss, tools

#open on the right: https://jspaint.app/#local:1cf34024529e6

print(pyautogui.position())
dur = 0.1
pyautogui.moveTo(1218, 355, duration=1)
pyautogui.click()
pyautogui.drag(0,200, duration=dur, button='left')
pyautogui.drag(60,0, duration=dur, button='left')
pyautogui.drag(0,-3, duration=dur, button='left')
pyautogui.drag(0,6, duration=dur, button='left')
pyautogui.drag(60,0, duration=dur, button='left')
pyautogui.drag(0,-6, duration=dur, button='left')
pyautogui.drag(-60,0, duration=dur, button='left')

pyautogui.move(60,0, duration=dur)
pyautogui.move(0,3, duration=dur)


pyautogui.drag(100,0, duration=dur, button='left')
pyautogui.drag(0,-120, duration=dur, button='left')

pyautogui.move(0,-40, duration=dur)
pyautogui.drag(0,-40, duration=dur, button='left')

pyautogui.drag(-220,0, duration=dur, button='left')

pyautogui.move(-50,-50, duration=dur)

with mss() as screen:
    part = {'top':345, 'left':1208, 'width':240, 'height':220}
    image = screen.grab(part)
    tools.to_png(image.rgb, image.size, output='draw_with_python.png')