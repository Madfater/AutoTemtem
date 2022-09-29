import pyautogui
import keyboard
import os

def getlocate():
    x,y=pyautogui.position()
    print(f"x={x}\ny={y}")

def getcolor():
    x,y=pyautogui.position()
    r,g,b=pyautogui.pixel(x,y)
    print(f'r=={r} and g=={g} and b=={b}')

if __name__=='__main__':
    keyboard.add_hotkey('1',getlocate)
    keyboard.add_hotkey('2',getcolor)
    keyboard.wait()
