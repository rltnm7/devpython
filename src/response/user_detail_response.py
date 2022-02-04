
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

    def __eq__(self, other):
        """
        ==演算子

        Parameters
        ----------
        other : UserDetailResponse
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
