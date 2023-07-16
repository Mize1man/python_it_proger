""" 
Циклы и операторы в них (for, while):
for - применяется в случае, если необходимо что-то перебрать
while - применяется в случае, если необходимо прописать условие и выполнять определенный цикл

Циклы - конструкции, которые позволяют выполнять код несколько раз подряд

"""

# for i in range(1, 6, 2):
#     print(i)

# count = 0
# word  = "Hello World!"
# for i in word:
#     if i == "l":
#         count += 1

# print("Count:", count)


# i = 5
# while i <= 15:
#     print(i)
#     i += 2


# isHasCar = True
# while isHasCar:
#     if input("Enter Stop: ") == "Stop":
#         isHasCar = False

# for i in range(1, 11):
#     if i == 5:
#         break

#     if i % 2 == 0: # % - остаток при делении
#         continue

#     print(i)


found = None
for i in "hello":
    if i == "l":
        found = True
        break

else:
    found = False

print(found)