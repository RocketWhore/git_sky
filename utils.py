import json
#from pprint import pprint
from datetime import datetime

def get_data():
    '''

    :return:
    '''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def get_filtered_data(data, filtred_empty_from):
    '''

    :param data:
    :param filtred_empty_from:
    :return:
    '''
    data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    if filtred_empty_from:
        data = [x for x in data if 'from' in x]
    return data

def get_last_values(data, COUNT_VALUES):
    '''

    :param data:
    :param COUNT_VALUES:
    :return:
    '''
    deta = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:COUNT_VALUES]

def get_formated_data(data):
    '''

    :param data:
    :return:
    '''
    formated_data = []
    for row in data:
        date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        desccription = row['description']
        if 'from' in row:
            sender = row['from'].split()
            from_bill = sender.pop(-1)
            from_bill = f'{from_bill[4:]} {from_bill[4:6]} ** **** {from_bill[-4:]}'
            from_info = ' '.join(sender)
        else:
            from_info, from_bill = 'Счет скрыт', ''
        recipient = row['to'].split()
        recipient_bill = recipient.pop(-1)
        recipient = f'**{recipient_bill[-4:]}'
        to_info = ''.join(recipient)
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formated_data.append(f"""
{date} {desccription}
{from_info} {from_bill} -> {to_info} {recipient_bill}
{amount}
""")
    return formated_data


