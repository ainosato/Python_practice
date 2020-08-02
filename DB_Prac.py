import sys, pymysql
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTreeView
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import Qt

class sql(QWidget):
    def __init__(self):
        super().__init__()
        self.sqlConnect()
        self.initUI()
        self.run()

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
        self.setGeometry(300, 300, 500, 520)
        self.setWindowTitle("데이터베이스 활용 예제")

        self.show()

    def enterEvent(self, QEvent):
        self.cmd = "SELECT * FROM login"
        self.cur.execute(self.cmd)
        self.conn.commit()
        ar = self.cur.fetchall()

    def run(self):
        self.cmd = "desc login"
        self.cur.execute(self.cmd)
        self.conn.commit()
        print(self.cur.fetchall())

    def closeEvent(self, QCloseEvent):
        print("close")
        self.conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    s = sql()
    s.show()
    app.exec_()