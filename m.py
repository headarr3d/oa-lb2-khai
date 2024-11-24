import math


def task_if1():
    """
    Завдання 1: Перевірка цілого числа.
    Якщо число додатне, відняти 8; інакше залишити без змін.
    """
    try:
        int_num = int(input("Введіть ціле число: "))
        if int_num > 0:
            int_num -= 8
        print("Результат:", int_num)
    except ValueError:
        print("Помилка: потрібно ввести ціле число.")


def task_points_in_area(points, a, b):
    """
    Завдання 2: Визначення точок у заданій області.
    :param points: список координат точок [(x1, y1), (x2, y2), ...]
    :param a: висота прямокутника
    :param b: ширина прямокутника
    :return: кількість точок у заданій області
    """
    count_variant1 = 0
    count_variant2 = 0

    for x, y in points:
        # Перевірка на належність до варіанту 1 (коричнева область)
        if 0 <= x <= b and 0 <= y <= a and (x - b / 2) ** 2 + y ** 2 <= (b / 2) ** 2:
            count_variant1 += 1

        # Перевірка на належність до варіанту 2 (салатова область)
        if 0 <= x <= b and 0 <= y <= a and (x - b / 2) ** 2 + y ** 2 >= (b / 2) ** 2:
            count_variant2 += 1

    print("Кількість точок у варіанті 1:", count_variant1)
    print("Кількість точок у варіанті 2:", count_variant2)


def task_series1(e=1e-5, g=1e5):
    """
    Завдання 3: Дослідження ряду на збіжність.
    |un| < e або |un| > g для зупинки.
    """
    n = 1
    s = 0  # Сума ряду
    while True:
        try:
            u = (n * math.sqrt(n)) / ((n / 2) ** n)
            if abs(u) < e:
                print("Ряд збігається. Сума:", s)
                break
            if abs(u) > g:
                print("Ряд розходиться. Часткова сума:", s)
                break
            s += u
            n += 1
        except ZeroDivisionError:
            print("Ділення на нуль.")
            break