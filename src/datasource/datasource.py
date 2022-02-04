import psycopg2


class PostgreSQL:
    """
    PostgreSQL用データソースクラス
    """

    def __init__(self, hostname, port, dbname, user, password):
        """
        コンストラクタ

        Parameters
        ----------
        hostname : str
            接続先ホスト名
        port : int
            接続先ポート
        dbname : str
            接続先データベース名
        user : str
            接続ユーザ名
        password : str
            接続パスワード
        """
        connect_string = "host=%s port=%s dbname=%s user=%s password=%s" % (
            hostname, port, dbname, user, password)
        self.connection = psycopg2.connect(connect_string)
        self.cursor = self.connection.cursor()

    def __del__(self):
        """
        デストラクタ
        """
        self.cursor.close()
        self.connection.close()

    def execute(self, query):
        """
        クエリの実行

        Parameters
        ----------
        query : str
            実行クエリ

        Returns
        -------
        list of tuple
            クエリ結果
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
