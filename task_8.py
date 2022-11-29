# # Task_1
# class MyDate:
#     def __init__(self, string):
#         self.date = string
#
#     @classmethod
#     def date_to_int(cls, obj):
#         return obj.date.split('-')
#
#     @staticmethod
#     def validate_date(self):
#         for i in range(len(self)):
#             if 1 <= int(self[0]) <= 31:
#                 if 1 <= int(self[1]) <= 12:
#                     if 2022 >= int(self[2]) >= 0:
#                         return f'The date is correct'
#                     else:
#                         return f'Year - incorrect value'
#                 else:
#                     return f'Month - incorrect value'
#             else:
#                 return f'Day - incorrect value'
#
#
# print(MyDate.validate_date(MyDate.date_to_int(MyDate('30-12-2022'))))
# print(MyDate.validate_date(MyDate.date_to_int(MyDate('33-12-2022'))))
# print(MyDate.validate_date(MyDate.date_to_int(MyDate('30-13-2022'))))
# print(MyDate.validate_date(MyDate.date_to_int(MyDate('30-12-2023'))))
#
#
# # Task_2
# class Div_By_Zero_Error(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# inp_num = int(input("Enter the numerator : "))
# inp_den = int(input("Enter the denominator : "))
# try:
#     if inp_den == 0:
#         raise Div_By_Zero_Error("Attention error You entered ZERO")
#     res = inp_num / inp_den
# except Div_By_Zero_Error as err:
#     print(err)
#     print("You can't divide by zero")
# else:
#     print(f"The arithmetic operation is completed. Result - {res}")
# finally:
#     print("The program is completed")
#
#
# # Task_3
# class Only_Number(ValueError):
#     pass
#
#
# my_list = []
# while True:
#     try:
#         value = input('Enter a number in the list : ')
#         if value == 'stop':
#             break
#         if not value.isdigit():
#             raise Only_Number(value)
#         my_list.append(int(value))
#     except Only_Number as err:
#         print('Attention You did not enter a number !', err)
# print(f' The entered list of numbers - {my_list}')
#
#
# # Task_4_5_6
# class Office_Equipment:
#
#     def __init__(self, t_p, names, prices, quantitys):
#         self.t_p = t_p
#         self.names = names
#         self.prices = prices
#         self.quantitys = quantitys
#         self.mydict = {'Products': self.t_p, 'Names': self.names, 'Price': self.prices, 'Quantity': self.quantitys}
#
#
# class Printer(Office_Equipment):
#     def draw(self):
#         print(f'Warehouse Printers')
#         print({'Products': self.t_p, 'Names': self.names, 'Price': self.prices, 'Quantity': self.quantitys})
#
#
# class Scanner(Office_Equipment):
#     def draw(self):
#         print(f'Warehouse Scanners')
#         print({'Products': self.t_p, 'Names': self.names, 'Price': self.prices, 'Quantity': self.quantitys})
#
#
# class Xerox(Office_Equipment):
#     def draw(self):
#         print(f'Warehouse Xeroxs')
#         print({'Products': self.t_p, 'Names': self.names, 'Price': self.prices, 'Quantity': self.quantitys})
#
#
# product = []
# numbers = int(input("Enter the numbers of products - "))
#
# for x in range(numbers):
#     try:
#         t_p = input("Enter type of product - ")
#         name = input("Enter a name of product - ")
#         price = int(input("Enter a price of product - "))
#         quantity = int(input("Enter a quantity of product - "))
#         mydict = dict({'Type of product': t_p, 'Names': name, 'Price': price, 'Quantity': quantity})
#         if t_p == 'printer':
#             a = Printer(t_p, name, price, quantity)
#             a.draw()
#         elif t_p == 'scanner':
#             a = Scanner(t_p, name, price, quantity)
#             a.draw()
#         elif t_p == 'xerox':
#             a = Xerox(t_p, name, price, quantity)
#             a.draw()
#         else:
#             print(f'Wrong input')
#     except ValueError:
#         print(f'Wrong input data !!!!!!')
#
#
# # Task_7
# class CompNum:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#
# a = 1 + 2j
# b = 2 + 4j
# print('Addition =', a.__add__(b))
# print('Multiplication =', a.__mul__(b))
