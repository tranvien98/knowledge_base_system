# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_view.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from diabetes_ui import Ui_Diabetes
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainView(object):
    def __init__(self, MainWindow):
        self.MainWindow = MainWindow
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        list_Item = self.readProfile('trieu_chung.txt')
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 10, 261, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(750, 100, 251, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 140, 291, 81))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 250, 351, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 250, 111, 31))
        self.pushButton.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(720, 180, 256, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 540, 141, 31))
        self.pushButton_2.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 290, 111, 31))
        self.pushButton_3.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1100, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.display)
        self.comboBox.addItems(list_Item)
        self.pushButton_3.clicked.connect(self.reset)
        self.pushButton_2.clicked.connect(self.openWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainView"))
        self.label.setText(_translate("MainWindow", "Chuẩn đoán bệnh"))
        self.label_2.setText(_translate("MainWindow", "Triệu chứng bệnh"))
        self.label_3.setText(_translate(
            "MainWindow", "Triệu chứng bạn gặp phải"))
        self.pushButton.setText(_translate("MainWindow", "Chọn"))
        self.pushButton_2.setText(_translate("MainWindow", "Tiếp theo"))
        self.pushButton_3.setText(_translate("MainWindow", "Làm mới"))

    def display(self):
        new_list = []
        content = self.textBrowser.toPlainText() + self.comboBox.currentText() + '\n'
        self.textBrowser.setText(content)

    def reset(self):
        self.textBrowser.setText("")

    def readProfile(self, pathFile):
        newlist = []
        f = open(pathFile, "r", encoding='utf-8')
        lines = f.readlines()
        for line in lines:
            newlist.append(line.strip())
        f.close
        return newlist
    def openWindow(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Diabetes(self.window)
        self.MainWindow.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Form = QtWidgets.QMainWindow()
    ui = Ui_MainView(Form)
    sys.exit(app.exec())
