class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history += args
        return super().__new__(cls)

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

    def __del__(self):
        print(f"{self.name},снесён, но он останется в истории")



    def go_to(self,new_floor):
        n = 0
        if new_floor <= self.floors and new_floor > 0:
            while n != new_floor:
                n += 1
                print(f'Вы на {n} этаже')

            print('Приехали!')

        else:
            print('Такого этажа нет!')

h1 = House('ЖК Эльбрус', number_of_floors = 10)

print(House.houses_history)

h2 = House('ЖК Акация', number_of_floors = 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', number_of_floors = 20)

print(House.houses_history)

del h2
del h3
print(House.houses_history)










