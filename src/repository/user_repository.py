from configuration import datasource
from entity import User

class UserRepository:
    def __init__(self):
        self.datasource = datasource

    @staticmethod
    def _convert_user(record):
        user = User()
        user.id=record[0]
        user.username=record[1]
        user.name = record[2]
        user.birthday = record[3]
        return user

    def find_all(self):
        query = "SELECT * FROM users"
        records = self.datasource.execute(query)

        users = []
        for record in records:
            user = self._convert_user(record)
            users.append(user)

        return users

    def find_by_username(self, username):
        query = "SELECT * FROM users WHERE username = '%s'" % username
        record = self.datasource.execute(query)
        user = self._convert_user(record[0])

        return user
