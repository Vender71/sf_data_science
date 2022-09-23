"""
Игра угадай число
Компьютер сам загадывает число и сам угадывает число

"""


import numpy as np
import math


MAX_NUMBER_VALUE = 101


def random_predict(number:int=np.random.randint(1, MAX_NUMBER_VALUE)) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(
            1, MAX_NUMBER_VALUE) # предполагаемое число
        
        if number == predict_number:
            break   # выход из цикла, если угадали
    
    return count


def binary_predict(number:int=np.random.randint(1, MAX_NUMBER_VALUE)) -> int:
    """Угадываем число бинарным поиском

    Args:
        number (int, optional):
            Загаданное число.
            Defaults to np.random.randint(1, MAX_NUMBER_VALUE).

    Returns:
        int: Число попыток
    """
    
    count = 0
    half_number = math.ceil(MAX_NUMBER_VALUE / 2)
    predict_number = half_number

    while True:
        count += 1
        
        if predict_number == number:
            break
        else:
            half_number = math.ceil(half_number / 2)
            
            if predict_number > number:
                predict_number -= half_number
            else:
                predict_number += half_number
    
    return count


def score_game(predict_algorithm) -> int:
    """За какое количество попыток в среднем из 1000 подходов
       угадывает наш алгоритм

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []   # список для сохранения количества попыток
    np.random.seed(1)   # фиксируем сид для воспроизводимости
    random_array = np.random.randint(
        1, MAX_NUMBER_VALUE, size = (1000)) # загадали список чисел
    
    for number in random_array:
        count_ls.append(predict_algorithm(number))
    
    score = int(np.mean(count_ls))  # находим среднее количество попыток
    
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток.")
    return score

# RUN
score_game(binary_predict)