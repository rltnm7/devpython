import sys
sys.path.append("src")

import pytest

import datetime
from datasource import PostgreSQL
from configuration import profile

@pytest.mark.skipif(profile=="test", reason="PostgreSQLがないとテストにならないため")
class TestPostgreSQL:

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.client = PostgreSQL(
            "devpython_devcontainer-db-1", 5432, "sample", "appusr01", "P@ssw0rd")

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        del self.client

    def test_execute(self, mocker):
        mocker.patch.object(psycopg2.cursor, "execute")
        mocker.patch.object(psycopg2.cursor, "fetchall", return_value=[
            (1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21)),
            (2, 'maaya-uchida', 'Maaya Uchida', datetime.date(1989, 12, 27))
        ])

        acctual = [
            (1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21)),
            (2, 'maaya-uchida', 'Maaya Uchida', datetime.date(1989, 12, 27))
        ]

        records = self.client.execute("SELECT * FROM users;")

        assert acctual == records
