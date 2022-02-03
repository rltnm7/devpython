import sys

sys.path.append("src")

import datetime

from datasource import PostgreSQL
from repository import UserRepository
from entity import User

class TestUserRepository:

    def setup_method(self,method):
        print('method={}'.format(method.__name__))
        self.repository = UserRepository()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_convert_user(self):
        acctual = User(id=1, username='nana-mizuki',
            name='Nana Mizuki', birthday=datetime.date(1980, 1, 21))

        record = (1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21))
        user = self.repository._convert_user(record)

        assert user == acctual

    def test_find_all(self, mocker):
        mocker.patch.object(PostgreSQL, "execute", return_value=[
            (1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21)),
            (2, 'maaya-uchida', 'Maaya Uchida', datetime.date(1989, 12, 27))
        ])

        acctual = [
            User(id=1, username='nana-mizuki',
                name='Nana Mizuki', birthday=datetime.date(1980, 1, 21)),
            User(id=2, username='maaya-uchida',
                name='Maaya Uchida', birthday=datetime.date(1989, 12, 27))
        ]

        results = self.repository.find_all()
        assert results == acctual

    def test_find_by_username(self, mocker):
        mocker.patch.object(PostgreSQL, "execute",
            return_value=[(1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21))],
        )

        acctual = User(id=1, username='nana-mizuki',
            name='Nana Mizuki', birthday=datetime.date(1980, 1, 21))

        result = self.repository.find_by_username('nana-mizuki')
        assert result == acctual
