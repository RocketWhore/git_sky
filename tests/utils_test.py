import pytest

from utils import get_data, get_filtered_data, get_formated_data


def test_get_data():
    data = get_data()

    assert isinstance(data, list)


def test_filtred_data():
    data = get_data()
    data = get_filtered_data(data)
    data_ = [x for x in data if x['state'] == "CANCELED"]
    assert len(data_) == 0


# def test_get_last_values():
#     data = [{"date": '2019-07-03T18:35:29.512364'}, {"date": '2019-08-26T10:50:58.294041'}]
#     datas = get_last_values(data, 2)
#     assert [x['date'] for x in datas] == ['2019-07-03T18:35:29.512364', '2019-08-26T10:50:58.294041']


def test_get_formated_data():
    data_ = [{
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    }]
    datas = get_formated_data(data_)
    assert datas == None

    # assert datas[0] == '\n26.08.2019 Перевод организации\nMaestro 837868705199 83 ** **** 5199 -> **9589 64686473678894779589\n31957.58 руб.\n'
