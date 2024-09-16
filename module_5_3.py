class House:
    def __init__(self, name: str, floors: int):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def eq(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __eq__(self, other):
        return self.eq(other)

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors


    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors

    def __ne__(self, other):
        return not self.eq(other)

    def add(self, value):
        if isinstance(value, int):
            self.floors += value
        return self

    def __add__(self, value):
        return self.add(value)

    def __radd__(self, value):
        return self.add(value)

    def __iadd__(self, value):
        return self.add(value)

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # eq

h1 = h1 + 10  # add
print(h1)
print(h1 == h2)

h1 += 10  # iadd
print(h1)

h2 = 10 + h2  # radd
print(h2)

print(h1 > h2)  # gt
print(h1 >= h2)  # ge
print(h1 < h2)  # lt
print(h1 <= h2)  # le
print(h1 != h2)  # ne