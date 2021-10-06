import sys
from PyQt5 import QtSql
from PyQt5 import uic
from PyQt5 import QtWidgets

class main_window(QtWidgets.QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.conn()
        self.

    def conn(self):
        db = QtSql.QSqlDatabase("QPSQL")
        db.setHostName('localhost')
        db.setPort(5432)
        db.setDatabaseName('kursach')
        db.setUserName('postgres')
        db.setPassword('1234')
        if db.open():
            print("Ready")
        else:
            print(db.lastError().text())

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)