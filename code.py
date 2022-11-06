
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self) -> None:

        self.resize(1000, 700)
        self.center()

        good_reviews = QLabel('Хорошие отзывы', self)
        good_reviews.resize(good_reviews.sizeHint())
        good_reviews.move(100, 10)

        bad_reviews = QLabel('Плохие отзывы', self)
        bad_reviews.resize(bad_reviews.sizeHint())
        bad_reviews.move(750, 10)
        good_reviews_edit = QLineEdit('', self)
        bad_reviews_edit = QLineEdit('', self)

        #grid = QGridLayout()
        # grid.setSpacing(10)

        #grid.addWidget(good_reviews, 1, 2)
        #grid.addWidget(good_reviews_edit,  3, 1, 5, 1)

        #grid.addWidget(bad_reviews, 1, 1)
        #grid.addWidget(bad_reviews_edit,  3, 1, 5, 1)

        # self.setLayout(grid)

        btn = QPushButton('Кнопка', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
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
