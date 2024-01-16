import pytest
from src.utils import *


def test_displays_list():
    assert displays_list()[0] == {"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041",
                                  "operationAmount": {"amount": "31957.58", "currency":
                                      {"name": "руб.", "code": "RUB"}},
                                  "description": "Перевод организации", "from": "Maestro 1596837868705199",
                                  "to": "Счет 64686473678894779589"}



def test_filter_list():
    pass


def test_creates_instance():
    pass