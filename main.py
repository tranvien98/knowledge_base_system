from login import Ui_Login
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QDialog()
ui = Ui_Login(Form)
sys.exit(app.exec_())
