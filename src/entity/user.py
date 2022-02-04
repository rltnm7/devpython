
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
