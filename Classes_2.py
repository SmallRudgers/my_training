class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __len__(self):
        return self.floors

    def go_to(self,new_floor):
        n = 0
        if new_floor <= self.floors and new_floor > 0:
            while n != new_floor:
                n += 1
                print(f'Вы на {n} этаже')

            print('Приехали!')

        else:
            print('Такого этажа нет!')

House_1 = House('ЖК Горский', 18)
House_2 = House('Домик в деревне', 2)

#__str__
print(House_1)
print(House_2)

#__len__
print(len(House_1))
print(len(House_2))
