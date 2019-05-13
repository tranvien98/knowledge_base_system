# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'advice.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Advice(object):
    def __init__(self, Dialog):
        self.Dialog = Dialog
        self.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(550, 400)
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(60, 80, 421, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 381, 31))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(220, 340, 100, 30))
        self.pushButton.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        advice = self.readFile("advice.txt")
        self.textBrowser.setText(advice)
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Lời khuyên"))
        self.label.setText(_translate("Dialog", "Một số lời khuyên"))
        self.pushButton.setText(_translate("Dialog", "OK"))

    def readFile(self, pathFile):
        newlist = " "
        f = open(pathFile, "r", encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            newlist = newlist + "\n" + line
        f.close
        return newlist
if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = Ui_Advice(Form)
    sys.exit(app.exec_())
