# Task 1.1
def task_1_1():
    my_string =  [4, 234, 45.8, "text", "word", "el", True, None]
    for el in range (len(my_string)):
        print('Переменная - ', type(my_string[el]))


# Task 1.2
def task_1_2():
    str = list(input("Введите список элементов - "))
    if len(str) % 2 == 0:
        str[::2], str[1::2] = str[1::2], str[::2]
    else:
        str[:-1:2], str[1:-1:2] = str[1:-1:2], str[:-1:2]
    print (f"Измененный список {' '.join(str)}")


# Task 1.3.1
def task_1_3_1():
    winter_list = [1, 2 ,12]
    spring_list = [3, 4, 5]
    summer_list = [6, 7, 8]
    autumn_list = [9, 10, 11]
    month = int(input("Введите цифровое значение месяца - "))
    if month in winter_list :
        print("Введенный месяц относится к времени года ЗИМА")
    elif month in spring_list :
        print("Введенный месяц относится к времени года ВЕСНА")
    elif month in summer_list:
        print("Введенный месяц относится к времени года ЛЕТО")
    elif month in autumn_list:
        print("Введенный месяц относится к времени года ОСЕНЬ")


# Task 1.3.2
def task_1_3_2():
    dict = { 1:'ЗИМА', 2:'ЗИМА' ,12:'ЗИМА', 3:'ВЕСНА', 4:'ВЕСНА' ,5:'ВЕСНА',
             6:'ЛЕТО', 7:'ЛЕТО' ,8:'ЛЕТО', 9:'ОСЕНЬ', 10:'ОСЕНЬ' ,11:'ОСЕНЬ'}
    month = int(input("Введите цифровое значение месяца - "))
    value = dict[month]
    print("Введенный месяц относится к времени года -", value)


# Task 1.4
def task_1_4():
    str = input("Введите строку из нескольких слов, разделённых пробелами - ")
    temp = str.split(' ')
    for number, i in enumerate (temp, 1):
        if len(i) >= 10:
            i = i[:10]
            print(number, i)
        else:
            print(number, i)

# Task 1.5
def task_1_5():
    rating= [7, 5, 3, 3, 2]
    print(f"Текущая структура Рейтинга : {rating}")
    new_el = int(input("Введите новый элеменнт рейтинга - "))
    rating.insert(0,new_el)
    rating.sort(reverse = True)
    print(f"Новая структура Рейтинга : {rating}")


# Task 1.6
def task_1_6():
    product = []
    names = []
    prices = []
    quantitys = []
    units = []
    numbers = int(input("Введите количество товаров - "))
    for x in range(numbers):
        name = input("Введите название - ")
        price = int(input("Введите цену - "))
        quantity = int(input("Введите количество - "))
        unit = input("Введите единицу измерения - ")
        mydict = dict({'Название': name, 'Цена': price, 'Количество': quantity, 'Ед': unit})
        prod = (x, mydict)
        product.append(prod)
        names.append(product[x][1].get('Название'))
        prices.append(product[x][1].get('Цена'))
        quantitys.append(product[x][1].get('Количество'))
        units.append(product[x][1].get('Ед'))
    print("Название: ", names)
    print("Цена: ", prices)
    print("Количество: ", quantitys)
    print("Ед: ", units)
