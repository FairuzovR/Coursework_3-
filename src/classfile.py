from datetime import datetime


class Transactiondata:

    def __init__(self, id_, date_, state, operationamount, description, to, from_=None):
        #  id_ – id транзакциии
        #  date – информация о дате совершения операции
        #  state – статус перевода (EXECUTED или CANCELED)
        #  operationamount – сумма операции и валюта
        #  description – описание типа перевода
        #  from_ - откуда (может отсуствовать)
        #  to - куда
        self.id_ = id_
        self.date_ = date_
        self.state = state
        self.operationamount = operationamount
        self.description = description
        self.from_ = from_
        self.to = to

    def data_operation(self):
        """Выводит дату операции"""
        thedate_one = datetime.strptime(self.date_, "%Y-%m-%dT%H:%M:%S.%f")
        return thedate_one.strftime("%d.%m.%Y")

    def status_description(self):
        """Выводит наименоание вида операции"""
        return self.description

    def sent_from(self):
        """Выводит зашифрованные реквизиты счета списания денежных средств"""
        if self.from_ is not None:
            data_sheet = self.from_.split(' ')
            if "Счет" in data_sheet:
                for item in data_sheet:
                    if item.isdigit():
                        number_check = ("**" + item[len(item) - 4:len(item)])
                        data_sheet.remove(item)
                        data_sheet.append(number_check)
                        return ' '.join(data_sheet) + ' ' + '->' + ' '
            else:
                for item in data_sheet:
                    if item.isdigit() and len(item) / 4 == 5:
                        number_card = item[0:4] + " " + item[4:6] + "** **** **** " + item[len(item) - 4:len(item)]
                        data_sheet.remove(item)
                        data_sheet.append(number_card)
                        return print(' '.join(data_sheet)) + ' ' + '->' + ' '
                    if item.isdigit() and len(item) / 4 == 4:
                        number_card = item[0:4] + " " + item[4:6] + "** **** " + item[len(item) - 4:len(item)]
                        data_sheet.remove(item)
                        data_sheet.append(number_card)
                        return ' '.join(data_sheet) + ' ' + '->' + ' '
                    if item.isdigit() and len(item) / 4 != 4 or item.isdigit() and len(item) / 4 != 5:
                        return 'test'
        else:
            return ''

    def sent_to(self):
        """Выводит зашифрованные реквизиты счета зачисления денежных средств"""
        data_sheet = self.to.split(' ')
        if "Счет" in data_sheet:
            for item in data_sheet:
                if item.isdigit():
                    number_check = ("**" + item[len(item) - 4:len(item)])
                    data_sheet.remove(item)
                    data_sheet.append(number_check)
                    return ' '.join(data_sheet)
        else:
            for item in data_sheet:
                if item.isdigit() and len(item) / 4 == 5:
                    number_card = item[0:4] + " " + item[4:6] + "** **** **** " + item[len(item) - 4:len(item)]
                    data_sheet.remove(item)
                    data_sheet.append(number_card)
                    return ' '.join(data_sheet)
                if item.isdigit() and len(item) / 4 == 4:
                    number_card = item[0:4] + " " + item[4:6] + "** **** " + item[len(item) - 4:len(item)]
                    data_sheet.remove(item)
                    data_sheet.append(number_card)
                    return ' '.join(data_sheet)
                if item.isdigit() and len(item) / 4 != 4 or item.isdigit() and len(item) / 4 != 5:
                    return 'test'

    def displays_amount(self):
        """Выводит сумму операции"""
        return self.operationamount["amount"]

    def displays_currency(self):
        """Выводит валюту операции"""
        return self.operationamount["currency"]["name"]