from PyQt5 import QtWidgets
from knn import knn
from main_view import Ui_MainWindow
import sys


class mylogin(QtWidgets.QMainWindow):

    def __init__(self):
        super(mylogin, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)



app = QtWidgets.QApplication([])

application = mylogin()

application.show()

sys.exit(app.exec())
