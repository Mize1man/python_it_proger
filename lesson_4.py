"""
Условные кострукции (if).

"""

# if 5 == 5:
#     print("Yes")
#     print("!!!")

user_data = int(input("Введите число: "))

isHappy = True

# if isHappy: # аналогичен if isHappy == False
if isHappy or user_data == 6: # проверка нескольких переменыых с помощью anad / or  
    print("User is Happy!")
elif user_data == 5:
    print("Number if 5")
elif user_data == 7:
    print("Number if 7")
else:      # условие срабатывает в том случае, если не сработали предыдущие.
    print("User is not Happy")





# if user_data != 5:
#     print("Мы на месте.")
#     if user_data > 6:
#         print("Number is bigger than 5.")

