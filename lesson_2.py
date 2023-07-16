"""
Переменные и Типы данных.

"""

number = 5 # тип данных int - целое число

digit = -4.543568 # тип данных float - число с плавающей точкой
word = "Результат: " # тип данных str (string) - строка

""" Булевое (bool) значение:
    True - правда, да;
    False - ложь, нет.
"""
booltan = True # тип данных bool 

str_num = "5" # str

print(word + str(digit))

print(word, number + int(str_num))
print(word + str(number + int(str_num)))

number = 7
print("Результат: ", number)

word = "hi" # str
print(word * 2)