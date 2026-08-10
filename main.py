#код Фролова и Климова
from time import time, sleep
import threading
from questions import questions
from test import *

score = 0
name = input("Введите ваше имя: ")
end = False

def start():
    print(name + 'У вас есть 60 секунд на прохождение теста')
    while not end:
        current_time = time.time()
        process_time = current_time - start_time
        print(f'{name}, прошло {process_time:.2f} секунд')
        time.sleep(5)
    
        if process_time > 60:
            print("Время закончилось")
            raise SystemExit()
        
threading.Thread(target=start, daemon=True)

for i in questions:
    score += testing(i)

print(f"{name}\nВремя прохождения теста: {round(time()-start)} сек\nНабранно баллов: {score}\n{get_result(score)}")

