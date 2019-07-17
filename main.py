from PySide import QtCore, QtGui
import sys
from ui import Ui_Dialog

# if __name__ == "__main__":


# creat application
app = QtGui.QApplication(sys.argv)

# creat form and init UI
Dialog = QtGui.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()


# hook  logic
def bp():
    ui.lineEdit.setText("Hello, world")

ui.pushButton_10.clicked.connect(bp)

# run main loop
sys.exit(app.exec_())





