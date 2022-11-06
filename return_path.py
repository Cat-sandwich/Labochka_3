from iterator import Iterator


def get_path(file_name: str, class_name: str, index: int) -> str:
    """получение путей файлов"""

    i = Iterator(file_name, class_name)
    if index >= len(i.list):
        index = 0

    for path in i:
        num = int(i.get_number_review())
        if (path != None) and num == index:
            return path


def find_review_by_path(path_txt: str) -> str:
    text = ''
    with open(path_txt, 'r', encoding='utf-8') as file:
        for item in file:
            text += item
    return text


if __name__ == "__main__":
    file_name = 'dataset.csv'
    class_name = 'good'
    print(get_path(file_name, class_name, 0))
    print(get_path(file_name, class_name, 77))
