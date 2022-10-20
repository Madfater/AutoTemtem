from config_utils import *
import temtem_detector

def tem_Clicker(position:bool=True,target:bool=True) -> None:
    """
    Click target.

    Args:
        position : Click position. Top is True. Down is False.
        target : Click enemy or friend. Enemy is True. Friend is False
    """
    tem_position=[[(490,785),(80,730)],[(1700,145),(1190,86)]]

    pyautogui.click(*tem_position[target][position],interval=0.5)
    
def pic_Clicker(pic_name:str,btn='left') -> None: 
    '''
    If the picture can be found on the screen, click the center of picture's position.\n

    Args:
        pic_name : The picture's name in the file.
        btn : Click by right or left button.
    Return:
        The picture can be found or not.
    '''
    send_message(f"按下{pic_name}按鈕",f'press {pic_name} button')

    if temtem_detector.detector(pic_name):

        if pyautogui.click((pyautogui.locateCenterOnScreen(path+f"{pic_name}.png",confidence=0.7,grayscale=True)),button=btn,interval=0.8):
            return True
        elif os.path.isfile(f"{pic_name}_focus.png"):
            return pyautogui.click((pyautogui.locateCenterOnScreen(path+f"{pic_name}_focus.png",confidence=0.7)),button=btn,interval=0.8) is not None
        else:
            return False


def tech_clicker(tech:int=1,position:bool=True,target:bool=True) -> None: 
    """
    Use the techniques to target which you select.\n
    Arg:
        tech: Technique's position
        position : Click position. Top is True. Down is False.
        target : Click enemy or friend. Enemy is True. Friend is False
    """
    tech_position=[[160,900],[460,900],[170,980],[470,980]]

    pyautogui.click(*tech_position[tech-1],interval=0.5)

    position = position if temtem_detector.tem_detector(position) else not position

    send_message(f"使用第{tech}個技能",f"Use the technique in {tech}th slot")

    tem_Clicker(position,target)