# Task 1.1
def task_1_1():
    a = 10  # integer
    b = "Good day"  # string

    print(a)  # output on screen "a"
    print(b)  # output on screen "b"

    name = input("Введите Ваше имя - ")
    digit = input("Введите Ваш номер - ")

    print("Добрый день -", name)  # output on screen "Имя"
    print("Вам необходимо пройти к окну", digit)  # output on screen "Возраст"


# Task 1.2
def task_1_2():
    S = int(input("Введите время в секундах - "))
    Hours = S // 3600
    Min = (S % 3600) // 60
    Sec = (S % 3600) % 60
    print("Время - ", f"{Hours}:{Min}:{Sec}")


# Task 1.3
def task_1_3():
    digit = input("Введите число - ")
    print("Результат равен:", (int(digit) + int(digit + digit) + int(digit + digit + digit)))


# Task 1.4
def task_1_4():
    digit = int(input("Введите целое положительное число - "))
    max = digit%10
    digit = digit//10
    while digit > 0:
        if digit%10 > max:
            max = digit%10
        digit = digit//10
    print(max)


# Task 1.5
def task_1_5():
    profit = int(input("Введите значение выручки - "))
    expenses = int(input("Введите значение затрат - "))
    if (profit - expenses) > 0:
        print('Фирма работает с прибылью')
    else:
        print('Фирма работает с убытком')


# Task 1.6
def task_1_6():
    profit = int(input("Введите значение выручки - "))
    expenses = int(input("Введите значение затрат - "))
    staff = int(input("Введите количество персонала - "))
    if (profit - expenses) > 0:
        print('Фирма работает с прибылью')
        pr = ((profit - expenses) / profit) * 100
        st = pr / staff
        print("Рентабельность фирмы - ", f"{pr} %")
        print("Рентабельность на одного сотрудника - ", f"{st} %")
    else:
        print('Фирма работает с убытком')


# Task 1.7
def task_1_7():
    dist = int(input("Введите количество километров которые пробегает спотрсмен в день - "))
    km = int(input("Введите количество километров для определния количества дней - "))
    days = 1
    while dist < km:
        print(f"{days}-й день: {round(dist, 2)} км")
        dist = dist + (dist * 0.1)
        days = days + 1
    print(f"{days}-й день: {round(dist, 2)} км")
    print("На -", f"{days} день спортсмен достиг результата - не менее", f"{km} километров")


