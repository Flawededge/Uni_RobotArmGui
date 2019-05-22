import os
os.system("pyuic5 GUI.ui > GUI.py")

import sys  # Forgot where I actually used this, but it's here
from GUI import Ui_Dialog
from PyQt5 import QtWidgets, QtCore


class MainPlotGui(Ui_Dialog):
    # The class variables which are used to pass things around

    def __init__(self, dialog):  # Initialization function
        # Set up the GUI
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog(flags=(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint |
                                      QtCore.Qt.WindowCloseButtonHint))

    prog = MainPlotGui(dialog)

    dialog.show()
    sys.exit(app.exec_())