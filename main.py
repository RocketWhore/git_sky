from utils import *

def main():
    COUNT_VALUES = 5


    # получаем данные
    data = get_data()
    # фильтруем данные
    data = get_filtered_data(data, COUNT_VALUES)

    # получаем последние 5 операций
 #  data = get_last_values(data, COUNT_VALUES)
    # выводим данные в формате, заданном в задании
    data = get_formated_data(data)

    # for row in data:
    #     print(row, end='\n')
    #     print()


if __name__ == '__main__':
    main()
