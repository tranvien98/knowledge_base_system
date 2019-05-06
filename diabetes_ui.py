# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'diabetes_ui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from knn import knn
from chuan_doan import Ui_Predict
import numbers

class Ui_Diabetes(object):
    def __init__(self, Dialog):
        self.Dialog = Dialog
        self.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(900, 600)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 10, 451, 100))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(250, 150, 150, 40))
        self.lineEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 230, 150, 40))
        self.lineEdit_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 310, 150, 40))
        self.lineEdit_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 390, 150, 40))
        self.lineEdit_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(80, 230, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(80, 150, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 310, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(80, 390, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(470, 150, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(470, 230, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(430, 310, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(470, 390, 150, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(640, 150, 150, 40))
        self.lineEdit_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_5.setObjectName("lineEdit_5")

        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(640, 230, 150, 40))
        self.lineEdit_6.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(640, 310, 150, 40))
        self.lineEdit_7.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_7.setObjectName("lineEdit_7")

        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(640, 390, 150, 40))
        self.lineEdit_8.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_8.setObjectName("lineEdit_8")

        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 500, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 500, 130, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.move)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Chuẩn đoán"))
        self.label.setText(_translate("Dialog", "Chuẩn đoán bệnh tiểu đường"))
        self.label_2.setText(_translate("Dialog", "Glucose"))
        self.label_3.setText(_translate("Dialog", "Pregnancies"))
        self.label_4.setText(_translate("Dialog", "BloodPressure"))
        self.label_5.setText(_translate("Dialog", "SkinThickness"))
        self.label_6.setText(_translate("Dialog", "Insulin"))
        self.label_7.setText(_translate("Dialog", "BMI"))
        self.label_8.setText(_translate("Dialog", "DiabetesPedigreeFunction"))
        self.label_9.setText(_translate("Dialog", "Age"))
        self.pushButton.setText(_translate("Dialog", "OK"))
        self.pushButton_2.setText(_translate("Dialog", "Cancle"))

    def move(self):
    
        a = []
        Pregnancies = self.lineEdit.text()
        Glucose = self.lineEdit_2.text()
        BloodPressure = self.lineEdit_3.text()
        SkinThickness = self.lineEdit_4.text()
        Insulin = self.lineEdit_5.text()
        Bmi = self.lineEdit_6.text()
        DiabetesPedigreeFunction = self.lineEdit_7.text()
        Age = self.lineEdit_8.text()
        print(isinstance(12, numbers.Real))
        if (len(Pregnancies) != 0 and 
            len(Glucose) != 0 and 
            len(BloodPressure) != 0 and 
            len(SkinThickness) != 0 and 
            len(Insulin) != 0 and 
            len(Bmi) != 0 and
            len(DiabetesPedigreeFunction) != 0 and 
            len(Age) != 0 ):
            a.append(float(Pregnancies))
            a.append(float(Glucose))
            a.append(float(BloodPressure))
            a.append(float(SkinThickness))
            a.append(float(Insulin))
            a.append(float(Bmi))
            a.append(float(DiabetesPedigreeFunction))
            a.append(float(Age))
            model = knn('diabetes.csv')
            output = model.predict([a])
            self.openWindow(output[0])
        else :
            self.warning("Cảnh báo", "Bạn nhập sai")
         

 

    def warning(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()
    def openWindow(self, b):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Predict(b,self.window)
        self.Dialog.hide()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    Form = QtWidgets.QDialog()
    ui = Ui_Diabetes(Form)

    sys.exit(app.exec())
