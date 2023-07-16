"""
Декораторы функций - добавляет к функции доп. функцию, что может срабатывать до и после основной функции.


"""

import webbrowser

def validator(func):   # декоратор
    def wrapper(url):
        if "." in url:
            func(url)
        else:
            print("Неверный URL.")
    return wrapper

@validator   # Декоратор
def open_url(url):
    webbrowser.open(url)

open_url("http://youtube.com")