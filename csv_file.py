import csv
import os.path


def add_to_csv(path_dataset: str, paths_txt: str) -> None:
    """добавление в csv-файл"""
    print("hey")
    with open('dataset.csv', 'w+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Absolute path", "Relative path", "Class"])

        for i in range(1, len(paths_txt)):
            class_txt = str(paths_txt[i]).split('\\')
            print(class_txt[1])
            writer.writerow([f'{ (path_dataset + str(paths_txt[i])).replace(" ","")}',
                            f'..\\dataset{(str(paths_txt[i])).replace(" ","")}', f'{class_txt[1]}'])
            print(i)


def find_path_txt(path_dataset: str) -> str:
    """поиск путей до файлов с отзывами"""
    paths_txt = list()
    class_list = ('\good', '\\bad')

    for folder_name in class_list:
        count = len([f for f in os.listdir(path_dataset + folder_name)
                    if os.path.join(path_dataset + folder_name, f)])

        for j in range(0, count):
            path_txt = folder_name + f'\\{(j): 05}' + '.txt'
            #print(f'{folder_name}: {(j): 05}')
            paths_txt.append(path_txt)

    return paths_txt


if __name__ == "__main__":
    print('Hallo')
    path_dataset = os.path.abspath('dataset')
    print(path_dataset)

    paths_txt = find_path_txt(path_dataset)
    print(paths_txt[1])

    add_to_csv(path_dataset, paths_txt)

    print("Готово!")
