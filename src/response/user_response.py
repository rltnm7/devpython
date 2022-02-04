
class UserResponse:
    """
    ユーザレスポンス
    """

    def __init__(self, *, id, username):
        """
        コンストラクタ

        Parameters
        ----------
        id : int
            ID
        username : string
            ユーザ名
        """
        self.id = id
        self.username = username

    def __eq__(self, other):
        """
        ==演算子

        Parameters
        ----------
        other : UserResponse
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

        return True
