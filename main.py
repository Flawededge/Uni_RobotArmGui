import os
os.system("pyuic5 GUI.ui > GUI.py")

import sys  # Forgot where I actually used this, but it's here
from GUI import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import cv2


class MainPlotGui(Ui_Dialog):
    # The class variables which are used to pass things around
    workingImage = None  # Stores the image shown in the top left

    def __init__(self, dialog):  # Initialization function
        # Set up the GUI
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        # Create then display the image
        self.clear_image()
        self.disp_image(self.workingImage)

    def clear_image(self):
        self.workingImage = np.zeros((150, 250, 3), np.uint8)  # Create the empty image (y, x)
        self.workingImage[:, 0:] = (255, 255, 255)  # Make the image white

    def disp_image(self, image):
        pix = QtGui.QPixmap(QtGui.QImage(image, image.shape[1], image.shape[0],
                                         image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        self.outImg.setPixmap(pix)

    def load_file(self):
        print("thingy 2")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog(flags=(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint |
                                      QtCore.Qt.WindowCloseButtonHint))

    prog = MainPlotGui(dialog)

    dialog.show()
    sys.exit(app.exec_())