"""
Словари (dict) и работа с ними.

"""

# country = {5 : 3}
# print(country[5])

country = {"code" : "RU", "name" : "Russian", "population" : 144}

# country = dict(code="ru", name="Russsian") # вариант создания словаря

# print(country["name"])

# print(country.items()) # выводит список, где каждый элемент - кортеж

for key, value in country.items():
    print(key, " - ", value)
