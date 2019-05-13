# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chuan_doan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#from main_view import Ui_MainView

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from advice import Ui_Advice
class Ui_Predict(object):
    def __init__(self, a, Dialog):
        self.a = a
        self.Dialog = Dialog
        self.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 131, 28))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 90, 300, 60))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        if self.a == 1 :
            self.label.setText("Bạn được chuẩn đoán: \nmắc bệnh tiểu đường loại 1")
            self.pushButton.clicked.connect(self.openWindow)
        elif self.a == 2:
            self.label.setText("Bạn được chuẩn đoán: \nmắc bệnh tiểu đường loại 2")
            self.pushButton.clicked.connect(self.openWindow)
        else:
            self.label.setText("Bạn được chuẩn đoán: \nkhông mắc bệnh tiểu đường")
            self.pushButton.clicked.connect(Dialog.close)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Kết quả"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Advice(self.window)
        self.Dialog.hide()


if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = Ui_Predict(2, Form)

    sys.exit(app.exec_())
