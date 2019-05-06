from PyQt5 import QtWidgets
from knn import knn
from diabetes_ui import Ui_Dialog
import sys
 
class mywindow(QtWidgets.QDialog):
 
	def __init__(self):
		super(mywindow, self).__init__()
		self.ui = Ui_Dialog()
		self.ui.setupUi(self) 
		self.ui.pushButton.clicked.connect(self.move)
	def move(self):
		a =  []
		Pregnancies = self.ui.lineEdit.text()
		Glucose = self.ui.lineEdit_2.text()
		BloodPressure = self.ui.lineEdit_3.text()
		SkinThickness = self.ui.lineEdit_4.text()
		Insulin = self.ui.lineEdit_5.text()
		BMI = self.ui.lineEdit_6.text()
		DiabetesPedigreeFunction = self.ui.lineEdit_7.text()
		Age = self.ui.lineEdit_8.text()
		a.append(float(Pregnancies))
		a.append(float(Glucose))
		a.append(float(BloodPressure))
		a.append(float(SkinThickness))
		a.append(float(Insulin))
		a.append(float(BMI))
		a.append(float(DiabetesPedigreeFunction))
		a.append(float(Age))
		print(a)
		model = knn('diabetes.csv')
		output = model.predict([a])
		print(output[0])
app = QtWidgets.QApplication([])
 
application = mywindow()
 
application.show()
 
sys.exit(app.exec())