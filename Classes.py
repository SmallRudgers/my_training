class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

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

House_1.go_to(5)
House_2.go_to(10)