# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(967, 733)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TopLayout = QtWidgets.QHBoxLayout()
        self.TopLayout.setObjectName("TopLayout")
        self.WinOut = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WinOut.sizePolicy().hasHeightForWidth())
        self.WinOut.setSizePolicy(sizePolicy)
        self.WinOut.setObjectName("WinOut")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.WinOut)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.outImg = QtWidgets.QLabel(self.WinOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outImg.sizePolicy().hasHeightForWidth())
        self.outImg.setSizePolicy(sizePolicy)
        self.outImg.setScaledContents(True)
        self.outImg.setAlignment(QtCore.Qt.AlignCenter)
        self.outImg.setObjectName("outImg")
        self.verticalLayout_10.addWidget(self.outImg)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.WinOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.spinBox = QtWidgets.QSpinBox(self.WinOut)
        self.spinBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setFrame(True)
        self.spinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox.setKeyboardTracking(False)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_2.addWidget(self.spinBox)
        self.label_11 = QtWidgets.QLabel(self.WinOut)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.spinBox_2 = QtWidgets.QSpinBox(self.WinOut)
        self.spinBox_2.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout_10.addLayout(self.horizontalLayout_2)
        self.TopLayout.addWidget(self.WinOut)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.TopLayout.addWidget(self.line_2)
        self.WinControl = QtWidgets.QGroupBox(Dialog)
        self.WinControl.setObjectName("WinControl")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.WinControl)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.txtInput = QtWidgets.QTextEdit(self.WinControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtInput.sizePolicy().hasHeightForWidth())
        self.txtInput.setSizePolicy(sizePolicy)
        self.txtInput.setObjectName("txtInput")
        self.verticalLayout_9.addWidget(self.txtInput)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bLoad = QtWidgets.QPushButton(self.WinControl)
        self.bLoad.setObjectName("bLoad")
        self.horizontalLayout.addWidget(self.bLoad)
        self.bSave = QtWidgets.QPushButton(self.WinControl)
        self.bSave.setAutoDefault(True)
        self.bSave.setObjectName("bSave")
        self.horizontalLayout.addWidget(self.bSave)
        self.bGo = QtWidgets.QPushButton(self.WinControl)
        self.bGo.setObjectName("bGo")
        self.horizontalLayout.addWidget(self.bGo)
        self.verticalLayout_9.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.WinControl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.WinControl)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.TopLayout.addWidget(self.WinControl)
        self.verticalLayout.addLayout(self.TopLayout)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.BotLayout = QtWidgets.QHBoxLayout()
        self.BotLayout.setObjectName("BotLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_7 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.bD = QtWidgets.QPushButton(Dialog)
        self.bD.setObjectName("bD")
        self.verticalLayout_8.addWidget(self.bD)
        self.gridLayout_2.addLayout(self.verticalLayout_8, 1, 2, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.bW = QtWidgets.QPushButton(Dialog)
        self.bW.setObjectName("bW")
        self.verticalLayout_3.addWidget(self.bW)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.bE = QtWidgets.QPushButton(Dialog)
        self.bE.setObjectName("bE")
        self.verticalLayout_5.addWidget(self.bE)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 0, 2, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.bS = QtWidgets.QPushButton(Dialog)
        self.bS.setObjectName("bS")
        self.verticalLayout_7.addWidget(self.bS)
        self.gridLayout_2.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.bA = QtWidgets.QPushButton(Dialog)
        self.bA.setObjectName("bA")
        self.verticalLayout_6.addWidget(self.bA)
        self.gridLayout_2.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.bQ = QtWidgets.QPushButton(Dialog)
        self.bQ.setObjectName("bQ")
        self.verticalLayout_2.addWidget(self.bQ)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.BotLayout.addLayout(self.gridLayout_2)
        self.txtCommands = QtWidgets.QPlainTextEdit(Dialog)
        self.txtCommands.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtCommands.sizePolicy().hasHeightForWidth())
        self.txtCommands.setSizePolicy(sizePolicy)
        self.txtCommands.setObjectName("txtCommands")
        self.BotLayout.addWidget(self.txtCommands)
        self.verticalLayout.addLayout(self.BotLayout)

        self.retranslateUi(Dialog)
        self.txtInput.textChanged.connect(self.label_8.clear)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.WinOut.setTitle(_translate("Dialog", "Output Window"))
        self.outImg.setText(_translate("Dialog", "No image shown yet"))
        self.label_10.setText(_translate("Dialog", "X:"))
        self.label_11.setText(_translate("Dialog", "  Y:"))
        self.WinControl.setTitle(_translate("Dialog", "Command Input"))
        self.bLoad.setText(_translate("Dialog", "Load"))
        self.bSave.setText(_translate("Dialog", "Save"))
        self.bGo.setText(_translate("Dialog", "Go!"))
        self.label_9.setText(_translate("Dialog", "Error check:"))
        self.label_8.setText(_translate("Dialog", "Good!"))
        self.label_7.setText(_translate("Dialog", "+ X"))
        self.bD.setText(_translate("Dialog", "D"))
        self.label_3.setText(_translate("Dialog", "- Y"))
        self.bW.setText(_translate("Dialog", "W"))
        self.label_4.setText(_translate("Dialog", "Manipulator Down"))
        self.bE.setText(_translate("Dialog", "E"))
        self.label_6.setText(_translate("Dialog", "+ Y"))
        self.bS.setText(_translate("Dialog", "S"))
        self.label_5.setText(_translate("Dialog", "- X"))
        self.bA.setText(_translate("Dialog", "A"))
        self.label_2.setText(_translate("Dialog", "Manipulator Up"))
        self.bQ.setText(_translate("Dialog", "Q"))
        self.txtCommands.setPlainText(_translate("Dialog", "serial log:\n"
""))


