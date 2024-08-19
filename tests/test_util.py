
from src.utils import read_file_xlsx
from unittest.mock import patch

import pandas as pd
import pytest


data_test = [
    {'id': 650703, 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': 16210, 'currency_name': 'Sol',
     'currency_code': 'PEN', 'from': 'Счет 58803664561298323391', 'to': 'Счет 39745660563456619397',
     'description': 'Перевод организации'},
    {'id': 3598919, 'state': 'EXECUTED', 'date': '2020-12-06T23:00:58Z', 'amount': 29740, 'currency_name': 'Peso',
     'currency_code': 'COP', 'from': 'Discover 3172601889670065', 'to': 'Discover 0720428384694643',
     'description': 'Перевод с карты на карту'}]

@pytest.fixture
def test_df() -> pd.DataFrame:
    return pd.DataFrame(data_test)


@patch("src.utils.pd.read_excel")
def test_read_file_xls(mock_read_xls, test_df):
    """Тест чтение из файла xls."""
    mock_read_xls.return_value = test_df
    res = csv_or_xls_read_file("./data_test/test.xlsx")
    expected = test_df.to_dict(orient="records")
    assert res == expected
    mock_read_xls.assert_called_once_with("./data_test/test.xlsx")
