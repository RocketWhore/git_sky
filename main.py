from utils import *


def main():
    # получаем данные
    data = get_data()
    # фильтруем данные
    data = get_filtered_data(data)

    # получаем последние 5 операций

    # выводим данные в формате, заданном в задании
    data = get_formated_data(data)


if __name__ == '__main__':
    main()
