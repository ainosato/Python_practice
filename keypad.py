# -*- coding: utf-8 -*-

import sys

import PyQt5
import sys, pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

PadUI = '../_uiFiles/keypad.ui'
SaveUI = '../_uiFiles/saved.ui'
MainUI = '../_uiFiles/main.ui'
OutUI = '../_uiFiles/out.ui'
OutcarUI = '../_uiFiles/outcar.ui'

class sql(QWidget):
    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()
        self.enterEvent()

    def sqlConnect(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="apmsetup",
                db="opentutorials",
                port=3306,
                charset="utf8"
            )
        except:
            print("문제 발생")
            exit(1)
        print("연결 성공")
        self.cur = self.conn.cursor()

    def initUI(self):
        Main = MainDialog()
        Main.exec_()

    def closeEvent(self, QCloseEvent):
        print("close")
        self.conn.close()

class MainDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(MainUI, self)
        self.in_pushButton.clicked.connect(self.go)
        self.out_pushButton.clicked.connect(self.out)
        self.sqlConnect()

    def sqlConnect(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="apmsetup",
                db="opentutorials",
                port=3306,
                charset="utf8"
            )
        except:
            print("문제 발생")
            exit(1)
        print("연결 성공")
        self.cur = self.conn.cursor()

    def go(self):
        self.close()
        pad = KeypadDialog()
        pad.exec_()

    def out(self):
        self.close()
        out = outDialog()
        out.exec_()


class KeypadDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(PadUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button = self.num_pushButton_0 : self.NumClicked(state, button))

        self.del_pushButton.clicked.connect(self.Delete)
        self.enter_pushButton.clicked.connect(self.checkAnswer)
        self.home_pushButton.clicked.connect(self.home)

    def enterEvent(self, QEvent):
        self.cmd = "SELECT * FROM keypad"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

    def NumClicked(self, state, button):
        exist_line_text = self.q_lineEdit.text()
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

    def checkAnswer(self):
        self.close()
        Save = SaveDialog()
        Save.exec_()

    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()


class SaveDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(SaveUI, self)
        self.home_pushButton.clicked.connect(self.home)

    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()



class outDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(OutUI, self)

        self.num_pushButton_1.clicked.connect(lambda state, button = self.num_pushButton_1 : self.NumClicked(state, button))
        self.num_pushButton_2.clicked.connect(lambda state, button = self.num_pushButton_2 : self.NumClicked(state, button))
        self.num_pushButton_3.clicked.connect(lambda state, button = self.num_pushButton_3 : self.NumClicked(state, button))
        self.num_pushButton_4.clicked.connect(lambda state, button = self.num_pushButton_4 : self.NumClicked(state, button))
        self.num_pushButton_5.clicked.connect(lambda state, button = self.num_pushButton_5 : self.NumClicked(state, button))
        self.num_pushButton_6.clicked.connect(lambda state, button = self.num_pushButton_6 : self.NumClicked(state, button))
        self.num_pushButton_7.clicked.connect(lambda state, button = self.num_pushButton_7 : self.NumClicked(state, button))
        self.num_pushButton_8.clicked.connect(lambda state, button = self.num_pushButton_8 : self.NumClicked(state, button))
        self.num_pushButton_9.clicked.connect(lambda state, button = self.num_pushButton_9 : self.NumClicked(state, button))
        self.num_pushButton_0.clicked.connect(lambda state, button = self.num_pushButton_0 : self.NumClicked(state, button))

        self.del_pushButton.clicked.connect(self.Delete)
        self.enter_pushButton.clicked.connect(self.checkAnswer)
        self.home_pushButton.clicked.connect(self.home)


    def NumClicked(self, state, button):
        exist_line_text = self.q_lineEdit.text()
        now_num_text = button.text()
        self.q_lineEdit.setText(exist_line_text + now_num_text)

    def Delete(self):
        exist_line_text = self.q_lineEdit.text()
        exist_line_text = exist_line_text[:-1]
        self.q_lineEdit.setText(exist_line_text)

    def checkAnswer(self):
        self.close()
        car = OutcarDialog()
        car.exec_()

    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()

class OutcarDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(OutcarUI, self)
        self.home_pushButton.clicked.connect(self.home)

    def home(self):
        self.close()
        Main = MainDialog()
        Main.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = sql()
    s.show()
    Main = MainDialog()
    app.exec_()