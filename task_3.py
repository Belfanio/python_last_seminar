"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки
b'' (без encode decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""


def print_info(text: str):
    try:
        print(text, bytes(text, encoding='ASCII'))
    except UnicodeEncodeError:
        print(f"{text} невозможно преобразовать")
    print()


print_info('attribute')
print_info('класс')
print_info('функция')
print_info('type')