import csv
import os
import random
import shutil


def add_to_csv_and_to_dataset_random_number(path_dataset: str, paths_txt: str) -> None:
    """создание csv-файла и копирование в dataset_random_number"""

    name_folder = "dataset_random_number"

    if not os.path.isdir(name_folder):
        os.mkdir(name_folder)

    path_dataset_random_number = os.path.abspath(name_folder)

    with open('dataset_random_number.csv', 'w+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Absolute path", "Relative path", "Class"])

        for i in range(0, len(paths_txt)):
            class_txt = str(paths_txt[i]).split('\\')
            new_name = str(random.randint(0, 10001)).zfill(5) + '.txt'
            while os.path.isfile(new_name):
                new_name = str(random.randint(0, 10001)).zfill(5) + '.txt'
            writer.writerow([f'{ (path_dataset_random_number) }\{ new_name }',
                            f'..\\dataset_random_number\{new_name}', f'{class_txt[1]}'])
            shutil.copyfile(
                path_dataset + str(paths_txt[i]), path_dataset_random_number + '\\' + new_name)


def find_path_txt(path_dataset: str) -> None:
    """поиск путей до файлов с отзывами"""
    paths_txt = list()
    class_list = ('\good', '\\bad')

    for folder_name in class_list:
        count = len([f for f in os.listdir(path_dataset + folder_name)
                    if os.path.join(path_dataset + folder_name, f)])

        for j in range(0, count):
            path_txt = folder_name + f'\\{(j): 05}' + '.txt'

            paths_txt.append(path_txt.replace(" ", ""))

    return paths_txt


def copy_dataset_random_add_csv() -> None:
    """функция, выполняющая копирование файлов с рандомными номерами в новый dataset и делающая csv-файл к нему"""
    path_dataset = os.path.abspath('dataset')
    paths_txt = find_path_txt(path_dataset)
    add_to_csv_and_to_dataset_random_number(path_dataset, paths_txt)
    print('Работа завершена!')


if __name__ == "__main__":

    print('Hallo')
    path_laba_2 = os.getcwd()
    path_dataset = os.path.abspath('dataset')
    print(path_dataset)
    paths_txt = find_path_txt(path_dataset)
    add_to_csv_and_to_dataset_random_number(path_dataset, paths_txt)

    print("Готово!")
