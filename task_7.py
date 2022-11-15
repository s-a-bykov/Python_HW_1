# # Task_1
# class Matrix:
#     def __init__(self, line):
#         self.line = line
#
#     def __str__(self):
#         return '\n'.join('  '.join(map(str, i)) for i in self.line)
#
#     def __add__(self, other):
#         for i in range(len(self.line)):
#             for j in range(len(self.line[0])):
#                 self.line[i][j] = self.line[i][j] + other.line[i][j]
#         return Matrix.__str__(self)
#
#
# a = Matrix([[31, 32], [37, 43], [51, 86]])
# b = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
# c = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
# d = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
# e = Matrix([[4, 5, 6], [4, 5, 6], [4, 5, 6]])
# print(a, '\n')
# print(b, '\n')
# print(c, '\n')
# print(d.__add__(e))
#
#
# Task_2
# from abc import ABC, abstractmethod
#
# class Clothes(ABC):
#     @abstractmethod
#     def value(self, r):
#         pass
#
#
# class Coat(Clothes):
#     def value(self, r):
#         return round(r / 6.5 + 0.5)
#
#
# class Suit(Clothes):
#     def value(self, r):
#         return round(2 * r / 100 + 0.3)
#
#
# class Size:
#     def __init__(self, r1, r2):
#         self.r1 = r1
#         self.r2 = r2
#
#     @property
#     def itog(self):
#         return (round(self.r1 / 6.5 + 0.5)) + (round(2 * self.r2 / 100 + 0.3))
#
#
# c = Coat()
# h = Suit()
# i = float(input(f'Enter your size - '))
# j = float(input(f'Enter your  height - '))
# if i < 30 or i > 64 or j < 120 or j > 200:
#     print(f'Please enter Size from 30 to 64 Height from 120 to 200')
# else:
#     print(f'A suit requires - {c.value(i)} meters of fabric')
#     print(f'A coat requires - {h.value(j)} meters of fabric')
#     s = Size(i, j)
#     print(f'As a result - {s.itog} meters of fabric will be required')
#
# Task_3
# class Cell:
#
#     def __init__(self, cell):
#         self.cell = cell
#
#     def __str__(self):
#         return '\n'.join('  '.join(map(str, i)) for i in self.cell)
#
#     def make_order(self, n):
#          return '\n'.join('  '.join(map(str, i)) for i in ([self.cell[i:i+n] for i in range(0, len(self.cell), n)]))
#
#     def __add__(self, other):
#         for i in range(len(self.cell)):
#             for j in range(len(self.cell[0])):
#                 self.cell[i][j] = self.cell[i][j] + other.cell[i][j]
#         return Cell.__str__(self)
#
#     def __sub__(self, other):
#         for i in range(len(self.cell)):
#             for j in range(len(self.cell[0])):
#                 self.cell[i][j] = self.cell[i][j] - other.cell[i][j]
#         return Cell.__str__(self)
#
#     def __mul__(self, other):
#         for i in range(len(self.cell)):
#             for j in range(len(self.cell[0])):
#                 self.cell[i][j] = self.cell[i][j] * other.cell[i][j]
#         return Cell.__str__(self)
#
#     def __truediv__(self, other):
#         for i in range(len(self.cell)):
#             for j in range(len(self.cell[0])):
#                 self.cell[i][j] = round(self.cell[i][j] // other.cell[i][j])
#         return Cell.__str__(self)
#
#
# a = Cell([[10, 20, 30], [10, 20, 30], [10, 20, 30]])
# b = Cell([[4, 5, 6], [4, 5, 6], [4, 5, 6]])
# c = Cell(['*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', '*', ])
# print(a.__add__(b))
# print(a.__sub__(b))
# print(a.__mul__(b))
# print(a.__truediv__(b))
# print(c.make_order(5))