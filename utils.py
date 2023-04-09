import json
# from pprint import pprint
from datetime import datetime


def get_data():
    '''

    :return: данные в формате list
    '''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):
    '''

    :param data: данные в формате list
    :param filtred_empty_from: наличие from (T/F)
    :return:
    '''
    data = [x for x in data if x.get('state') == 'EXECUTED']
    data = sorted(data, key=lambda x: x['date'], reverse=True)

    return data[:5]



#def get_last_values(data, COUNT_VALUES):

#    deta = sorted(data, key=lambda x: x['date'], reverse=True)
#    return data[:COUNT_VALUES]
def get_date_str(date_str):
    date_list = date_str[:10].split('-')
    return '.'.join(reversed(date_list))

def mask_card(card):
    card = card.split(' ')
    if card[0] == 'Счет':
        return f'Счет **{card[-1][:-4]}'
    return f'{" ".join(card[:-1])} {card[-1][:4]} {card[-1][4:6]}** **** {card[-1][-4:]}'

def get_formated_data(data_):
    for x in data_:
        formated_data = get_date_str(x['date'])

        if x.get('from'):
            from_ = mask_card(x.get('from')) + ' -> '
        else:
            from_ = ''

        to_ = mask_card(x.get('to'))

        print(f'{formated_data} {x["description"]}\n'
              f'{from_}{to_}\n'
              f'{x["operationAmount"]["amount"]} {x["operationAmount"]["currency"]["name"]}\n')



# def get_formated_data(data):
#     '''
#
#     :param data: отсортированные данные для форматирования и вывода
#     :return:
#     '''
#     formated_data = []
#     for row in data:
#         date = datetime.strptime(row['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
#         desccription = row['description']
#         if 'from' in row:
#             sender = row['from'].split()
#             from_bill = sender.pop(-1)
#             from_bill = f'{from_bill[4:]} {from_bill[4:6]} ** **** {from_bill[-4:]}'
#             from_info = ' '.join(sender)
#         else:
#             from_info, from_bill = 'Счет скрыт', ''
#         recipient = row['to'].split()
#         recipient_bill = recipient.pop(-1)
#         recipient = f'**{recipient_bill[-4:]}'
#         to_info = ''.join(recipient)
#         amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
#         formated_data.append(f"""
# {date} {desccription}
# {from_info} {from_bill} -> {to_info} {recipient_bill}
# {amount}
# """)
#     return formated_data
