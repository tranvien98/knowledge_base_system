# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main_view import Ui_MainView
class Ui_Login(object):
    def __init__(self, Dialog):
        self.Dialog = Dialog
        self.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 296)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 60, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 55, 16))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 60, 113, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 140, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login"))
        self.label.setText(_translate("Dialog", "user"))
        self.label_2.setText(_translate("Dialog", "password"))
        self.pushButton.setText(_translate("Dialog", "Login"))
    def login(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if True:
            print("helo")
            self.openWindow()
            
        else:
            self.warning('Cảnh báo', 'Bạn nhập sai mật khẩu')
    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainView(self.window)
        self.Dialog.hide()



if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = Ui_Login(Form)
    sys.exit(app.exec_())
