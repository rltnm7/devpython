import sys
sys.path.append("src")

import freezegun
import datetime
from dateutil.relativedelta import relativedelta

from repository import UserRepository
from service import UserService
from entity import User

class TestUserRepository:

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        self.service = UserService()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    @freezegun.freeze_time("2022-01-20")
    def test_calc_age_41(self):
        acctual = 41
        result = self.service._calc_age(datetime.date(1980, 1, 21))
        assert result == acctual

    @freezegun.freeze_time("2022-01-21")
    def test_calc_age_42(self):
        acctual = 42
        result = self.service._calc_age(datetime.date(1980, 1, 21))
        assert result == acctual

    @freezegun.freeze_time("2022-01-21")
    def test_find_all(self, mocker):
        mocker.patch.object(UserRepository, "find_all", return_value=[
            User(id=1, username='nana-mizuki', name='Nana Mizuki',
                birthday=datetime.date(1980, 1, 21)),
            User(id=2, username='maaya-uchida', name='Maaya Uchida',
                birthday=datetime.date(1989, 12, 27))
        ])

        acctual = []
        acctual.append(User(id=1, username='nana-mizuki', name='Nana Mizuki',
            birthday=datetime.date(1980, 1, 21), age=42))
        acctual.append(User(id=2, username='maaya-uchida', name='Maaya Uchida',
            birthday=datetime.date(1989, 12, 27), age=32))

        results = self.service.find_all()
        
        assert results == acctual

    @freezegun.freeze_time("2022-01-21")
    def test_find_by_username(self, mocker):
        mocker.patch.object(UserRepository, "find_by_username",
            return_value=User(id=1, username='nana-mizuki', name='Nana Mizuki',
                birthday=datetime.date(1980, 1, 21))
        )

        acctual = User(id=1, username='nana-mizuki', name='Nana Mizuki',
            birthday=datetime.date(1980, 1, 21), age=42)

        result = self.service.find_by_username('nana-mizuki')

        assert result.__eq__(acctual)
