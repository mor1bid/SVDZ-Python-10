from smn import animality as Ani
from smn import Herbivore
from smn import Carnivore
from smn import Omnivore
import os

# 1. Доработать задачи 5-6. Создайте класс-фабрику.
# • Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# • Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class Foundry:

    species = ''
    name = ''
    food = ''
    perk = ''

    def __init__(self, pick):
        match pick:
            case '1':
                myani = Herbivore()
                myani.name = input("Введите название/имя вашего травоядного\n: ")
                myani.food = input(f"Что ест {myani.name}?\n: ")
                myani.perk = input(f"Что ещё можете добавить о существе {myani.name}?\n: ")
            case '2':
                myani = Carnivore()
                myani.name = input("Введите название/имя вашего плотоядного\n: ")
                myani.food = input(f"Кого ест {myani.name}?\n: ")
                myani.perk = input(f"Что ещё можете добавить о существе {myani.name}?\n: ")
            case '3':
                myani = Omnivore()
                myani.name = input("Введите название/имя вашего всеядного\n: ")
                myani.food = input(f"Что/кого ест {myani.name}?\n: ")
                myani.perk = input(f"Что ещё можете добавить о существе {myani.name}?\n: ")
            case 'q':
                print('\nПриятного дня!')
                
        species = myani.__class__.__name__
        name = myani.name
        food = myani.food
        perk = myani.perk

        print(f'Класс: {species}\n{Ani.creation(name, food, perk)}')

pick = input("\n1. Здравствуйте. Выберите желаемый вид животных:\n(1) Травоядные\n(2) Плотоядные\n(3) Всеядные\n(q) Выход\n: ")
Foundry(pick)

# 2. Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Семинар 4 Задание №2 
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ- значение
# переданного аргумента, а значение - имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

class Agang:
    def __init__(self, keybox, valbox, data = dict()):
        self.data = data
        self.data[keybox] = valbox
        # print(self.data)

    def getitem(self):
        return self.data
    
    def __str__(self):
        state = self.getitem()
        return str(state)


leader='Hearr Icks'
teamcol='green'
members= 144
casualties= None
form='Anarchist raiders'

keybox = [f'{leader=}'.split('=')[0], f'{teamcol=}'.split('=')[0], f'{members=}'.split('=')[0], f'{casualties=}'.split('=')[0], f'{form=}'.split('=')[0]]
valbox = [leader, teamcol, members, casualties, form]

for i in range(len(keybox)-1):
    Agang(keybox[i], valbox[i])
autoinput = Agang(keybox[i], valbox[i])
print("\n2.1.", autoinput)

# Семинар 5 Задание № 1 
# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов путь, имя файла, расширение файла.

class Pathrec:
    def __init__(self, line, path, newpath = list(), record = list()):
        file = path
        self.newpath = newpath
        if line not in file:
            self.newpath += line + '\\'
        file = file.split('.')
        self.record = ({"Путь:", self.newpath}, {"Имя файла:", file[0]}, {"Расширение файла:", file[-1]})
        # print(record)
    # def __pathinit__(self, newpath):
    #     return newpath
    def recinit(self):
        return self.record
    def __str__(self):
        state = self.recinit()
        return str(state)

path = input("2.2. Здравствуйте. Введите имя желаемого файла, вместе с его расширением\n: ")
newpath = ''
absolute = os.path.abspath(path).split("\\")
for line in range(len(absolute)):
    Pathrec(absolute[line], path, newpath)
    
res = Pathrec(absolute[-1], path, newpath)
print(f'Результат\n: {res}')