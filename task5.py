# # Task 1.1
# with open('example.txt', 'a') as my_f:
#     line = input('Введите текст\n')
#     while line:
#         my_f.writelines(line + '\n')
#         line = input('Введите текст\n')
#         if not line:
#             break
#
#
# # Task 1.2
# with open('example_task_2.txt', 'r') as my_f:
#         w = my_f.read().replace(" ", "")
#         enter = w.count('\n')
# print("Количество строк - ", enter + 1)
# print("Количество символов - ", (len(w) - enter))
#
#
# # Task 1.3
# with open('example_task_3.txt', 'r', encoding='utf-8') as my_f:
#     workers = {}
#     s = 0
#     w = 0
#     for line in my_f:
#         key, value = line.split()
#         workers[key] = value
#         s = s + float(value)
#         w += 1
#         if float(value) < 20000:
#             print(f'Оклад меньше 20 тысяч рублей у сотрудника - {key}')
# print(f'Cредняя величина дохода сотрудников - {round(s / w, 2)} рублей')
#
#
# # Task 1.4
# my_dict = {'One' : 'Один', 'Two' : 'Два', 'Three' : 'Три', 'Four' : 'Четыре'}
# new_str = []
# with open('example_task_4.txt', 'r') as my_f1:
#     for i in my_f1:
#         i = i.split(' ', 1)
#         new_str.append(my_dict[i[0]] + '  ' + i[1])
# with open('target_4.txt', 'w') as my_f2:
#     my_f2.writelines(new_str)
#
#
# Task 1.5
# with open('digit.txt', 'w') as my_f:
#     line = input('Введите набор целых чисел разделенных пробелами - ')
#     my_f.writelines(line + '\n')
# try:
#     with open('digit.txt', 'r') as my_f:
#         text = my_f.read().split()
#         sum = 0
#         for i in range(len(text)):
#             sum += int(text[i])
# except ValueError:
#     print("Внимание ввод только целых чисел")
# else:
#     print(f'Сумма числел в файле = {sum}')
#
#
# # Task 1.6
# my_dict = {}
# try:
#     with open('example_task_6.txt', encoding='utf-8') as my_f:
#         my_str = my_f.readlines()
#     for line in my_str:
#         data = line.replace('(', ' ').split()
#         my_dict[data[0][::]] = sum(int(i) for i in data if i.isdigit())
# finally:
#     print(my_dict)
#
#
# # Task 1.7
# import json
# input_data = []
# with open('example_task_7.txt', 'r') as my_f:
#     my_dict = {}
#     profit_comp = []
#     for i in my_f:
#         comp_name, comp_form, revenue, losses = i.split()
#         profit = float(revenue) - float(losses)
#         my_dict[comp_name] = profit
#         if profit:
#             profit_comp.append(profit)
#     input_data.append(my_dict)
#     input_data.append(f'Average profit = {round(sum(profit_comp) / len(profit_comp), 2)}')
#
# with open('example_task_7.json', 'w') as output_data:
#     json.dump(input_data, output_data)
