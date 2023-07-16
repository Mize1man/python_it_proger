"""
Функции строк. Индексы и срезы.

Функции строк.

"""

word = "Footbal, basketball, skate"
# print(word[1])
# print(len(word))
# print(word.count("p"))

# print(word.upper()) # выводит строку в верхнем регистре
# print(word.isupper()) # выводит Fals или True в зависимости от того, является ли вся строка или элемент в верхнем регистре
# print(word.lower()) # выводит строку в нижнем регистре
# print(word.islower()) # выводит Fals или True в зависимости от того, является ли вся строка или элемент в нижнем регистре

# print(word.capitalize()) # выводит каждый первый символ любого слова в верхнем регистре

# print (word.find("r")) # поиск одного или сразу нескольких символов в строке и вывод их индекса

# print(word.split(", ")) # разбивает строку по определенному символу и выводит списком

hobby = word.split(", ")

for i in range(len(hobby)):
    hobby[i] = hobby[i].capitalize()

result = ", ".join(hobby)
print(result)



