#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


def game_core_v3(number):
    '''Деление массива чисел пополам, 
       затем в зависимости от того, больше или меньше загаданное число,
       продолжение поиска в нужной половине массива.
       Функция принимает загаданное число и возвращает число попыток.'''
    
    count = 0    # счётчик попыток
    num_1 = 1    # начало диапазона поиска
    num_2 = 100    # конец диапазона поиска
    
    while True:
        count+=1
        predict = int((num_1+num_2)/2)
        
        if number > predict: 
            num_1 = predict+1
        elif number < predict: 
            num_2 = predict-1
        else: 
            break            
    return(count) # выход из цикла, если число угадано

    
def score_game(game_core):
    '''Запуск игры 1000 раз подряд'''
    count_ls = []
    np.random.seed(1)  # фиксация для воспроизводимости эксперимента
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запуск
score_game(game_core_v3)

