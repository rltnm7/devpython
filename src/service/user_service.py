import datetime
from dateutil.relativedelta import relativedelta

from repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def _calc_age(self, birthday):
        return relativedelta(datetime.date.today(), birthday).years

    def find_all(self):
        users = self.repository.find_all()
        for user in users:
            user.age = self._calc_age(user.birthday)

        return users

    def find_by_username(self, username):
        user = self.repository.find_by_username(username)
        user.age = self._calc_age(user.birthday)
        return user
