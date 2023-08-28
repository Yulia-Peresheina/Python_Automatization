# Напишите функцию, которая принимает строку текста.
# ✔ Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.
import re


def list_unicode_symbols(data: str) ->list:
    symbol_list = []
    for symbol in data:
        symbol_list.append(ord(symbol))
    sorted_symbol_list = sorted(list(set(symbol_list)), reverse=True)
    return sorted_symbol_list


text = "Напишите функцию"
print(list_unicode_symbols(text))
