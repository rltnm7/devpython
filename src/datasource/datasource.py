import psycopg2

class PostgreSQL:
    def __init__(self, hostname, port, dbname, user, password):
        connect_string = "host=%s port=%s dbname=%s user=%s password=%s" % (hostname, port, dbname, user, password)
        self.connection = psycopg2.connect(connect_string)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.cursor.close()
        self.connection.close()

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
