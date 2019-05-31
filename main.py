# pip install -r dependencies.txt
import os
os.system("pyuic5 GUI.ui > GUI.py")

import sys  # Forgot where I actually used this, but it's here
from GUI import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import cv2
import serial


class MainPlotGui(Ui_Dialog):
    # The class variables which are used to pass things around
    workingImage = None  # Stores the image shown in the top left
    dataSend = serial.Serial('com8', 115200)
    curX, curY = 0, 0

    def __init__(self, dialog):  # Initialization function
        # Set up the GUI
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        # Create then display the image
        self.clear_image()
        self.disp_image(self.workingImage)

        self.bGo.clicked.connect(self.run_calculations)
        self.bE.clicked.connect(self.serialTransmit)

    def serialTransmit(self, input):
        t = 0
        # snt = "t 100 123"
        self.txtCommands.appendPlainText(f"Sent: {input}")
        # self.dataSend.flushInput()
        self.dataSend.write(input.encode())


        read = self.dataSend.read(10)
        # while l_sent <= len(snt):
        while t < 3000000:
            t = t + 1
            if t % 100 == 0:
                print(t)
        self.txtCommands.appendPlainText(f"Received: {read}")

    def run_calculations(self):
        error = False
        for cnt, i in enumerate(self.txtInput.toPlainText().split("\n")):  # Split the input text into discreet lines
            print(f"Processing: {i}")

            # Error check and distribute functions
            if i[0] == 'z':
                self.serialTransmit('z')
            elif i[0] == 'u':
                if i[2] == '0':
                    self.serialTransmit("u 0")
                elif i[2] == '1':
                    self.serialTransmit("u 1")
                else:
                    error = True

            elif i[0] == 't':
                tmp = i.split(" ")
                # self.calculate_angle(self.curX + i.split(" ")[1], self.curY + i.split(" ")[2])
                self.serialTransmit(f"t {tmp[1]} {tmp[2]}")

            elif i[0] == 'a':
                print("A not implemented")

            else:
                error = True

            if error:
                print(f"Error on line {cnt}")
                return

    def calculate_angle(self, x, y):
        cv2.line(self.workingImage, (0, 0), (75, 75), (255, 0, 0), 2)
        self.disp_image(self.workingImage)

    def clear_image(self):
        self.workingImage = np.zeros((150, 250, 3), np.uint8)  # Create the empty image (y, x)
        self.workingImage[:, 0:] = (255, 255, 255)  # Make the image white

    def disp_image(self, image):
        pix = QtGui.QPixmap(QtGui.QImage(image, image.shape[1], image.shape[0],
                                         image.shape[1] * 3, QtGui.QImage.Format_RGB888))
        self.outImg.setPixmap(pix)

    def load_file(self):
        print("thingy 5")

# Ignore this bit, setup code for the code
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog(flags=(QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowMinimizeButtonHint |
                                      QtCore.Qt.WindowCloseButtonHint))

    prog = MainPlotGui(dialog)

    dialog.show()
    sys.exit(app.exec_())