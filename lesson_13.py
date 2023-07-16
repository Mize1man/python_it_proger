"""
Работа с файлами за счет Phyton.

"""

# data = input("введите текст: ")

# file = open("data/text.txt", "a")

# file.write(data + "\n") # несение данных в файл + переход на новую строку

# file.close()


file = open("data/text.txt", "r")

# print(file.read()) # в скобках указывается число выводимых символов. Если пусто, то выводит все.

for line in file: # вывод построчно
    print(line, end="|")

file.close()