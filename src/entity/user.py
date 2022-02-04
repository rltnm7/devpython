
class User:
    """
    ユーザエンティティ
    """

    def __init__(self, *, id=None, username=None, name=None, birthday=None, age=None):
        """
        コンストラクタ

        Parameters
        ----------
        id : int, optional
            ID, by default None
        username : str, optional
            ユーザ名, by default None
        name : str, optional
            氏名, by default None
        birthday : datatime.date, optional
            生年月日, by default None
        age : int, optional
            年齢, by default None
        """
        self.id = id
        self.username = username
        self.name = name
        self.birthday = birthday
        self.age = age

    def __eq__(self, other):
        """
        ==演算子

        Parameters
        ----------
        other : User
            比較対象

        Returns
        -------
        bool
            比較結果
        """
        if self.id != other.id:
            return False

        if self.username != other.username:
            return False

        if self.name != other.name:
            return False

        if self.birthday != other.birthday:
            return False

        if self.age != other.age:
            return False

        return True
