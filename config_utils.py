import os
import pyautogui
import time
import keyboard
import json


bag='bag'
buy='buy'

cnt_c=0

down=False

E='E'
enemy=True

friend=False

Lang=json.load(open(os.path.dirname(os.path.abspath(__file__))+'\config.json'))["Language"]

luma='luma'

radar_pic='radar'
radar_onscreen='radar_on_screen'
radar_onscreen2='radar_on_screen2'
radar_onscreen3='radar_on_screen3'
reconnect='reconnect'
run='run'
rest='rest'
release='release'

switch='switch'

top=True
temcard_plus='temcard_plus'

path=os.path.dirname(os.path.abspath(__file__))+f'\\img\\{Lang}\\'

smoke_bomb='smoke_bomb'

yes='yes'
yes2='yes2'

def send_message(zh,en):
    if Lang=='zh-TW':
        print(zh)
    else :
        print(en)