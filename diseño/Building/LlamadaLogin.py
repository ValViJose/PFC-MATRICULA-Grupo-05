import sys
from Login import *
from PyQt6 import QtCore, QtGui, QtWidgets

class MainW(QtGui.QDialog):
    def __int__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MainW()
        myapp.show()
        sys.exit(app.exec_())