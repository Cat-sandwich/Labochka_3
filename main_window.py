
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

import csv_file
import copy_dataset
import copy_dataset_random_number
import return_path
from PyQt5.QtCore import QThread, QObject
import typing


class CreateDataset(QThread):
    def __init__(self, parent: typing.Optional[QObject]) -> None:
        super().__init__(parent)

    def run(self):
        copy_dataset.copy_dataset_add_csv()

        self.parent().msg.setText("Работа завершена!")
        self.parent().msg.setWindowTitle("СООБЩЕНИЕ")
        self.parent().msg.exec_()


class CreateDatasetRandom(QThread):
    def __init__(self, parent: typing.Optional[QObject]) -> None:
        super().__init__(parent)

    def run(self):
        copy_dataset_random_number.copy_dataset_random_add_csv()


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.create_new_dataset = CreateDataset(self)
        self.create_random_number_dataset = CreateDatasetRandom(self)
        self.current_good = 0
        self.current_bad = 0
        self.path_dataset = ""
        self.initUI()

    def Set_Label(self, x: int, y: int, text: str) -> None:
        """Этот метод устанавливает Label на форму по заданным координатам"""

        reviews = QLabel(text, self)
        reviews.resize(reviews.sizeHint())
        reviews.move(x, y)

    def Set_LineEdit(self, x: int, y: int) -> QTextEdit:
        """Этот метод устанавливает TextEdit на форму по заданным координатам"""

        reviews_edit = QTextEdit(' ', self)
        reviews_edit.resize(400, 500)
        reviews_edit.setReadOnly(True)
        reviews_edit.move(x, y)
        return reviews_edit

    def Set_Button(self, x: int, y: int, text: str, function) -> None:
        """Этот метод устанавливает PushButton на форму по заданным координатам"""

        btn = QPushButton(text, self)
        btn.resize(btn.sizeHint())
        btn.move(x, y)
        btn.clicked.connect(function)
        return btn

    def Set_Widgets(self) -> None:
        """Метод установки всех виджетов на форму"""
        self.Set_Label(180, 50, 'Хороший отзыв')
        self.Set_Label(700, 50, 'Плохой отзыв')

        self.Line_Edit_Good = self.Set_LineEdit(50, 90)
        self.Line_Edit_Bad = self.Set_LineEdit(550, 90)

        self.Set_Button(
            100, 610, 'Посмотреть следующий хороший отзыв', self.On_Next_Good_Review_Button)

        self.Set_Button(
            610, 610, 'Посмотреть следующий плохой отзыв', self.On_Next_Bad_Review_Button)

        self.Set_Button(
            1000, 90, 'Создать аннотацию для dataset', self.On_Create_Csv_Dataset_Button)
        self.Set_Button(
            1000, 140, 'Создать новый dataset и аннотацию для него', self.On_Create_Copy_Dataset_Button)
        self.Set_Button(
            1000, 190, 'Создать рандомный dataset и аннотацию для него', self.On_Create_Dataset_Random_Button)

    def On_Next_Good_Review_Button(self) -> None:
        """Метод для отображения следующего хорошего отзыва"""
        if self.path_dataset != "":
            path = return_path.get_path(
                self.path_dataset + '.csv', 'good', self.current_good)
            self.Line_Edit_Good.setText(
                return_path.find_review_by_path(path))
            self.current_good += 1

    def On_Next_Bad_Review_Button(self) -> None:
        """Метод для отображения следующего плохого отзыва"""
        if self.path_dataset != "":
            path = return_path.get_path(
                self.path_dataset + '.csv', 'bad', self.current_bad)
            self.Line_Edit_Bad.setText(
                return_path.find_review_by_path(path))
            self.current_bad += 1

    def On_Create_Csv_Dataset_Button(self) -> None:
        """Метод для создания csv-файла для датасета"""
        while self.path_dataset == "":
            self.path_dataset = QFileDialog.getExistingDirectory(
                self, 'Выберите папку для датасета')

        csv_file.Create_csv(self.path_dataset)

    def On_Create_Copy_Dataset_Button(self) -> None:
        """Метод для создания нового датасета и его csv-файла"""
        if self.path_dataset != "":
            self.create_new_dataset.start()

    def On_Create_Dataset_Random_Button(self) -> None:
        """Метод для создания рандомного датасета и его csv-файла"""
        if self.path_dataset != "":
            self.create_random_number_dataset.start()

    def initUI(self) -> None:

        self.resize(1400, 700)
        self.center()
        self.Set_Widgets()
        self.msg = QMessageBox()
        self.setWindowTitle('Отзывы')
        self.setWindowIcon(QIcon('web.png'))

    def center(self) -> None:

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


def Init_Application() -> None:
    """создание оконного приложения"""
    app = QApplication(sys.argv)
    ex = Example()
    ex.setStyleSheet("background-image: url(background.jpg)")

    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    Init_Application()
