# # Task_1.1
# from time import sleep
#
#
# class TrafficLight:
#     __color = {'Red': 7, 'Yellow': 2, 'Green': 7}
#
#     def __init__(self):
#         print(self.__color)
#
#     def running(self):
#         for key, value in self.__color.items():
#             print(f'TrafficLight now - {key}', f'Time {value} second')
#             sleep(value)
#
#
# a1 = TrafficLight()
# a1.running()
# print("The END")
#
#
# # Task_1.2
# from time import sleep
#
#
# class TrafficLight:
#     __delay = {'r': 7, 'y': 2, 'g': 7}
#     __color = "ryg"
#
#     def __init__(self, color):
#         if color != self.__color:
#             print("Error!!! The default output will be made (ryg)")
#
#     def running(self):
#         for key, value in self.__delay.items():
#             print(f'TrafficLight now - {key}', f'Time {value} second')
#             sleep(value)
#
#
# c = input(f'Enter order of colors TrafficLight (for example ryg) - ')
# a1 = TrafficLight(c)
# a1.running()
# print("The END")
#
#
# # Task_2
# class Road:
#
#     def road_mass(self, length, width):
#         self._length = length
#         self._width = width
#         print(f'Road mass = {self._length * self._width * 0.025 * thickness} t')
#
#
# thickness = float(input(f'Enter thickness of Road (sm) - '))
# l = float(input(f'Enter length of Road (m) - '))
# w = float(input(f'Enter width of Road (m) - '))
# a = Road()
# a.road_mass(l, w)
#
#
#
# # Task_3
# class Worker:
#
#     def __init__(self, name, surname, position):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": w, "bonus": b}
#
#
# class Position(Worker):
#
#     def get_full_name(self):
#         print(f'Full name - {self.surname} {self.name} holds the position - {self.position}')
#
#     def get_total_income(self, wage, bonus):
#         print(f'Income - {sum(self._income.values())}')
#
#
# n = input(f'Enter first name - ')
# s = input(f'Enter second name - ')
# p = input(f'Enter work position - ')
# w = float(input(f'Enter wage (RUB) - '))
# b = float(input(f'Enter bonus (RUB) - '))
#
# a = Position(n, s, p)
# a.get_full_name()
# a.get_total_income(w, b)
#
# # Task_4
# class Car:
#
#     def __init__(self, speed, color, name, is_police, direction):
#         self.speed = speed
#         self.color = color
#         self.name = name
#         self.is_police = is_police
#         self.direction = direction
#
#     def go(self):
#         if self.speed != 0:
#             print(f'Car - {self.color} {self.name} GO')
#
#     def stop(self):
#         if self.speed == 0:
#             print(f'Car - {self.color} {self.name} Stop')
#
#     def turn(self, direction):
#         if self.is_police:
#             print(f'Car - {self.color} {self.name} make direction {direction}')
#         else:
#             print(f'Car - {self.color} {self.name} moving straight')
#
#     def show_speed(self):
#         print(f"Speed {self.speed}")
#
#
# class TownCar(Car):
#     def show_speed(self):
#         if self.speed < 61 and self.name == "Towncar":
#             print(f'Car - {self.color} {self.name} Speed - {self.speed}')
#         else:
#             print(f"Speeding on {self.speed - 60}")
#
#
# class SportCar(Car):
#     pass
#
#
# class WorkCar(Car):
#     def show_speed(self):
#         if self.speed < 41 and self.name == "Workcar":
#             print(f'Car - {self.color} {self.name} Speed - {self.speed}')
#         else:
#             print(f"Speeding on {self.speed - 40}")
#
#
# class PoliceCar(Car):
#     pass
#
#
# a = TownCar(65, "White", "Towncar", True, direction="")
# a.go()
# a.stop()
# a.turn("Left")
# a.show_speed()
#
# b = SportCar(170, "Black", "Sportcar", False, direction="")
# b.go()
# b.stop()
# b.turn("Left")
# b.show_speed()
#
# c = WorkCar(43, "Red", "Workcar", True, direction="")
# c.go()
# c.stop()
# c.turn("Right")
# c.show_speed()
#
# d = PoliceCar(200, "Blue", "Policecar", False, direction="")
# d.go()
# d.stop()
# d.turn("Left")
# d.show_speed()
#
#
# # Task_5
# class Stationery:
#     def __int__(self, title):
#         self.title = title
#
#     def draw(self):
#         print(f'Starting rendering')
#
#
# class Pen(Stationery):
#     def draw(self):
#         print(f'Starting rendering from Pen')
#
#
# class Pencil(Stationery):
#     def draw(self):
#         print(f'Starting rendering from Pencil')
#
#
# class Handle(Stationery):
#     def draw(self):
#         print(f'Starting rendering from Handle')
#
# a = Stationery()
# a.draw()
#
# b = Pen()
# b.draw()
#
# c = Pencil()
# c.draw()
#
# d = Handle()
# d.draw()


