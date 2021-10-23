from PyQt5 import QtSql
import func.config as config

def conn():
    db = QtSql.QSqlDatabase.addDatabase('QPSQL')
    db.setHostName(config.DB_HOST)
    db.setPort(config.DB_PORT)
    db.setDatabaseName(config.DB_DATABASE_NAME)
    db.setUserName(config.DB_USERNAME)
    db.setPassword(config.DB_PASSWORD)