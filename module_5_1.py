# module_5_1.py  Домашняя работа по уроку "Атрибуты и методы объекта."


class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floor:
            for i in range(new_floor):
                i += 1
                print(i)
        else:
            print("Такого этажа не существует")


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
print("----")
h2.go_to(10)
print("----")
h3 = House('Ясная поляна', 7)
h3.go_to(47)
print("----")
h3.go_to(4)
print("----")
h3.go_to(2)
print("----")
h3.go_to(7)
print('------')
h3.go_to(1)
