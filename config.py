from dataclasses import dataclass
import pyautogui
import temtem_utils
import time
import threading
import keyboard
from pynput.keyboard import Listener, KeyCode
import json
import os


j=json.load(open(os.path.dirname(os.path.abspath(__file__))+'\\img\\config.json'))



cnt=0
cnt_f=1
cnt_c=0

direction=j['direction']

k=j['key_start']
k_exit=j['key_exit']