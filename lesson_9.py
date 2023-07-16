"""
Кортежи (tuple)

кортежи - то же, что и списки, за исключением:
     - нельзя видоизменять добавленные элементы;
     - кортежи "весят" меньше, чем списки.
     
"""


data = (4, 6, 7, 3, 6, True, 5.6, "Hello")
# data[0] = 5 - нельзя изменять элементы
#print(data[2:5]) # срез

# print(data.count(6)) # подсчет указанных элементов

# print(len(data)) # длинна кортежа

#print(data)



#data = 5, 7, True # кортеж можно записывать без скобок

for el in data:
    print(el)

nums = [5, 7, 8]

new_data = tuple(nums) # конвертация списка в кортеж (tuple)
word = tuple("Hello World")

print(word)


