from smn import animality as ani
from smn import herbivore
from smn import carnivore
from smn import omnivore

# Доработать задачи 5-6. Создайте класс-фабрику.
# • Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# • Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

class foundry:
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

        self.name = myani.name
        self.food = myani.food
        self.perk = myani.perk

pick = input("1. Здравствуйте. Выберите желаемый вид животных:\n(1) Травоядные\n(2) Плотоядные\n(3) Всеядные\n(q) Выход\n: ")
foundry(pick)
