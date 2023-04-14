"""
Задание 1.
Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.
*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!
Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор
кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""


def get_unicode_escape(text: str) -> bytes:
    return text.encode("unicode_escape")


def get_unicode(text: str) -> str:
    return get_unicode_escape(text).decode("utf-8")


def print_info(text: str):
    print(text)
    print(type(text))
    text_unicode = get_unicode(text)
    print(text_unicode)
    print(type(text_unicode))
    print()


print_info('разработка')
print_info('сокет')
print_info('декоратор')