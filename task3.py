# # Task 1.1
# def div(a,b):
#     try:
#         rez = a / b
#         print(f"Результат = {rez}")
#     except:
#         ZeroDivisionError
#         print(f'Ошибка! Делить на ноль нельзя')
#
#
# div(float(input("Введите числитель: ")), float(input("Введите знаменатель: ")))
#
#
# # Task 1.2
# def p_d(first_name, second_name, year, city, e_mail, phone):
#     print(f'Сотрудник : {second_name} {first_name} {year} года рождения, проживает в городе {city}  телефон - {phone} электронная почта - {e_mail}')
#
#
# p_d((input("Введите имя: ")), input("Введите фамилию: "), input("Введите год рождения: "), input("Введите город проживания: "), input("Введите e-mail: "), input("Введите телефон: "))
#
#
# # Task 1.3
# def sum_big_arg(a1, a2, a3):
#     try:
#         q = list(map(float, [a1, a2, a3]))
#         q.remove(min(q))
#         return sum(q)
#     except (TypeError, ValueError):
#         return "Внимание !!! Ввод только чисел"
#
#
# print(f'Сумма наибольших аргументов = {sum_big_arg(input("Введите первый аргумент: "), input("Введите второй аргумент: "), input("Введите третий аргумент: "))}')
#

# # Task 1.4.1
# def expon(x, y):
#     try:
#         return float(x) ** int(y)
#     except (ValueError, TypeError):
#         return "Внимание !!! Ввод только чисел"
#
#
# print(f'Результат = {expon(input("Введите действительное положительное число: "), input("Введите целое отрицательное число: "))}')
#

# # Task 1.4.2
# def expon(x, y):
#     rez = 1
#     try:
#         i = abs(int(y))
#         while i != 0:
#             rez /= float(x)
#             i -= 1
#         return rez
#     except (ValueError, TypeError):
#        return "Внимание !!! Ввод только чисел"
#
#
# print(f'Результат = {expon(input("Введите действительное положительное число: "), input("Введите целое отрицательное число: "))}')
#
# # Task 1.5
# def my_sum():
#     sum = 0
#     try:
#         while True:
#             error = False
#             str = input("Введите числа через пробел, Символ # - выход, Нажатие enter подсчет: ").split()
#             for n in str:
#                 if n.lower() == "#":
#                     return sum
#                 else:
#                     try:
#                         sum += int(n)
#                     except ValueError:
#                         error = True
#             if error:
#                 print("Введенные данные некорректны")
#             print(f'Сумма введенных чисел = {sum}')
#     finally:
#         return sum
#
#
# print(f'Сумма введенных чисел = {my_sum()}')

# Task 1.6
# def capital (str):
#     import re
#     if (re.search(r'[^a-zA-Z]', str, re.A)):
#         print("Введенные данные некорректны")
#     else:
#         print(f'Полученный результат - {str.title()}')
#
#
# str = capital(input("Введите слово из маленьких латинских букв - "))


# # Task 1.7
# def capital (str):
#     import re
#     if (re.search(r'[^a-zA-Z ]', str, re.A)):
#         print("Введенные данные некорректны")
#     else:
#         print(f'Полученный результат - {str.title()}')
#
#
# str = capital(input("Введите текст из маленьких латинских букв - "))
