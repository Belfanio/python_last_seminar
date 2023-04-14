"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


def print_convert(text: str):
    text_bytes = text.encode(encoding='utf-8')
    print(text_bytes)
    print(text_bytes.decode(encoding='utf-8'))
    print()


print_convert('разработка')
print_convert('администрирование')
print_convert('protocol')
print_convert('standard')