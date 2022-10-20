from config_utils import *
import temtem_detector
import temtem_clicker

def catch(position:bool=True) -> bool: 
    '''
    Throw the temcard to target.

    Args:
        position : The position of temtem.
    Return:
        Temcard is finished or not.
    '''
    temtem_clicker.pic_Clicker(bag)

    if not temtem_clicker.pic_Clicker(E):
        send_message("沒卡了","Theere is no temcard")
        temtem_clicker.pic_Clicker(run)
        return True
        
    if temtem_clicker.pic_Clicker(temcard_plus):
        send_message("對temtem使用temcard+","Use temcard")
        if temtem_clicker.tem_detector(top) and temtem_clicker.tem_detector(down):
            temtem_clicker.tem_Clicker(position)

        return False
    else:
        send_message("沒卡了","Theere is no temcard")
        return True

def switch_tem(position:int) -> None: 
    """
    Switch the current temtem to another one in the bag.

    Args:
        position : The position of temtem in the bag
    """
    switch_position=[[400,224],[1260,344],[400,488],[1260,608],[400,757],[1260,878]]

    temtem_clicker.pic_Clicker(switch)

    if position==-1:
        for i in range(2,6):
            if temtem_detector.temtem_alive_in_bag(switch_position[i]):
                position=i
                break

    send_message(f"與第{position}個temtem交換",f"Switch to {position}th temtem")
    
    pyautogui.click(switch_position[position])

def leave_game() -> None: 
    '''
    Leave game in battle
    '''
    process=['esc','s','s','f','f']

    for i in process:
        pyautogui.press(i,1,0.5)

def buy_temcard():
    
    #use smoke_bomb
    send_message("打開背包並使用煙霧彈","Open the bag and use smoke bomb")
    
    pyautogui.press('i',1,0.5)
    temtem_clicker.pic_Clicker(E)
    temtem_clicker.pic_Clicker(smoke_bomb)
    pyautogui.press('f',2,0.5)
    temtem_detector.animation()
    pyautogui.press('x',1,0.5)
    pyautogui.click(928,1062,1,1,'right')
    temtem_detector.animation()
    pyautogui.sleep(1)

    #go to store
    send_message("跑去商店","go to store")

    pyautogui.click(928,1062,4,1,'right')
    pyautogui.click(151,927,1,1,'right')
    pyautogui.click(1054,1067,1,1,'right')
    pyautogui.click(928,1062,1,1,'right')
    pyautogui.click(5,650,8,1.5,'right')
    pyautogui.click(375,482,1,1,'right')
    temtem_detector.animation()
    pyautogui.sleep(1)
    
    #open stroe
    send_message("打開商店","open store")
    
    pyautogui.click(1458,244,button='right')
    pyautogui.sleep(1.5) 
    pyautogui.press('f',2,1)

    #buy carde
    send_message("買卡","buy card")

    pyautogui.press('s',4,0.5)
    pyautogui.press('f',1,0.5)
    pyautogui.press('a',2,0.5)
    pyautogui.press('f',1,0.5)
    pyautogui.press('esc',1,0.5)

    #leave store
    send_message("離開商店","leave store")

    pyautogui.click(0,1077,2,1,button='right')
    temtem_detector.animation()
    pyautogui.sleep(1)

    #go to castle
    send_message("回去城堡","go to castle")

    pyautogui.click(1883,622,8,1.5,'right')
    pyautogui.click(1275,314,1,1.5,'right')
    pyautogui.click(984,179,1,1.5,'right')
    pyautogui.click(1481,98,1,1.5,'right')
    pyautogui.click(970,61,2,1.5,'right')
    temtem_detector.animation()
    pyautogui.sleep(1)

    #go to room
    send_message("回到房間","go to room")
    
    pyautogui.click(960,207,1,1,'right')
    pyautogui.click(335,350,1,1,'right')
    pyautogui.click(178,471,1,1,'right')
    temtem_detector.animation()
    pyautogui.sleep(1)
    pyautogui.click(9,550,2,1,'right')
    pyautogui.press('x',1,0.5)

def heal_exp():

    #use smoke_bomb
    send_message("打開背包並使用煙霧彈","Open the bag and use smoke bomb")
    
    pyautogui.press('i',1,0.5)
    temtem_clicker.pic_Clicker(E)
    temtem_clicker.pic_Clicker(smoke_bomb)
    pyautogui.press('f',2,0.5)
    temtem_detector.animation()
    pyautogui.sleep(1)
    
    #heal
    pyautogui.click(761,549,1,0.5,'right')
    pyautogui.click(956,477,2,0.5)

    send_message("治療中","Healing")

    pyautogui.sleep(8)

    #go
    send_message("前往古墳","go to barrow")

    pyautogui.click(942,1063,2,1.5,'right')
    pyautogui.click(13,1067,1,1.5,'right')
    pyautogui.click(16,1059,1,1.5,'right')
    pyautogui.click(28,578,1,3,'right')
    pyautogui.click(67,445,1,1.5,'right')
    pyautogui.click(467,253,1,1.5,'right')
    temtem_detector.animation()
    pyautogui.sleep(1)
    pyautogui.click(752,12,2,5,'right')

def use_healcan():

    send_message('判斷隊伍temtem死亡數',"Detector the number of died temtem")

    if temtem_detector.temtems_alive()>=1:
        pyautogui.click(1860,240)
        if not temtem_clicker.detect_map():
            pyautogui.press('f',2,0.5)
            pyautogui.sleep(2)
            pyautogui.press('esc',1,0.5)
            return True

    return False

def open_radar():
    pyautogui.press('i',1,0.5)
    if temtem_detector.detector(radar_pic):
        pyautogui.press('f',2,0.5)
    else:
        return False
