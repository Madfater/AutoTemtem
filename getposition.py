import pyautogui
import keyboard

while False:
    keyboard.wait('esc')
    p=pyautogui.position()
    print(p)
    print(pyautogui.pixel(*p))
