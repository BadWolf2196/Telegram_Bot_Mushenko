from collections import defaultdict


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


db = UserDB()
db.change_to(1, 'RUB')
db.change_to(1, 'USD')

print(db.get_pair(1))
