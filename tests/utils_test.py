

from utils import get_data, get_filtered_data, get_formated_data


def test_get_data():
    data = get_data()

    assert isinstance(data, list)


def test_filtred_data():
    data = get_data()
    data = get_filtered_data(data)
    data_ = [x for x in data if x['state'] == "CANCELED"]
    assert len(data_) == 0


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
