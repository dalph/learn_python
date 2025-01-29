import numpy as np

min_value = 1
max_value = 100
test_count = 10000


def random_predict(number: int = 1) -> int:
    """Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        # предполагаемое число
        predict_number = np.random.randint(min_value, max_value + 1)

        if number == predict_number:
            # выход из цикла если угадали
            break

    return count


def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(min_value, max_value + 1)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count


def game_core_v3(number: int = 1) -> int:
    """Алгоритм бинарного поиска. Мы делим диапазон пополам,
    уменьшая область поиска вдвое на каждом шаге.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Количество попыток
    """
    count = 0
    # границы поиска
    low, high = min_value, max_value

    while True:
        count += 1
        # выбираем середину диапазона
        predict = (low + high) // 2

        if predict == number:
            # если угадали, возвращаем число попыток
            return count
        elif predict < number:
            # поднимаем нижнюю границу
            low = predict + 1
        else:
            # опускаем верхнюю границу
            high = predict - 1


def score_game(random_predict_function: callable) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict_function (callable): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []

    # фиксируем сид для воспроизводимости
    # np.random.seed(1)

    # загадали список чисел
    random_array = np.random.randint(min_value, max_value + 1, size=(test_count))

    for number in random_array:
        count_ls.append(random_predict_function(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == "__main__":
    # Run benchmarking to score effectiveness of all algorithms
    print("Run benchmarking for random_predict: ", end="")
    score_game(random_predict)

    print("Run benchmarking for game_core_v2: ", end="")
    score_game(game_core_v2)

    print("Run benchmarking for game_core_v3: ", end="")
    score_game(game_core_v3)
