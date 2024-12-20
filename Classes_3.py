class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __len__(self):
        return self.floors

    def __eq__(self, other):
        return self.floors == other.floors

    def __lt__(self, other):
        return self.floors < other.floors

    def __le__(self, other):
        return self.floors <= other.floors

    def __add__(self, other):
        if isinstance(other, House):
            self.floors += other.floors
        elif isinstance(other, int):
            self.floors += other
        return self

    def __radd__(self, other):
        if isinstance(other, House):
            self.floors += other.floors
        elif isinstance(other, int):
            self.floors += other
        return self

    def __iadd__(self, other):
        if isinstance(other, House):
            self.floors += other.floors
        elif isinstance(other, int):
            self.floors += other
        return self

    def go_to(self,new_floor):
        n = 0
        if new_floor <= self.floors and new_floor > 0:
            while n != new_floor:
                n += 1
                print(f'Вы на {n} этаже')

            print('Приехали!')

        else:
            print('Такого этажа нет!')

house_1 = House('ЖК Эльбрус', 10)
house_2 = House('ЖК Акация', 20)

print(house_1)
print(house_2,'\n')

#__eq__ __ne__
print(house_1 == house_2)
print(house_1 != house_2,'\n')

#__lt__ __gt__
print(house_1 < house_2)
print(house_1 > house_2,'\n')

#__le__ __ge__
print(house_1 <= house_2)
print(house_1 >= house_2,'\n')

#__add__ __radd__ __iadd__
house_1 = house_1 + 10
house_2 += 10
print(house_1)
print(house_1 == house_2)






