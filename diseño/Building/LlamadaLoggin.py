import sys
from Loggin import *

class MainW(QtGui.QMainWindow):
    def __int__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    if __name__ == "__main__":
        app = QtGui.QApplication(sys.argv)
        myapp = MainW()
        myapp = show()
        sys.executable(app .exec_())