from PyQt5 import QtWidgets
from cls.mywindow import mywindow
import sys


app = QtWidgets.QApplication(sys.argv)
application = mywindow()
application.show()

sys.exit(app.exec())
