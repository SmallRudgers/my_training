
class Animal:
    alive = True
    fed = False
    edible = True

    def __init__(self,name,edible=True):
        self.name = name



    def eat(self,food):

        if food.edible == True and self.omnivore == True:
            print(f'{self.name} съел(a) {food.name}')
            self.fed = True

        elif food.omnivore == True:
            print(f'{self.name} в попытках съесть {food.name}, был(а) съеден(а)')
            food.fed = True
            self.alive = False

        elif food.edible == True and self.omnivore == False:
            print(f'{self.name} съел(a) {food.name}')
            self.fed = True

        else:
            print(f'Мдааа... {self.name} умер(ла) с голоду')
            self.alive = False



class Plant:

    def __init__(self,name,edible=False):
        self.name = name
        self.edible = edible


class Mammal(Animal):
    omnivore = False


class Predator(Animal):
    omnivore = True


class Flower(Plant):
    omnivore = False


class Fruit(Plant):
    omnivore = False


apple = Fruit('Яблоко',True)
aconit = Flower('Аконит',)
bear = Predator('Медведь')
horse = Mammal('Лошадь')


print(bear.name)
print(horse.name)

print('\n')

print(bear.alive)
print(horse.fed)

print('\n')

bear.eat(apple)
horse.eat(aconit)

print('\n')

print(bear.alive)
print(horse.fed)

