
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
