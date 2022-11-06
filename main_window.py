
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def Set_Label(self, x: int, y: int, text: str) -> None:
        """Этот метод устанавливает Label на форму по заданным координатам"""

        reviews = QLabel(text, self)
        reviews.resize(reviews.sizeHint())
        reviews.move(x, y)

    def Set_LineEdit(self, x: int, y: int) -> None:
        """Этот метод устанавливает LineEdit на форму по заданным координатам"""

        reviews_edit = QLineEdit(' ', self)
        reviews_edit.resize(400, 500)
        reviews_edit.setReadOnly(True)
        reviews_edit.move(x, y)

    def Set_Button(self, x: int, y: int, text: str) -> None:
        """Этот метод устанавливает PushButton на форму по заданным координатам"""

        btn = QPushButton(text, self)
        btn.resize(btn.sizeHint())
        btn.move(x, y)

    def Set_Widgets(self) -> None:
        """Метод установки всех виджетов на форму"""
        self.Set_Label(180, 50, 'Хороший отзыв')
        self.Set_Label(700, 50, 'Плохой отзыв')

        self.Set_LineEdit(50, 90)
        self.Set_LineEdit(550, 90)

        self.Set_Button(
            100, 610, 'Посмотреть следующий хороший отзыв')
        self.Set_Button(
            610, 610, 'Посмотреть следующий плохой отзыв')

        self.Set_Button(
            1000, 90, 'Создать аннотацию для dataset')
        self.Set_Button(
            1000, 140, 'Создать новый dataset и аннотацию для него')
        self.Set_Button(
            1000, 190, 'Создать рандомный dataset и аннотацию для него')

    def initUI(self) -> None:

        self.resize(1400, 700)
        self.center()
        self.Set_Widgets()

        self.setWindowTitle('Отзывы')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def center(self) -> None:

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
