import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, 101)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали

score_game(game_core_v1)
score_game(game_core_v2)

def game_core_v3(number):
    '''Делим область поиска пополам, соответственно, каждый раз исключаем половину возможных цифр'''
    count = 1
    divide = 50
    range1 = list(range(1,50))
    range2 = list(range(51,101))
    while number != divide:
        count+=1
        if number > divide:
            a = 100-round(len(range2)/2)
            newRange2 = list(range(a,))
        elif number < divide:
            round(len(range1)/2)
    return(count) # выход из цикла, если угадали

def numDivider(num):
    return num / 2

