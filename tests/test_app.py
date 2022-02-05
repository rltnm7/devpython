import sys
sys.path.append("src")

import datetime

from entity import User
from service import UserService
from app import app

class TestApp:
    TEMPLATE_DIRECTORY = "tests/templates/"

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        app.config['TESTING'] = True
        self.client = app.test_client()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_list_users(self, mocker):
        mocker.patch.object(UserService, "find_all", return_value=[
            User(id=1, username='nana-mizuki', name='Nana Mizuki',
                 birthday=datetime.date(1980, 1, 21), age=42),
            User(id=2, username='maaya-uchida', name='Maaya Uchida',
                 birthday=datetime.date(1989, 12, 27), age=32)
        ])

        acctual = None
        with open(self.TEMPLATE_DIRECTORY + "acctual_users.html", "rb") as f:
            acctual = f.read()

        result = self.client.get("/users")

        assert result.data == acctual

    def test_get_user(self, mocker):
        mocker.patch.object(UserService, "find_by_username",
                            return_value=User(id=1, username='nana-mizuki', name='Nana Mizuki',
                                              birthday=datetime.date(1980, 1, 21), age=42))

        acctual = None
        with open(self.TEMPLATE_DIRECTORY + "acctual_user_detail.html", "rb") as f:
            acctual = f.read()

        result = self.client.get("/users/nana-mizuki")

        assert result.data == acctual
