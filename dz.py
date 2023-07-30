from smn import animality as ani
from smn import herbivore
from smn import carnivore
from smn import omnivore
import os

# 1. Доработать задачи 5-6. Создайте класс-фабрику.
# • Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# • Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class foundry:

    species = ''
    name = ''
    food = ''
    perk = ''

    def __init__(self, pick):
        match pick:
            case '1':
                myani = herbivore()
                myani.name = input("Введите название/имя вашего травоядного\n: ")
                myani.food = input(f"Что ест {myani.name}?\n: ")
                myani.perk = input(f"Что ещё можете добавить о существе {myani.name}?\n: ")
            case '2':
                myani = carnivore()
                myani.name = input("Введите название/имя вашего плотоядного\n: ")
                myani.food = input(f"Кого ест {myani.name}?\n: ")
                myani.perk = input(f"Что ещё можете добавить о существе {myani.name}?\n: ")
            case '3':
                myani = omnivore()
                myani.name = input("Введите название/имя вашего всеядного\n: ")
                myani.food = input(f"Что/кого ест {myani.name}?\n: ")
                myani.perk = input(f"Что ещё можете добавить о существе {myani.name}?\n: ")
            case 'q':
                print('\nПриятного дня!')
                
        if pick != '':
            species = myani.__class__.__name__
            name = myani.name
            food = myani.food
            perk = myani.perk

        print(f'Класс: {species}\n{ani.creation(name, food, perk)}')

pick = input("\n1. Здравствуйте. Выберите желаемый вид животных:\n(1) Травоядные\n(2) Плотоядные\n(3) Всеядные\n(q) Выход\n: ")
foundry(pick)

# 2. Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# Семинар 4 Задание №2 
# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ- значение
# переданного аргумента, а значение - имя аргумента. 
# Если ключ не хешируем, используйте его строковое представление.

class agang:
    def __init__(self, i, record):
        self._data = dict()

    def __additem__(self, i, record):
        self._data[record[i]] = i

    def __getitem__(self, i, record):
        return self._data

keybox = ['Hearr Icks', 'green', 144, None, 'Anarchist raiders']

for i in range(len(keybox)-1):
    # print("\n2.", agang(i, leader='Hearr Icks', color='green', members= 144, casualties= None, type='Anarchist raiders'))
    agang(i, keybox[i])
print("\n2.", agang(i, keybox[i]))

# 1. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов путь, имя файла, расширение файла.

def pathrec(path):
    absolute = os.path.abspath(path).split("\\")
    file = path
    path = ''
    for l in absolute:
        if l not in file:
            path += l + '\\'
    file = file.split('.')
    record = ({"Путь:", path}, {"Имя файла:", file[0]}, {"Расширение файла:", file[-1]})
    return record