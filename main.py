# pip install -r dependencies.txt
import os
os.system("pyuic5 GUI.ui > GUI.py")

import sys  # Forgot where I actually used this, but it's here
from GUI import Ui_Dialog
from PyQt5 import QtWidgets, QtCore, QtGui
import numpy as np
import cv2
import serial
from serial.tools import list_ports
import math


class MainPlotGui(Ui_Dialog):
    # The class variables which are used to pass things around
    workingImage = None  # Stores the image shown in the top left
    dataSend = None
    targetPID = "1A86:7523"


    def __init__(self, dialog):  # Initialization function
        # Set up the GUI
        Ui_Dialog.__init__(self)
        self.setupUi(dialog)

        # Create then display the image
        self.clear_image()
        self.disp_image(self.workingImage)

        self.bStart.clicked.connect(self.connect_serial)

        self.bGo.clicked.connect(self.run_calculations)
        self.bE.clicked.connect(self.serial_transmit)

    def connect_serial(self):
        print("Connecting to serial")
        ports = list_ports.comports(True)
        target = None
        for i in ports:
            if self.targetPID in i[2]:
                print(f"Device found")
                target = i

        print(target[2])
        if self.dataSend is not None:
            self.dataSend.close()
        self.dataSend = serial.Serial(target[0], 115200, timeout=1)
        print(self.dataSend)
        self.dataSend.write(b'h\n')
        print("Data written!")

        response = b''
        while response == b'':
            response = self.dataSend.read_all()
        print(response)
        self.dataSend.write(b'h')

    def serial_transmit(self, input):
        t = 0
        # snt = "t 100 123"
        self.txtCommands.appendPlainText(f"Sent: {input}")
        app.processEvents()
        # self.dataSend.flushInput()
        self.dataSend.write(f"{input}\n".encode())
        response = b''
        while response == b'':
            response = self.dataSend.read_all()

        self.txtCommands.appendPlainText(f"Received: {response}")
        app.processEvents()

    def run_calculations(self):
        error = False
        for cnt, i in enumerate(self.txtInput.toPlainText().split("\n")):  # Split the input text into discreet lines
            print(f"Processing: {i}")

            # Error check and distribute functions
            if i[0] == 'z':
                self.serial_transmit('z')
            elif i[0] == 'u':
                if i.split(" ")[1] == '0':
                    self.serial_transmit("u 0")
                elif i.split(" ")[1] == '1':
                    self.serial_transmit("u 1")
                else:
                    error = True

            elif i[0] == 't':
                tmp = i.split(" ")
                try:
                    theta1, theta2 = self.calculate_angle(int(i.split(" ")[1]), int(i.split(" ")[2]))
                    print(f"Calculated angles: {theta1} {theta2}")
                    self.serial_transmit(f"t {int(theta1)} {int(theta2)}")
                except:
                    print(f"Line failed: {cnt}")
            else:
                error = True

            if error:
                print(f"Error on line {cnt}")
                print(i)
                return

    def calculate_angle(self, x, y):
        L1 = 220
        L2 = 190
        theta1 = math.atan2(y, x)
        L = math.sqrt(x ** 2 + y ** 2)
        theta1 += math.acos((L ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * L2))

        theta2 = math.acos((L2 ** 2 + L1 ** 2 - L ** 2) / (2 * L1 * L2))

        return math.degrees(theta1), math.degrees(theta2)

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