"""
Менеджер "with ... as" для работы с файлами"

"""

# try:
#     file = open("text2.txt", "r")
#     file.read()
# except FileNotFoundError:
#     print("Файл не найден.")

try:     # конструкция обработки исключений
    with open("data/text2.txt", "r", encoding="utf-8") as file: # открыть файл "text2.txt" из папки "data",  методом "r" (чтение), кодировка "utf-8" (кирилица и латиница)
        print(file.read())    # вывести содержимое файла (прочесть)
except FileNotFoundError:     # если ошибка ...такая...
    print("Файл не найден.")      # вывести ("...")

# Менеджер "with ... as" - открывает и закрывает файл. Нет необходимости писать команду file.close()




