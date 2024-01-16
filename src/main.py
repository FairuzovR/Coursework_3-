from utils import *
from classfile import *

for item in filter_list():
    if "from" in item:
        instance_info = Transactiondata(item["id"], item["date"], item["state"], item["operationAmount"],
                                        item["description"], item["to"], item["from"])
    else:
        instance_info = Transactiondata(item["id"], item["date"], item["state"], item["operationAmount"],
                                        item["description"], item["to"])
    print(f'{instance_info.data_operation()} {instance_info.status_description()}\n'
          f'{instance_info.sent_from()}{instance_info.sent_to()}\n'
          f'{instance_info.displays_amount()} {instance_info.displays_currency()}\n')