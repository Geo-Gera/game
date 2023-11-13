import numpy


def random_predict(number: int = 1) -> int:
    """угадываем значение, уменьшая диапазон значений в два раза.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    L1 = 1  # Минимум
    L2 = 100  # Максимум
    attemption = 0  # Количество попыток

    while True:
        attemption += 1
        if attemption >50:
            break
        step = (L1+L2) // 2  # Складываем минимум и максимум
        if step > number:
            L2 = step - 1
        elif step < number:
            L1 = step + 1
        elif number == step:
            # print(X,"Число Угадано","за", att, "попыток")
            break
    return attemption


def score_game():
    import math
    count_ls = []  # Создаем пустой массив для ответов функции угадывания random_predict
    # загадали список чисел - создали массив чисел от 1 до 100 размеров в 1000 единиц
    numpy.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = numpy.random.randint(1, 101, size=(1000))

    for number in random_array:  # Для кажого числа в нашем массиве случайных чисел делай:
        # Циклически передаем число в функцию random_predict, функция возвращает количество попыток ушедшее на угадывание
        count_ls.append(random_predict(number))

    # при помощи библиотеки numpy вызываем функицю mean вовзращающую среднее в массиве
    score = math.ceil(numpy.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    


if __name__ == "__main__":  # Запуск как главный модуль
    # RUN
    score_game()
