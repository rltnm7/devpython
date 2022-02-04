import datetime
from dateutil.relativedelta import relativedelta

from repository import UserRepository


class UserService:
    """
    ユーザサービスクラス
    """

    def __init__(self):
        """
        コンストラクタ
        """
        self.repository = UserRepository()

    def _calc_age(self, birthday):
        """
        生年月日から年齢を計算する

        Parameters
        ----------
        birthday : datetime.date
            生年月日

        Returns
        -------
        int
            年齢
        """
        return relativedelta(datetime.date.today(), birthday).years

    def find_all(self):
        """
        ユーザ全件検索

        Returns
        -------
        list of User
            ユーザ検索結果
        """

        users = self.repository.find_all()
        for user in users:
            user.age = self._calc_age(user.birthday)

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

        user = self.repository.find_by_username(username)
        user.age = self._calc_age(user.birthday)
        return user
