import numpy as np

def random_predict(number:int=1) -> int:
    print(number)
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попаданий
    """
    return ''
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break
    return(count)

if __name__ == '__main__':
    random_predict('hhello')