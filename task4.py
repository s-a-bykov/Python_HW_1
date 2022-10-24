# # Task 1.1
# Запуск файла (скрипта) salary.py с параметрами из командной строки
#
#
# Task 1.2
# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# print([n for i, n in zip(my_list, my_list[1:]) if n > i])
#
#
# Task 1.3
#print([i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0])
#
# Task 1.4
# my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# print([i for i in my_list if my_list.count(i) == 1])
#
#
# Task 1.5
# from functools import reduce
# print(reduce(lambda x, y: x * y, [i for i in range(100, 1001, 2)]))
#
#
# # Task 1.6.1
# from itertools import count
# from itertools import islice
# stop = int(input("Введите необходимое количество генерируемых целых чисел: "))
# n = int(input("Введите начальное число: "))
# print([i for i in islice(count(n), stop)])
#
#
# # Task 1.6.2
# from itertools import cycle, islice
# my_list = ["QWE"]
# stop = int(input("Введите количество генерируемых повторений: "))
# print(" ".join([next(iter(i for i in islice(cycle(my_list), stop))) for _ in range(stop)]))
#
#
# # Task 1.7
# def my_fact(n):
#     t = 1
#     for i in range(1, n+1):
#         t *= i
#         yield t
#
#
# n = int(input("Введите число, факториал которого Вы хотели бы узнать - "))
# for el in my_fact(n):
#     continue
# print("Ответ", n, "! =", el)
#


