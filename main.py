from utils import get_data, get_filtered_data, get_last_values, get_formated_data
from pprint import pprint

def main():
    COUNT_VALUES = 5
    FILTRED_EMPTY_FROM = True

    # получаем данные
    data = get_data()
    # фильтруем данные
    data = get_filtered_data(data, FILTRED_EMPTY_FROM)
    print(data)
    #
    data = get_last_values(data, COUNT_VALUES)
    #
    data = get_formated_data(data)


    for row in data:
        print(row, end='\n')
        print()

if __name__ == '__main__':
    main()