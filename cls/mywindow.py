from PyQt5 import QtWidgets, QtSql
from PyQt5.QtCore import *
from cls.win_lay import Ui_MainWindow
from lxml import etree
from func.connection import conn
import os


class mywindow(QtWidgets.QMainWindow):
    conn()
    model = QtSql.QSqlTableModel()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.comboBox.addItem("Regions")
        self.ui.comboBox.addItem("Languages")
        self.ui.comboBox.addItem("Servers")
        self.ui.comboBox.addItem("Game worlds")
        self.ui.comboBox.addItem("Characters")
        self.ui.comboBox.addItem("Users")

        self.ui.comboBox.activated.connect(self.switch_case)

        tab = 'regions'
        self.model.setTable(tab)
        self.model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.model.setHeaderData(0, Qt.Horizontal, 'Region')
        self.model.select()
        self.ui.tableView.setModel(self.model)
        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_3.clicked.connect(self.export_table_to_xml)
        self.ui.pushButton_2.clicked.connect(self.remove_row)
        self.ui.pushButton_4.clicked.connect(self.save_new_row)
        self.ui.pushButton_5.clicked.connect(self.import_xml)

    def remove_row(self):
        self.model.removeRow(self.model.rowCount() - 1)
        self.model.submitAll()
        self.model.select()

    def add_row(self):
        self.model.insertRow(self.model.rowCount())

    def save_new_row(self):
        self.model.submitAll()
        self.model.select()

    def export_table_to_xml(self):
        current_table = self.pass_combobox_text()
        query = "select table_to_xml('"  + current_table + "', true, false, '')"
        xmlpath = current_table + ".xml"
        q = QtSql.QSqlQuery()
        q.exec(query)
        with open(xmlpath, "w") as f:
            while (q.next()):
                xml = str(q.value(0))
                xml = xml.replace('xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"','')
                f.write(xml)

    def import_xml(self):
        FileDialog = QtWidgets.QFileDialog()
        selectfile, _ = FileDialog.getOpenFileName(self, 'Select table for import', '', '.XML files(*.xml)')
        fname = selectfile.rstrip(os.sep)
        if not selectfile == "":
            parse = etree.parse(fname)
            root = parse.getroot()
            tablename = root.tag
            query = QtSql.QSqlQuery()
            q = "select column_name from information_schema.columns where table_schema = 'public' and table_name = '" + tablename + "'"
            query.exec(q)
            columns = []
            while query.next():
                columns.append(str(query.value(0)))
            q2 = "insert into " + tablename + " ("
            for i in range(len(columns)):
                if (i == len(columns) - 1):
                    q2 = q2 + columns[i] + ")"
                else:
                    q2 = q2 + columns[i] + ", "
            q2 = q2 + " values (" + ("?, " * len(columns))
            q2 = q2[:-2] + ")"
            query2 = QtSql.QSqlQuery()
            query2.prepare(q2)
            rows = root.findall(".//row")
            for i in range(len(rows)):
                row = str.split(etree.tostring(rows[i], method="text").decode())
                for col_ind in range(len(row)):
                    query2.bindValue(col_ind, row[col_ind])
                query2.exec_()
            self.model.select()

    def pass_combobox_text(self):
        return str(self.ui.comboBox.currentText())

    def switch_case(self):
        if (self.pass_combobox_text() == "Regions"):
            tab = 'regions'
            self.model.setTable(tab)
            self.model.setHeaderData(0, Qt.Horizontal, 'Region')
            self.model.select()
        if (self.pass_combobox_text() == "Languages"):
            tab = 'languages'
            self.model.setTable(tab)
            self.model.setHeaderData(0, Qt.Horizontal, 'Language')
            self.model.select()
        if (str(self.ui.comboBox.currentText()) == "Servers"):
            tab = 'servers'
            self.model.setTable(tab)
            self.model.setHeaderData(0, Qt.Horizontal, 'Region')
            self.model.setHeaderData(1, Qt.Horizontal, 'Language')
            self.model.select()
        if (str(self.ui.comboBox.currentText()) == "Characters"):
            tab = 'chars'
            self.model.setTable(tab)
            self.model.setHeaderData(0, Qt.Horizontal, 'Game World')
            self.model.setHeaderData(1, Qt.Horizontal, 'Character name')
            self.model.setHeaderData(2, Qt.Horizontal, 'Character level')
            self.model.setHeaderData(3, Qt.Horizontal, 'Experience points')
            self.model.setHeaderData(4, Qt.Horizontal, 'Character faction')
            self.model.setHeaderData(5, Qt.Horizontal, 'User')
            self.model.select()
        if (str(self.ui.comboBox.currentText()) == "Game worlds"):
            tab = 'game_worlds'
            self.model.setTable(tab)
            self.model.setHeaderData(0, Qt.Horizontal, 'Game World name')
            self.model.setHeaderData(1, Qt.Horizontal, 'Server Region')
            self.model.setHeaderData(2, Qt.Horizontal, 'Server id')
            self.model.select()
        if (str(self.ui.comboBox.currentText()) == "Users"):
            tab = 'users'
            self.model.setTable(tab)
            self.model.setHeaderData(0, Qt.Horizontal, 'Username')
            self.model.select()
