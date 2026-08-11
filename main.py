#код Фролова
from time import time, sleep
import threading, sys
from questions import questions
from test import *

score = 0
name = input("Введите ваше имя: ")
end = False

def start():
    start_time = time()
    print(f'{name}, У вас есть 60 секунд на прохождение теста')
    while not end:
        current_time = time()
        process_time = current_time - start_time
        print(f'{name}, прошло {int(process_time)} секунд')
        sleep(5)
    
        if process_time > 60:
            print("Время закончилось")
            break
        
threading.Thread(target=start, daemon=True).start()

for i in questions:
    score += testing(i)
    if round(time()-start) > 60:
        sys.exit()

print(f"{name}\nВремя прохождения теста: {round(time()-start) сек\nНабранно баллов: {score}\n{get_result(score)}")

