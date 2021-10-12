from PyQt5 import QtWidgets, QtSql, QtCore
from PyQt5.QtCore import *
from window_layout import Ui_MainWindow
import sys


def conn(self):
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName('localhost')
    db.setPort(5432)
    db.setDatabaseName("mmo_db")
    db.setUserName('postgres')
    db.setPassword('1234')

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Добавляем новые значения
        self.ui.comboBox.addItem("Regions")
        self.ui.comboBox.addItem("Languages")
        self.ui.comboBox.addItem("Servers")
        self.ui.comboBox.addItem("Game worlds")
        self.ui.comboBox.addItem("Characters")
        self.ui.comboBox.addItem("Users")
        conn(self)
        self.ui.comboBox.activated.connect(self.switch_case)
        temp = QtSql.QSqlTableModel()
        def remove_row():
            temp.removeRow(temp.rowCount()-1)
            temp.submitAll()
            temp.select()
        def add_row():
            temp.insertRow(temp.rowCount())
            temp.submitAll()
        tab = 'regions'
        temp.setTable(tab)
        temp.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        temp.setHeaderData(0, Qt.Horizontal, 'Region')
        temp.select()
        self.ui.tableView.setModel(temp)
        self.ui.pushButton.clicked.connect(add_row)
        self.ui.pushButton_2.clicked.connect(remove_row)


    def pass_combobox_text(self):
        return str(self.ui.comboBox.currentText())

    def switch_case(self):
        def remove_row():
            model.removeRow(model.rowCount()-1)
            model.submitAll()
            model.select()
        def add_row():
            model.insertRow(model.rowCount())
            model.submitAll()
        if (self.pass_combobox_text() == "Regions"):
            model = QtSql.QSqlTableModel()
            tab = 'regions'
            model.setTable(tab)
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.setHeaderData(0, Qt.Horizontal, 'Region')
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.pushButton.clicked.connect(add_row)
            self.ui.pushButton_2.clicked.connect(remove_row)
        if (self.pass_combobox_text() == "Languages"):
            model = QtSql.QSqlTableModel()
            tab = 'languages'
            model.setTable(tab)
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.setHeaderData(0, Qt.Horizontal, 'Language')
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.pushButton.clicked.connect(add_row)
            self.ui.pushButton_2.clicked.connect(remove_row)
        if (str(self.ui.comboBox.currentText()) == "Servers"):
            model = QtSql.QSqlTableModel()
            tab = 'servers'
            model.setTable(tab)
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.setHeaderData(0, Qt.Horizontal, 'Region')
            model.setHeaderData(1, Qt.Horizontal, 'Language')
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.pushButton.clicked.connect(add_row)
            self.ui.pushButton_2.clicked.connect(remove_row)
        if (str(self.ui.comboBox.currentText()) == "Characters"):
            model = QtSql.QSqlTableModel()
            tab = 'chars'
            model.setTable(tab)
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.setHeaderData(0, Qt.Horizontal, 'Game World')
            model.setHeaderData(1, Qt.Horizontal, 'Character name')
            model.setHeaderData(2, Qt.Horizontal, 'Character level')
            model.setHeaderData(3, Qt.Horizontal, 'Experience points')
            model.setHeaderData(4, Qt.Horizontal, 'Character faction')
            model.setHeaderData(5, Qt.Horizontal, 'User')
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.pushButton.clicked.connect(add_row)
            self.ui.pushButton_2.clicked.connect(remove_row)
        if (str(self.ui.comboBox.currentText()) == "Game worlds"):
            model = QtSql.QSqlTableModel()
            tab = 'game_worlds'
            model.setTable(tab)
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.setHeaderData(0, Qt.Horizontal, 'Game World name')
            model.setHeaderData(1, Qt.Horizontal, 'Server Region')
            model.setHeaderData(2, Qt.Horizontal, 'Server Language')
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.pushButton.clicked.connect(add_row)
        if (str(self.ui.comboBox.currentText()) == "Users"):
            model = QtSql.QSqlTableModel()
            tab = 'users'
            model.setTable(tab)
            model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
            model.setHeaderData(0, Qt.Horizontal, 'Username')
            model.select()
            self.ui.tableView.setModel(model)
            self.ui.pushButton.clicked.connect(add_row)
            self.ui.pushButton_2.clicked.connect(remove_row)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

# def initializeModel(model):
#    model.setTable('sportsmen')
#    model.setEditStrategy(QSqlTableModel.OnFieldChange)
#    model.select()
#
# def createView(title, model):
#    view = QTableView()
#    view.setModel(model)
#    view.setWindowTitle(title)
#    return view
#
# def addrow():
#    print (model.rowCount())
#    ret = model.insertRows(model.rowCount(), 1)
#    print (ret)
#
# def findrow(i):
#    delrow = i.row()
#
# if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    db = QSqlDatabase.addDatabase('QPSQL')
#    db.setHostName('localhost')
#    db.setPort(5432)
#    db.setDatabaseName("kursach")
#    db.setUserName('postgres')
#    db.setPassword('1234')
#    model = QSqlTableModel()
#    delrow = -1
#    initializeModel(model)
#
#    view1 = createView("Table Model (View 1)", model)
#    view1.clicked.connect(findrow)
#
#    dlg = QDialog()
#    layout = QVBoxLayout()
#    layout.addWidget(view1)
#
#    button = QPushButton("Add a row")
#    button.clicked.connect(addrow)
#    layout.addWidget(button)
#
#    btn1 = QPushButton("del a row")
#    btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
#    layout.addWidget(btn1)
#
#    dlg.setLayout(layout)
#    dlg.setWindowTitle("Database Demo")
#    dlg.show()
#    sys.exit(app.exec_())