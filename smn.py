print("\n56.")

class animality():
    def creation(name, food, perk):
        print(f'Животное: {name}\nРацион питания: {food}\nОсобенность: {perk}')

    name = ''
    food = ''
    perk = ''

class herbivore(animality):
    fani = animality()
    fani.name = 'Травоядное'
    fani.food = 'Трава'
    runsfast = 'Быстро бегают'
    animality.creation(fani.name, fani.food, runsfast)
class carnivore(animality):
    sani = animality()
    sani.name = 'Плотоядное'
    sani.food = herbivore
    fangsclaws = 'Очень опасны'
    animality.creation(sani.name, sani.food, fangsclaws)
class omnivore(animality):
    tani = animality()
    tani.name = 'Всеядное'
    tani.food = 'Трава, ' + str(herbivore)
    cannibal = 'Едят всё'
    animality.creation(tani.name, tani.food, cannibal)