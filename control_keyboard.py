import pyautogui
import time 
import pyperclip

position = pyautogui.position()
print(position)

pyautogui.click(125, 508)
time.sleep(1)
pyautogui.click(450, 527, duration=1)
pyautogui.press('down')
pyautogui.press('enter')

#pyautogui.write("One!")

#copy and paste code
pyautogui.hotkey('command','a')
pyautogui.hotkey('command','c')
text = pyperclip.paste()
#pyautogui.alert(text) #alert does not work, something is depricated
print(text)
pyautogui.press('down')
pyautogui.hotkey('command','v')
pyautogui.hotkey('command','s')

#access text from clipboard
