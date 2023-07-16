"""
Основы ООП.
Создание класса и объекта.

"""

class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, "age:", self.age, ". Happy:", self.isHappy)

cat1 = Cat()
cat1.set_data("Барсик", 3, True) # заменяет следующие 3 строчки
# cat1.name = "Barsik"
# cat1.age = 3
# cat1.isHappy = True

cat2 = Cat()
cat2.set_data("Жопен", 2, False) # заменяет следующие 3 строчки
# cat2.name = "Жопен"
# cat2.age = 2
# cat2.isHappy = False

cat1.get_data()
cat2.get_data()










