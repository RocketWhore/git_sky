import pytest

from utils import get_data, get_filtered_data, get_last_values, get_formated_data

def test_get_data():
    data = get_data()

    assert isinstance(data, list)

def test_filtred_data(data):
    assert len(get_filtered_data(data, filtred_empty_from=False))
    assert len(get_filtered_data(data, filtred_empty_from=True))

def test_get_last_values(data):
    datas = get_last_values(data, 2)
    assert [x['date'] for x in datas] == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364']

def test_get_formated_data(data):
    datas = get_formated_data(data[:1])
    assert datas[0] == '\n26.08.2019 Перевод организации\nMaestro 837868705199 83 ** **** 5199 -> **9589 64686473678894779589\n31957.58 руб.\n'

    assert datas[0] == '\n26.08.2019 Перевод организации\nMaestro 837868705199 83 ** **** 5199 -> **9589 64686473678894779589\n31957.58 руб.\n'
