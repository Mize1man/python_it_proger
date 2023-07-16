"""
Словари (dict) и работа с ними.
Пример.

"""

person = {
    "user_1" : {
        "first_name" : "John",
        "last_name" : "Marley",
        "age" : 45,
        "adres" : ("г.Москва", "ул. Какая-то", 45), # можно указывать списком или кортежем
        "grades" : {"math" : 5, "physics": 3}
    },
    "user_2" :{

    }
}

print(person["user_1"])
print(person["user_1"]["adres"])
print(person["user_1"]["adres"][1])