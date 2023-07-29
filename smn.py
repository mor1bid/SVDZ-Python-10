print("\n56.")

class animality:
    def creation(name, food, perk):
        print(f'Животное: {name}\n Рацион питания: {food}\nОсобенность: {perk}')

    name = '0_0'
    food = '0_0'

class herbivore(animality):

    name = 'Травоядное'
    food = 'Трава'
    runsfast = True
    animality.creation(name, food, runsfast)
class carnivore(animality):
    name = 'Плотоядное'
    food = herbivore
    fangsclaws = True
    animality.creation(name, food, fangsclaws)
class omnivore(animality):
    name = 'Всеядное'
    food = 'Трава, ' + str(herbivore)
    cannibal = True
    animality.creation(name, food, cannibal)