from PyQt5 import QtWidgets, QtSql
from PyQt5.QtCore import *
from win_lay import Ui_MainWindow
from lxml import etree
import sys
import config
import os

def conn(self):
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName(config.DB_HOST)
    db.setPort(config.DB_PORT)
    db.setDatabaseName(config.DB_DATABASE_NAME)
    db.setUserName(config.DB_USERNAME)
    db.setPassword(config.DB_PASSWORD)

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
        def save_new_row():
            temp.submitAll()
            temp.select()
        tab = 'regions'
        temp.setTable(tab)
        temp.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        temp.setHeaderData(0, Qt.Horizontal, 'Region')
        temp.select()
        self.ui.tableView.setModel(temp)
        self.ui.pushButton.clicked.connect(add_row)
        self.ui.pushButton_3.clicked.connect(self.export_table_to_xml)
        self.ui.pushButton_2.clicked.connect(remove_row)
        self.ui.pushButton_4.clicked.connect(save_new_row)
        self.ui.pushButton_5.clicked.connect(self.import_xml)

    def export_table_to_xml(self):
        current_table = self.pass_combobox_text()
        query = "select table_to_xml('"  + current_table + "', true, false, '')"
        xmlpath = current_table + ".xml"
        q = QtSql.QSqlQuery()
        q.exec(query)
        with open(xmlpath, "w") as f:
            while (q.next()):
                xml = str(q.value(0))
                xml = xml.replace(' xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"','')
                f.write(xml)

    def import_xml(self):
        selectfile, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Select table for import', '', '.XML files(*.xml)')
        fname = selectfile.rstrip(os.sep)
        r = etree.parse(fname)
        t = r.getroot()
        tablename = t.tag
        query = QtSql.QSqlQuery()
        q = "select column_name from information_schema.columns where table_schema = 'public' and table_name = '" + tablename + "'"
        query.exec(q)
        while query.next():
            print(query.value(0))



    def pass_combobox_text(self):
        return str(self.ui.comboBox.currentText())

    def switch_case(self):
        def remove_row():
            model.removeRow(model.rowCount()-1)
            model.submitAll()
            model.select()
        def add_row():
            model.insertRow(model.rowCount())
        def save_new_row():
            model.submitAll()
            model.select()
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
            self.ui.pushButton_4.clicked.connect(save_new_row)
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
            self.ui.pushButton_4.clicked.connect(save_new_row)
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
            self.ui.pushButton_4.clicked.connect(save_new_row)
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
            self.ui.pushButton_4.clicked.connect(save_new_row)
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
            self.ui.pushButton_2.clicked.connect(remove_row)
            self.ui.pushButton_4.clicked.connect(save_new_row)
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
            self.ui.pushButton_4.clicked.connect(save_new_row)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())
