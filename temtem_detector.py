from config_utils import *
import warnings

def map_detector()->bool:
    """
    Return : 
        Map is still on the screen or not.
    """
    return pyautogui.pixelMatchesColor(1790, 40,(60,232,234))

def luma_detector()->bool:
    """
    Return : 
        Map is still on the screen or not.
    """
    send_message("判斷是否有色違","Detector luma exists")

    cnt = 0
    for i in pyautogui.locateAllOnScreen(path+f"{luma}.png",confidence=0.7,region=(1200,20,800,180)):
        cnt+=1
    return cnt>0

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
    if pyautogui.locateOnScreen(path+f"{pic_name}.png",confidence=0.7,grayscale=True) is not None:
        return True
    else:
        if os.path.isfile(f"{pic_name}_focus.png"):
            return pyautogui.locateOnScreen(path+f"{pic_name}_focus.png",confidence=0.7,grayscale=True) is not None
        else:
            return False
     
def catch_animation() -> int: 
    '''
    Waiting for catch animation until it ends and release it.\n
    It works by detecting the map and run button.\n

    Return:
        The number of temtem caught.
    ''' 
    num=0

    send_message("等待捕捉動畫","waiting catch anmation")
    
    while 1:
        if detector(run):
            send_message("動畫結束","anmation end")
            return num
        elif map_detector():
            send_message("動畫結束","anmation end")
            return num
        elif detector(yes):
            pyautogui.click(850,650)
            num=num+1
            continue
        elif detector(release):
            pyautogui.click(1030,780)
            continue

def animation() -> bool:
    '''
    Waiting for animation until it ends.\n
    It works by detecting the map and run button.
    ''' 
    send_message("等待動畫","waiting anmation")
 
    while 1:
        if detector(run):
            return True
        if map_detector():
            send_message("動畫結束","anmation end")
            return False
        if detector('esc'):
            pyautogui.press('esc',2,0.5)

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

def radar_detector():
    
    send_message('判斷隊伍radar',"Detector the radar")
    if pyautogui.pixelMatchesColor(1530,1000,(220,77,114)):
        pyautogui.click(1530,1000)
        return False
    return True
