import pytest

from src.views import greeting
from unittest.mock import patch, Mock
import datetime


@pytest.mark.parametrize(
    "my_date, expected",
    [
        ("2021-12-13 00:13:15", "Доброй ночи"),
        ("2021-12-13 06:13:15", "Доброе утро"),
        ("2021-12-13 14:13:15", "Добрый день"),
        ("2021-12-13 20:13:15", "Добрый вечер")
        ],
)
def test_greeting(my_date: str, expected: str) -> None:
    assert greeting(my_date) == expected


# @patch("src.views.datetime.datetime")
# def test_greeting_non_date(mock_datetime_now):
#     date_test = datetime.datetime(2021, 12, 8, 3, 34, 18, 936772)
#     mock_datetime_now.now.return_value = date_test
#     # datetime.datetime.now = mock_datetime_now
#     res = greeting()
#     print (res)
#     assert res == "Доброй ночи"
#     # mock_datetime_now.assert_called_once_with("2021-12-13 00:13:15")
