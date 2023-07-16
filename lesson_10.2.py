"""
Словари (dict) и работа с ними.
Функции.

"""

country = {"code" : "RU", "name" : "Russian", "population" : 144}

# print(country.get("code")) = print(country["code"])

# country.clear() # удаляет весь словарь
# country.pop("name") # удаляет элемент указанного ключа
# country.popitem() # удаляет последний элемент

# print(country.keys()) # выводит только ключи
# print(country.values()) # выводит значения

country["code"] = "None" # заменяет значение ключа

print(country.items()) # выводит ключь + значение


