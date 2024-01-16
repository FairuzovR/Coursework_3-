import os
import json
from config import root_path
import operator


def displays_list():
    """открывает файл с данными и выводит список операций"""
    with open(os.path.join(root_path, 'operations.json')) as file:
        raw_json = file.read()
        operations_file = json.loads(raw_json)

    return operations_file


def filter_list():
    """Фильтрует лист по результату операции EXECUTED,
    выдает отсортированный список последних 5-ти операций
    ввиде кортежа"""
    operations_list = list()
    for item in displays_list():
        if item == {}:
            continue
        elif item["state"] == "EXECUTED":
            operations_list.append(item)
    del operations_list[0:len(operations_list) - 5]

    return sorted(operations_list, key=operator.itemgetter('date'), reverse=True)


# def creates_instance():
#     """Создает экземпляры - 5 шт"""
#     instance_file = list()
#     for item in filter_list():
#         if "from" in item:
#             instance_file.append(Transactiondata(item["id"], item["date"], item["state"], item["operationAmount"],
#                                                  item["description"], item["to"], item["from"]))
#         else:
#             instance_file.append(Transactiondata(item["id"], item["date"], item["state"], item["operationAmount"],
#                                                  item["description"], item["to"]))
#
#     return instance_file