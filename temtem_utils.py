from config_utils import *

def tem_detector(position:bool,target:bool=True) -> bool: #回傳該位置temtem是否存在

    tem_position=[[(490,785),(80,730)],[(1700,141),(1190,86)]]

    return pyautogui.pixelMatchesColor(*tem_position[target][position],expectedRGBColor=(28,209,211))

def detector(pic_name:str) -> bool: #回傳該圖片是否存在在畫面
    
    return pyautogui.locateOnScreen(path+f"\\img\\{pic_name}.png",confidence=0.7) is not None

def tem_Clicker(position:bool,target:bool=True) -> None: #點擊該位置temtem

    tem_position=[[(490,785),(80,730)],[(1700,145),(1190,86)]]

    pyautogui.click(*tem_position[target][position])

    time.sleep(0.5)
        
def btn_Clicker(pic_name:str) -> None: #點擊該位置按鈕

    print(f"按下{pic_name}按鈕")

    if detector(pic_name):
        pyautogui.click((pyautogui.locateCenterOnScreen(path+f"\\img\\{pic_name}.png",confidence=0.7)),button='left')
    elif detector(pic_name+'_mouseon'):
        pyautogui.click((pyautogui.locateCenterOnScreen(path+f"\\img\\{pic_name}_mouseon.png",confidence=0.7)),button='left')

    time.sleep(0.5)

def tech_clicker(tech:int,position:bool=True,target:bool=True) -> None: #點擊所選技能於該位置temtem上

    target_str,position_str = (enemy_str,top_str) if target else (friend_str,down_str)
    tech_position=[[160,900],[460,900],[170,980],[470,980]]

    pyautogui.click(*tech_position[tech-1])
    
    time.sleep(0.5)

    position = position if tem_detector(position) else not position

    print(f"對{target_str}{position_str}的temtem使用第{tech}個技能")

    tem_Clicker(position,target)

def catch(position:bool=True) -> None: #捕捉該位置temtem

    process=[bag,catch_obj,temcard_plus]

    for i in process:
        btn_Clicker(i)

    position = position if tem_detector(position) else not position

    print(f"對{target_str}{position_str}的temtem使用temcard+")

    tem_Clicker(position)

def switch_tem(position:int) -> None: #交換temtem

    switch_position=[[0,0],[1105,360],[410,519],[1272,640],[410,788],[1272,904]]

    btn_Clicker(switch)

    if position==-1:
        position=temtem_alive()

    print(f"與第{position}個temtem交換")
    
    pyautogui.click(*switch_position[position])

def catch_animation() -> int: #等待捕捉動畫並回傳捕捉數量

    print("等待捕捉動畫")
    while 1:
        if btn_Clicker(release):
            if btn_Clicker(yes):
                print("成功放生")
                return 1+catch_animation()
        if detector(run):
            return 0
        if pyautogui.pixelMatchesColor(1790, 40,(60,232,234)):
            print('戰鬥結束')
            return 0

def animation() -> bool: #等待過場動畫

    print('等待動畫')
    while 1:
        if detector(run):
            return True
        if pyautogui.pixelMatchesColor(1790, 40,(60,232,234)):
            print('戰鬥結束')
            return False

def temtem_alive() -> int: #回傳存活temtem的位置(最近) p.s.需打開背包

    position=[[410,519],[1272,640],[410,788],[1272,904]]

    for i,pos in enumerate(position):
        if pyautogui.pixelMatchesColor(pos[0],pos[1],(28,209,211)):
            return i+2

    return 0

def leave_game() -> None: #離開遊戲 p.s.戰鬥中

    process=['esc','s','s','f','f']

    for i in process:
        pyautogui.press(i)
        time.sleep(0.1)

def weekly_release() -> None:

    turn_cnt=1
        
    animation()
    
    while 1:
        print(f"第{turn_cnt}回合開始")
        if turn_cnt==1:
            tech_clicker(1)
            switch_tem(2)
        elif turn_cnt==2:
            btn_Clicker(rest)
            tech_clicker(4)
        elif turn_cnt==3:
            catch()
            catch()
            catch_animation()
        else:
            btn_Clicker(run)
            btn_Clicker(run)

        if animation():
            print(f"第{turn_cnt}結束")
            turn_cnt=turn_cnt+1
        else:
            break

def luma_finding() -> None:

    animation()

    if detector(luma):
        leave_game()
        return False
    else:
        btn_Clicker(run)    
        btn_Clicker(run)

    animation()
    return True
    
def exp_training() -> None:
   
    animation()

    if tem_detector(top):
        tech_clicker(1,down,False)
        switch_tem(-1)
    else:
        tech_clicker(1)
        tech_clicker(1)

    animation()
