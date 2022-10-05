from config_utils import *

def detect_map()->bool:
    """
    Return : 
        Map is still on the screen or not.
    """
    return pyautogui.pixelMatchesColor(1790, 40,(60,232,234))

def tem_detector(position:bool,target:bool=True) -> bool:
    """
    Args :
        position : Click position. Top is True. Down is False.
        enemy : Click enemy or friend. Enemy is True. Friend is False
    Return :
        Target exists or not.
    """
    tem_position=[[(490,785),(80,730)],[(1700,141),(1190,86)]]

    return pyautogui.pixelMatchesColor(*tem_position[target][position],expectedRGBColor=(28,209,211))

def detector(pic_name:str) -> bool: 
    """
    Return the picture can be found on the screen or not

    Args:
        pic_name : The picture's name in the file.
    """
    return pyautogui.locateOnScreen(path+f"\\img\\{pic_name}.png",confidence=0.7) is not None

def tem_Clicker(position:bool=True,target:bool=True) -> None:
    """
    Click target.

    Args:
        position : Click position. Top is True. Down is False.
        target : Click enemy or friend. Enemy is True. Friend is False
    """
    tem_position=[[(490,785),(80,730)],[(1700,145),(1190,86)]]

    pyautogui.click(*tem_position[target][position],interval=0.5)
    pyautogui.sleep(0.5)
    
def pic_Clicker(pic_name:str,btn='left') -> None: 
    '''
    If the picture can be found on the screen, click the center of picture's position.\n

    Args:
        pic_name : The picture's name in the file.
        btn : Click by right or left button.
    Return:
        The picture can be found or not.
    '''
    print(f"按下{pic_name}按鈕")

    if detector(pic_name):
        pyautogui.click((pyautogui.locateCenterOnScreen(path+f"\\img\\{pic_name}.png",confidence=0.7)),button=btn,interval=0.8)
        pyautogui.sleep(0.3)
    else:
        try:
            if detector(pic_name+'_focus'):
                pyautogui.click((pyautogui.locateCenterOnScreen(path+f"\\img\\{pic_name}_focus.png",confidence=0.7)),button=btn,interval=0.8)
                pyautogui.sleep(0.3)
            else:
                return False
        except:
            return False

    return True

def tech_clicker(tech:int=1,position:bool=True,target:bool=True) -> None: 
    """
    Use the techniques to target which you select.\n
    Arg:
        tech: Technique's position
        position : Click position. Top is True. Down is False.
        target : Click enemy or friend. Enemy is True. Friend is False
    """
    target_str,position_str = (enemy_str,top_str) if target else (friend_str,down_str)
    tech_position=[[160,900],[460,900],[170,980],[470,980]]

    pyautogui.click(*tech_position[tech-1],interval=0.5)

    position = position if tem_detector(position) else not position

    print(f"對{target_str}{position_str}的temtem使用第{tech}個技能")

    tem_Clicker(position,target)

def catch(position:bool=True) -> bool: 
    '''
    Throw the temcard to target.

    Args:
        position : The position of temtem.
    Return:
        Temcard is finished or not.
    '''
    pic_Clicker(bag)
    if not pic_Clicker(E):
        print("沒卡了")
        pic_Clicker(run)
        return True
    if pic_Clicker(temcard_plus):

        print(f"對temtem使用temcard+")

        if tem_detector(top) and tem_detector(down):
            tem_Clicker(position)

        return False
    else:
        print("沒卡了")
        return True

def switch_tem(position:int) -> None: 
    """
    Switch the current temtem to another one in the bag.

    Args:
        position : The position of temtem in the bag
    """
    switch_position=[[0,0],[1105,360],[410,519],[1272,640],[410,788],[1272,904]]

    pic_Clicker(switch)

    if position==-1:
        for i in range(1,6):
            if temtem_alive_in_bag(switch_position[i]):
                position=i
                break

    print(f"與第{position}個temtem交換")
    
    pyautogui.click(switch_position[position])

def catch_animation() -> int: 
    '''
    Waiting for catch animation until it ends and release it.\n
    It works by detecting the map and run button.\n

    Return:
        The number of temtem caught.
    ''' 
    num=0
    print("等待捕捉動畫")
    while 1:
        if detector(run):
            return num
        elif detect_map():
            print('戰鬥結束')
            return num
        elif detector(yes) or detector(yes+'_focus'):
            pic_Clicker(yes)
            print("成功放生")
            num=num+1
            continue
        elif detector(release):
            pic_Clicker(release)
            continue

def animation() -> bool:
    '''
    Waiting for animation until it ends.\n
    It works by detecting the map and run button.
    ''' 
    print('等待動畫')
    while 1:
        if detector(run):
            return True
        if detect_map():
            print('動畫結束')
            return False
        if detector('esc'):
            pic_Clicker('esc','right')

def temtem_alive_in_bag(position) -> int: 
    """
    Args:
        position : the position of temtem in bag 

    Return: 
        Temtem in the current position is alive or not
    """
    if pyautogui.pixelMatchesColor(*position,(28,209,211)):
        return True

    return False

def temtems_alive() -> bool:
    '''
        If the bar of temtem's HP is in the lower right of main screen whose color equal to RGB (106, 38, 46), the temtem is dead.\n
        The first bar exists in x=1432 and y=1036, and each bar have 80 bits intervals.

        Return: 
            numbers of dead Temtems 
    '''
    cnt=0
    for i in range(0,6):
        if pyautogui.pixelMatchesColor(1432+(80*i),1036,(106, 38, 46)):
            cnt=cnt+1
    return cnt

def leave_game() -> None: 
    '''
    Leave game in battle
    '''
    process=['esc','s','s','f','f']

    for i in process:
        pyautogui.press(i,1,0.5)

def buy_temcard():
    
    #use smoke_bomb
    print("打開背包並使用煙霧彈")
    pyautogui.press('i',1,0.5)
    pic_Clicker(E)
    pic_Clicker(smoke_bomb)
    pyautogui.press('f',2,0.5)
    animation()
    pyautogui.press('x',1,0.5)
    pyautogui.click(928,1062,1,1,'right')
    animation()
    pyautogui.sleep(1)

    #go to store
    print("跑去商店")
    pyautogui.click(928,1062,4,1,'right')
    pyautogui.click(151,927,1,1,'right')
    pyautogui.click(1054,1067,1,1,'right')
    pyautogui.click(928,1062,1,1,'right')
    pyautogui.click(5,650,8,1.5,'right')
    pyautogui.click(375,482,1,1,'right')
    animation()
    pyautogui.sleep(1)

    #open stroe
    print("打開商店")
    pyautogui.click(1458,244,button='right')
    pyautogui.sleep(1.5) 
    pyautogui.press('f',2,0.5)

    #buy carde
    print("買卡")
    pyautogui.press('s',4,0.5)
    pyautogui.press('f',1,0.5)
    pyautogui.press('a',2,0.5)
    pyautogui.press('f',1,0.5)
    pyautogui.press('esc',1,0.5)

    #leave store
    print("離開商店")
    pyautogui.click(0,1077,2,1,button='right')
    animation()
    pyautogui.sleep(1)

    #go to castle
    print("回去城堡")
    pyautogui.click(1883,622,8,1.5,'right')
    pyautogui.click(1275,314,1,1.5,'right')
    pyautogui.click(984,179,1,1.5,'right')
    pyautogui.click(1481,98,1,1.5,'right')
    pyautogui.click(970,61,2,1.5,'right')
    animation()
    pyautogui.sleep(1)

    #go to room
    print("回到房間")
    pyautogui.click(960,207,1,1,'right')
    pyautogui.click(335,350,1,1,'right')
    pyautogui.click(178,471,1,1,'right')
    animation()
    pyautogui.sleep(1)
    pyautogui.click(9,550,2,1,'right')

def heal_exp():
    #use smoke_bomb
    
    print("打開背包並使用煙霧彈")
    pyautogui.press('i',1,0.5)
    pic_Clicker(E)
    pic_Clicker(smoke_bomb)
    pyautogui.press('f',2,0.5)
    animation()
    pyautogui.sleep(1)
    
    #heal
    pyautogui.click(761,549,1,0.5,'right')
    pyautogui.click(956,477,2,0.5)
    print("治療中")
    pyautogui.sleep(8)

    #go
    print("前往格鬥神廟")
    pyautogui.click(942,1063,2,1.5,'right')
    pyautogui.click(13,1067,1,1.5,'right')
    pyautogui.click(16,1059,1,1.5,'right')
    pyautogui.click(28,578,1,3,'right')
    pyautogui.click(67,445,1,1.5,'right')
    pyautogui.click(467,253,1,1.5,'right')
    animation()
    pyautogui.sleep(1)
    pyautogui.click(752,22,2,5,'right')
       
def weekly_release() -> None:
    '''
    Release the Hazrat in Braeside Castle weekly.
    Need Oceara, Momo, Barnshe in bag slot 1,2,3.
    if there is no temcard in the bag, it will use one smoke_bomb to buy.
    '''
    turn_cnt=1
    flag_temcard=False
    global cnt_c
        
    animation()
    print("判斷是否有色違中")
    if detector(luma):
        leave_game()
        print("關閉遊戲")
        return False
    
    while 1:
        print(f"第{turn_cnt}回合開始")
        if turn_cnt==1:
            tech_clicker()
            switch_tem(2)
        elif turn_cnt==2:
            pic_Clicker(rest)
            tech_clicker()
        elif turn_cnt==3:
            flag_temcard=catch()
            flag_temcard=catch()
            if not flag_temcard:
                cnt_c=cnt_c+catch_animation()
        else:
            pic_Clicker(run)
            pic_Clicker(run)

        if animation():
            print(f"第{turn_cnt}回合結束")
            turn_cnt=turn_cnt+1
        else:
            print(f"目前捕捉了{cnt_c}隻")
            break

    if flag_temcard:
        buy_temcard()
        return True
    
    if cnt_c<200:
        return True
    else:
        return False
        
def luma_finding() -> None:

    animation()

    print("判斷是否有色違中")
    if detector(luma):
        leave_game()
        print("關閉遊戲")
        return False
    else:
        pic_Clicker(run)    
        pic_Clicker(run)

    animation()
    return True

def exp_training() -> None:
   
    animation()

    turn_cnt=1
    
    print("判斷是否有色違中")
    if detector(luma):
        leave_game()
        print("關閉遊戲")
        return False

    while 1:
        if turn_cnt==1:
            if tem_detector(top):
                tech_clicker(1,down,False)
                switch_tem(-1)
            else:
                tech_clicker()
                pic_Clicker(rest)
        else:
            pic_Clicker(run)
            pic_Clicker(run)

        if animation():
            turn_cnt=turn_cnt+1
        else:
            break

    animation()

    print('判斷隊伍temtem死亡數')
    if temtems_alive()>=4:
        pic_Clicker('can')
        if not detect_map():
            pyautogui.press('f',2,0.5)
            pyautogui.sleep(2)
            pyautogui.press('esc',1,0.5)
        else:
            heal_exp()
    return True

def radar():

    animation()
    
    print("判斷是否有色違中")
    if detector(luma):
        leave_game()
        print("關閉遊戲")
        return False
    else:
        tech_clicker(1)
        tech_clicker(1)

    animation()
    return True    
