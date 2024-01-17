import pytest
from src.utils import (
    displays_list, filter_list)


def test_displays_list():
    temp_list = list()
    assert displays_list()[0] == {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                                  "operationAmount": {"amount": "31957.58", "currency":
                                      {"name": "руб.", "code": "RUB"}},
                                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                                  "to": "Счет 64686473678894779589"}
    assert displays_list()[-1]["id"] == 667307132
    assert displays_list()[0]["state"] == "EXECUTED"
    assert displays_list()[0]["date"] == "2019-08-26T10:50:58.294041"
    assert displays_list()[0]["operationAmount"] == {"amount": "31957.58", "currency":
                                      {"name": "руб.", "code": "RUB"}}
    assert displays_list()[0]["to"] == "Счет 64686473678894779589"
    assert type(displays_list()) == type(temp_list)



def test_displays_list__KeyError():
    with pytest.raises(KeyError):
        displays_list()[0][1]
        displays_list()[10000]["id"]
        displays_list()[0]["operationAmount"]["state"]
        displays_list()


def test_filter_list():
    temp_dict = dict()
    for item in filter_list():
        assert item['state'] == 'EXECUTED'
        assert type(item) == type(temp_dict)
    assert filter_list()[0]["id"] == 207126257
    assert len(filter_list()) == 5
