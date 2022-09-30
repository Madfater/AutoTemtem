import threading
import time
def func(i):
    while True:
        print(i)
        time.sleep(1)
threads:list[threading.Thread]=[]
for i in range(5):
    temp = threading.Thread(target=func,args=(i,))
    threads.append(temp)
for i in threads:
    i.start()
while True:
    pass