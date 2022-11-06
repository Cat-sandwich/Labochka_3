from iterator import Iterator


def get_path(file_name: str, class_name: str) -> None:
    """получение путей файлов"""

    i = Iterator(file_name, class_name)
    for val in i:
        if (val != None):
            print(val)

    print('Готово')


if __name__ == "__main__":
    file_name = 'dataset.csv'
    class_name = 'good'
    get_path(file_name, class_name)
