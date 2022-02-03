import sys
sys.path.append("src")

import pytest

import datetime
from entity import User

class TestUser:

    def setup_method(self,method):
        print('method={}'.format(method.__name__))

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_eq_true(self):
        left = User(id=1, username='nana-mizuki', name='Nana Mizuki',
            birthday=datetime.date(1980, 1, 21), age=42)
        right = User(id=1, username='nana-mizuki', name='Nana Mizuki',
            birthday=datetime.date(1980, 1, 21), age=42)
        assert left == right

    @pytest.mark.parametrize((
        "left_id", "left_username", "left_name", "left_birthday", "left_age",
        "right_id", "right_username", "right_name", "right_birthday", "right_age"
    ), [
        (
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 42,
            2, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 42
        ),
        (
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 42,
            1, 'maaya-uchida', 'Nana Mizuki', datetime.date(1980, 1, 21), 42
        ),
        (
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 42,
            1, 'nana-mizuki', 'Maaya Uchida', datetime.date(1980, 1, 21), 42
        ),
        (
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 42,
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1989, 12, 27), 42
        ),
        (
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 42,
            1, 'nana-mizuki', 'Nana Mizuki', datetime.date(1980, 1, 21), 32
        ),
    ])
    def test_eq_false(self,
        left_id, left_username, left_name, left_birthday, left_age,
        right_id, right_username, right_name, right_birthday, right_age
    ):
        left = User(id=left_id, username=left_username, name=left_name,
            birthday=left_birthday, age=left_age)
        right = User(id=right_id, username=right_username, name=right_name,
            birthday=right_birthday, age=right_age)
        assert left != right
