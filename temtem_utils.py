from config_utils import *
import temtem_detector
import temtem_clicker
import temtem_action

def weekly_release() -> None:
    '''
    Release the Hazrat in Braeside Castle weekly.
    Need Oceara, Momo, Barnshe in bag slot 1,2,3.
    if there is no temcard in the bag, it will use one smoke_bomb to buy.
    '''
    turn_cnt=1
    flag_temcard=False
    global cnt_c
        
    temtem_detector.animation()

    if temtem_detector.luma_detector():
        temtem_action.leave_game()
        return False
    
    while 1:
        send_message(f"第{turn_cnt}回合開始",f"{turn_cnt}th turn start")
        
        if turn_cnt==1:
            temtem_clicker.tech_clicker()
            temtem_action.switch_tem(2)
        elif turn_cnt==2:
            temtem_clicker.pic_Clicker(rest)
            temtem_clicker.tech_clicker()
        elif turn_cnt==3:
            flag_temcard=temtem_action.catch()
            flag_temcard=temtem_action.catch()
            if not flag_temcard:
                cnt_c=cnt_c+temtem_detector.catch_animation()
        else:
            temtem_clicker.pic_Clicker(run)
            temtem_clicker.pic_Clicker(run)

        if temtem_detector.animation():
            send_message(f"第{turn_cnt}回合結束",f"{turn_cnt}th turn end")
            turn_cnt=turn_cnt+1
        else:
            send_message(f"目前捕捉了{cnt_c}隻",f"Catch {cnt_c} temtem in total")
            break

    temtem_action.use_healcan()

    if flag_temcard:
        temtem_action.buy_temcard()
        return True
    
    if cnt_c<200:
        return True
    else:
        return False
        
def luma_finding() -> None:

    temtem_detector.animation()

    if temtem_detector.luma_detector():
        temtem_action.leave_game()
        return False
    else:
        temtem_clicker.pic_Clicker(run)    
        temtem_clicker.pic_Clicker(run)

    temtem_detector.animation()

    return True

def exp_training() -> None:
   
    temtem_detector.animation()

    turn_cnt=1

    if temtem_detector.luma_detector():
        temtem_action.leave_game()
        return False

    while 1:
        if turn_cnt==1:
            if temtem_clicker.tem_detector(top):
                temtem_clicker.tech_clicker(1,down,False)
                temtem_action.switch_tem(-1)
            else:
                temtem_clicker.tech_clicker()
                temtem_clicker.pic_Clicker(rest)
        else:
            temtem_clicker.pic_Clicker(run)
            temtem_clicker.pic_Clicker(run)

        if temtem_detector.animation():
            turn_cnt=turn_cnt+1
        else:
            break

        if not temtem_action.use_healcan():
            temtem_action.heal_exp()
    return True

def radar():

    turn_cnt=1
    temtem_detector.animation()

    if temtem_detector.luma_detector():
        temtem_action.leave_game()
        return False
    
    while 1:
        send_message(f"第{turn_cnt}回合開始",f"{turn_cnt}th turn start")
        if turn_cnt==1:
            temtem_clicker.tech_clicker()
            temtem_clicker.tech_clicker()
        else:
            temtem_clicker.tech_clicker()
            temtem_clicker.tech_clicker()

        if temtem_detector.animation():
            send_message(f"第{turn_cnt}回合結束",f"{turn_cnt}th turn end")
            turn_cnt=turn_cnt+1
        else:
            break
        
    if not temtem_detector.radar_detector():
        temtem_action.open_radar()
    
    temtem_action.use_healcan()

    pyautogui.click(10,10)
    
    return True
