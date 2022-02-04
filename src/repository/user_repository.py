from configuration import datasource
from entity import User


class UserRepository:
    """
    ユーザリポジトリクラス
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.datasource = datasource

    @staticmethod
    def _convert_user(record):
        """
        データベースの検索結果をUserオブジェクトに変換する

        Parameters
        ----------
        record : tuple
            データベース検索結果

        Returns
        -------
        User
            検索結果のユーザオブジェクト
        """
        user = User(id=record[0], username=record[1],
                    name=record[2], birthday=record[3])
        return user

    def find_all(self):
        """
        ユーザ全件検索

        Returns
        -------
        list of User
            ユーザ検索結果
        """
        query = "SELECT * FROM users"
        records = self.datasource.execute(query)

        users = []
        for record in records:
            user = self._convert_user(record)
            users.append(user)

        return users

    def find_by_username(self, username):
        """
        特定ユーザ検索

        Parameters
        ----------
        username : str
            検索ユーザ名

        Returns
        -------
        User
            検索結果
        """
        query = "SELECT * FROM users WHERE username = '%s'" % username
        record = self.datasource.execute(query)
        user = self._convert_user(record[0])

        return user
