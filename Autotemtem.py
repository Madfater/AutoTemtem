from dataclasses import dataclass
import pyautogui
import temtem_utils
import time
import threading
from pynput.keyboard import Listener, KeyCode
  

direction=['a','s','d','w']
cnt=0
start_stop_key = KeyCode(char='e')
stop_key = KeyCode(char='r')

@dataclass
class data():
    running:bool
    program_running:bool
  
class keyboard_Script(threading.Thread):
    
    def __init__(self,flags):
        super(keyboard_Script, self).__init__()
        self.flag:data = flags
  
    def run(self):
        global cnt
        flag_released=False
        while self.flag.program_running:
            while self.flag.running:
                pyautogui.keyDown(direction[(cnt+1)%4])
                pyautogui.keyUp(direction[cnt%4])
                cnt=cnt+1
                flag_released=True
            else:
                if flag_released:
                    for i in direction:
                        pyautogui.keyUp(i)
                    flag_released=False
            time.sleep(0.01)

    
class detector(threading.Thread):
    
    def __init__(self,flags):
        super(detector,self).__init__()
        self.flag:data=flags

    def fight(self):
        cnt_f=1
        if not (pyautogui.pixelMatchesColor(1790, 40,(60,232,234))):
            print(f"開始第{cnt_f}次戰鬥")
            self.flag.running=False
            self.flag.program_running=temtem_utils.luma_finding()
            self.flag.running=True
            cnt_f=cnt_f+1
    
    def run(self):
        while self.flag.program_running:
            self.fight()

class AutoTemtem():
    def __init__(self):
        self.flag=data(False,True)
        self.script = keyboard_Script(self.flag)
        self.fight_detector = detector(self.flag)
        self.script.start()
        self.fight_detector.start()
        self.listener:Listener=None

    def on_press(self,key):
        if key == start_stop_key:
            if self.flag.running:
                print("暫停")
                self.flag.running=False
            else:
                print("開始")
                self.flag.running=True
    
        elif key == stop_key:
            print("關閉腳本")
            self.flag.program_running=False
            self.listener.stop()
    
    def run(self):
        with Listener(on_press=self.on_press) as self.listener:
            self.listener.join()

if __name__=='__main__':
    AutoTemtem().run()