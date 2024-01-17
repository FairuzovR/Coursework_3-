import pytest
from datetime import datetime
from src.classfile import Transactiondata

check_instance = Transactiondata(957763565, '2019-01-05T00:52:30.108534', 'EXECUTED',
                                 {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                 'Перевод со счета на счет', 'Счет 46363668439560358409',
                                 'Счет 18889008294666828266')

def test_data_operation():
    assert check_instance.data_operation() == '05.01.2019'


def test_status_description():
    assert check_instance.status_description() == 'Перевод со счета на счет'

def test__sent_from():
    assert check_instance.sent_from() == 'Счет **8266 -> '

def test_sent_to():
    assert check_instance.sent_to() == 'Счет **8409'

def test_displays_amount():
    assert check_instance.displays_amount() == '87941.37'

def test_displays_currency():
    assert check_instance.displays_currency() == 'руб.'