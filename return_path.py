from iterator import Iterator


def get_path(file_name: str, class_name: str, index: int) -> str:
    """получение путей файлов"""

    i = Iterator(file_name, class_name)
    if len(i.list) >= index:
        index = 0

    for path in i:
        if (path != None):
            return path


def find_review_by_path(path_txt: str) -> list:
    text = list
    with open(path_txt, 'r', encoding='utf-8') as file:
        for item in file:
            text.append(item)
    return text


if __name__ == "__main__":
    file_name = 'dataset.csv'
    class_name = 'good'
    print(get_path(file_name, class_name))
    print(get_path(file_name, class_name))
