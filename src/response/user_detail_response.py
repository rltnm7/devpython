
class UserDetailResponse:
    """
    ユーザ詳細レスポンス
    """

    def __init__(self, *, id, username, name, birthday, age):
        """
        コンストラクタ

        Parameters
        ----------
        id : int
            ID
        username : str
            ユーザ名
        name : str
            氏名
        birthday : datatime.date
            生年月日
        age : int
            年齢
        """
        self.id = id
        self.username = username
        self.name = name
        self.birthday = birthday
        self.age = age
