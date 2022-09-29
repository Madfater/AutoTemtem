import pyautogui
import keyboard
import asyncio
import Autotemtem


direction=['a','d']
run=False
key='p'
key_exit='esc'
kill_switch = True

async def randomlly_walk():
    cnt=0
    global run
    while run:
        pyautogui.keyDown(direction[cnt])
        pyautogui.keyUp(direction[cnt])
        cnt=(cnt+1)%2
        await asyncio.sleep(0.05)
    else:
        for i in direction:
            pyautogui.keyUp(i)

async def activator():
    global run,kill_switch
    while kill_switch:
        if keyboard.is_pressed(key_exit):
            kill_switch=False
        if keyboard.is_pressed(key):
            run = not run
            if run:
                print('開始奔跑')
            else:
                print('暫停奔跑')
            if run:
                loop.create_task(randomlly_walk())
            while keyboard.is_pressed(key):
                await asyncio.sleep(0.01)
        await asyncio.sleep(0.01)

async def fight_detector():
    global run
    global kill_switch
    cnt=1
    while kill_switch:
        if not (pyautogui.pixelMatchesColor(1790, 40,(60,232,234))):

            print('停止奔跑')
            print(f'開啟第{cnt}輪戰鬥')

            for i in direction:
                pyautogui.keyUp(i)

            kill_switch=Autotemtem.luma_finding()
            
            if cnt>=1000:
                kill_switch=False
            
            print('開始奔跑')
            cnt=cnt+1
        await asyncio.sleep(0.01)


if __name__=='__main__':

    loop = asyncio.get_event_loop()
    loop.create_task(fight_detector())
    loop.run_until_complete(activator())
    for i in direction:
            pyautogui.keyUp(i)