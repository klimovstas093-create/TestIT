#Должен был быть код Кроткова Льва
from time import time, sleed
from questions import questions
from test import *

start = time()
score = 0
name = input("Введите ваше имя:")

for i in questions:
    score += testing(i)

print(f"{name}\nВремя прохождения теста: {round(start-time())} сек\nНабранно баллов: {score}\n{get_result(score)}")

sleep(10000)
