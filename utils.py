import requests
import json
from config import exchanger, API_access_key, website
from collections import defaultdict


# исключения
class ConvertionException(Exception):
    pass


# создаем класс, в котором хранится информация
# о пользователе
class UserInfo:
    def __init__(self):
        self.fro = 'RUB'  # с какой валюты переводим
        self.to = 'USD'  # на какую валюту переводим


# создаем базу данных с пользователями
class UserDB:
    def __init__(self):
        # если пользователь отсутствует в базе данных
        # то его id создается автоматически посредством
        # метода defaultdict()
        self.db = defaultdict(UserInfo)

    def change_from(self, user_id, val):
        self.db[user_id].fro = val

    def change_to(self, user_id, val):
        self.db[user_id].to = val

    def get_pair(self, user_id):
        user = self.db[user_id]
        return user.fro, user.to


class CryptoConverter:
    @staticmethod
    def convert(values):
        if len(values) != 3:
            raise ConvertionException('Неверное количество параметров. ')
        base, quote, amount = values

        if quote == base:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}.')

        quote_ticker = quote
        base_ticker = base

        print(base_ticker)
        print(quote_ticker)

        if base == 'RUB': base_ticker = 'EUR'

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(
            f'{website}?access_key={API_access_key}&base={base_ticker}&symbols={quote_ticker}')

        total_base = float(json.loads(r.content)['rates'][quote]) * amount

        if base == 'RUB': total_base = float(json.loads(r.content)['rates'][quote]) * 0.010743802 * amount

        return round(total_base, 2)
