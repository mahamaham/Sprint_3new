from random import randint

class Person:
    user_name = 'Ксения'
    email = f'kseniyaminchenko6123@yandex.ru'
    password = f'61236qwe'

class RandomData:
    user_name = 'Тест'
    email = f'test{randint(0, 999)}@yandex.ru'
    password = f'{randint(1000, 9999)}Qwe'