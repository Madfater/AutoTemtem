from config import *
from string import *

@dataclass
class data():
    running:bool
    program_running:bool
  
class keyboard_Script(threading.Thread):
    '''
    A class for controlling the role in the game by auto-pressing keyboard
    '''
    def __init__(self,flags):
        super(keyboard_Script, self).__init__()
        self.flag:data = flags

    def run(self):
        global cnt
        flag_released=False
        while self.flag.program_running:
            while self.flag.running and self.flag.program_running:
                pyautogui.keyDown(direction[(cnt+1)%len(direction)])
                pyautogui.keyUp(direction[cnt%len(direction)])
                cnt=cnt+1
                flag_released=True
            else:
                if flag_released:
                    for i in direction:
                        pyautogui.keyUp(i)
                    flag_released=False
            time.sleep(0.01)

class fight_detector(threading.Thread):
    """
    A class for dectecting fight or not.

    Args:
        mode : 
            1 : Luma finding.\n
            2 : Auto level training.\n
            3 : Release the Hazrat in Braeside Castle weekly
    """
    
    def __init__(self,flags,mode):
        super(fight_detector,self).__init__()
        self.flag:data=flags
        self.mode=mode

    def fight(self):
        global cnt_f
        modes=[temtem_utils.luma_finding,temtem_utils.exp_training,temtem_utils.weekly_release,temtem_utils.radar]
        if not (pyautogui.pixelMatchesColor(1790, 40,(60,232,234))):
            if Lang=='zh-TW':
                print(f"開始第{cnt_f}次戰鬥")
            else:
                print(f"start the {cnt_f}th fight")
            self.flag.running=False
            self.flag.program_running=modes[self.mode-1]()
            self.flag.running=True
            cnt_f=cnt_f+1

    def run(self):
        while self.flag.program_running:
            self.fight()
        
class keyboard_detector():
    '''
    A class for listening the key start, pause or exit

    Args:
        key : the key to stop or start this script.
        key_exit : the key to close this script.\n
    '''
    def __init__(self,flags,key,key_exit):
        self.flag:data=flags
        self.key=key
        self.key_exit=key_exit
        self.listener=None

    def on_press(self,key):
        if key == self.key:
            if self.flag.running:
                if Lang=='zh-TW':
                    print('暫停')
                else:
                    print('pause')
                self.flag.running=False
            else:
                if Lang=='zh-TW':
                    print("開始")
                else:
                    print("start")
                self.flag.running=True
    
        if key == self.key_exit:
            if Lang=='zh-TW':
                print('離開')
            else:
                print('close the bot')
            self.flag.program_running=False
            exit()

    def stop(self):
        self.listener.stop()

    def run(self):
        self.listener=Listener(on_press=self.on_press)
        self.listener.start()

class AutoTemtem():
    '''
    A script for temtem.
    
    Args:
        key : the key to stop or start this script.
        key_exit : the key to close this script.\n
        mode : 
            1 : Luma finding.\n
            2 : Auto level training.\n
            3 : Release the Hazrat in Braeside Castle weekly.\n

    '''

    def __init__(self,key,key_exit,mode=0):
        self.flag=data(False,True)
        self.script = keyboard_Script(self.flag)
        self.fight = fight_detector(self.flag,mode)
        self.keyboard = keyboard_detector(self.flag,KeyCode(char=f"{key}"),KeyCode(char=f"{key_exit}"))

    def start(self):
        self.fight.start()
        self.script.start()
        self.keyboard.run()

        self.fight.join()
        self.script.join()
        self.keyboard.stop()

if __name__=='__main__':
    if Lang=='zh-TW':
        mode=int(input("1.色違尋找模式\n2.自動練等模式\n3.每周釋放\n4.雷達模式\n5.測試補卡功能\n請選擇模式:"))
    else:
        mode=int(input("1.luma hunt\n2.Auto leveling\n3.Weekly release\n4.radar\n5.test buy temcard\nPlease select the mode:"))
    if mode ==5:
        if Lang=='zh-TW':
            print("請按e開始")
        else:
            print("Please press e to start")
        keyboard.wait('e')
        temtem_utils.buy_temcard()
    elif mode<4:
        AutoTemtem(k,k_exit,mode).start()
    else:
        if Lang=='zh-TW':
            print("錯誤")
        else:
            print("Error")