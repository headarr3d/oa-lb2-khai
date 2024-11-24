import m

def main():
    while True:
        print("\nМеню:")
        print("1. Завдання 1: Перевірка числа")
        print("2. Завдання 2: Точки в області")
        print("3. Завдання 3: Дослідження ряду")
        print("0. Вихід")
        try:
            choice = int(input("Виберіть задачу (0 для виходу): "))
            if choice == 0:
                print("До побачення!")
                break
            elif choice == 1:
                m.task_if1()
            elif choice == 2:
                # Задати координати точок та параметри області
                points = [(1, 1), (2, 2), (3, 3)]  # Введіть свої точки
                a = float(input("Введіть висоту прямокутника a: "))
                b = float(input("Введіть ширину прямокутника b: "))
                m.task_points_in_area(points, a, b)
            elif choice == 3:
                e = float(input("Введіть значення e (мала величина): "))
                g = float(input("Введіть значення g (величина для розходження): "))
                m.task_series1(e, g)
            else:
                print("Невірний вибір. Спробуйте ще раз.")
        except ValueError:
            print("Помилка: потрібно ввести число.")

if __name__ == "__main__":
    main()
