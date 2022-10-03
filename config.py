from dataclasses import dataclass
import pyautogui
import temtem_utils
import time
import threading
import keyboard
from pynput.keyboard import Listener, KeyCode
  
cnt=0
cnt_f=1
cnt_c=0

direction=['a','s','d','w']

k='e'
k_exit='r'