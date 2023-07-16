"""
Функции (def, lambda).

"""

# def test_func(word):
#     print(word, end="")
#     print("!")


# test_func("hi")
# test_func("5")
# test_func("5.6")




def summ(a, b):
    res = a + b
    print("Result:", res)

summ(5.5, 7.5)
summ("H", "i")
"""
аналогичный вариант
"""
def summ(a, b):
    return a + b

res = summ(5.5, 7.5)
print(res)
print(summ("H", "i")) # вместо двух строк