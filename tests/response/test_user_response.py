import sys
sys.path.append("src")

import pytest

import datetime
from response import UserResponse

class TestUserResponse:

    def setup_method(self,method):
        print('method={}'.format(method.__name__))

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))

    def test_eq_true(self):
        left = UserResponse(id=1, username='nana-mizuki')
        right = UserResponse(id=1, username='nana-mizuki')
        assert left == right

    @pytest.mark.parametrize((
        "left_id", "left_username",
        "right_id", "right_username"
    ), [
        (
            1, 'nana-mizuki',
            2, 'nana-mizuki'
        ),
        (
            1, 'nana-mizuki',
            1, 'maaya-uchida'
        )
    ])
    def test_eq_false(self,
        left_id, left_username,
        right_id, right_username
    ):
        left = UserResponse(id=left_id, username=left_username)
        right = UserResponse(id=right_id, username=right_username)
        assert left != right
