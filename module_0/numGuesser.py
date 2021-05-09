import numpy as np

#определяем диапазон поиска
a = 1
b = 100


def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(a, b+1)  # предполагаемое число
        if number == predict:
            return count  # выход из цикла, если угадали


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(a, b+1, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(a,b+1)
    while number != predict:
        count+=1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Делим область поиска пополам, соответственно, каждый раз исключаем половину возможных цифр'''
    count = 0
    first = a
    last = b
    answer = -1 #изначально ответ вне диапазона поиска
    A = list(range(a, b+1))
    while (first < last) and (answer != number): #Пока первое число меньше, чем последнее и ответ не угадан, продолжаем поиск
        count += 1
        mid = (first + last) // 2 # находим середину
        if A[mid-1] == number: #т.к. в некоторых случаях возможны ситуации, что ответ является first или last, делаем на это проверку
            answer = mid
        elif A[first - 1] == number:
            answer = first
        elif A[last - 1] == number: #добавление этих elif сократило среднее кол-во попыток с 5 до 4 (20%)
            answer = last
        else:
            if number < A[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return(count) # выход из цикла, если угадали

score_game(game_core_v1)
score_game(game_core_v2)
score_game(game_core_v3)