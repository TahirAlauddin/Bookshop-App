# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bookForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 476)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("* {\n"
"color: white;\n"
"background: rgb(23, 26, 30);\n"
"}\n"
"QLineEdit {\n"
"padding: 5px;\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.contentBottom = QtWidgets.QFrame(self.centralwidget)
        self.contentBottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contentBottom.setObjectName("contentBottom")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.content = QtWidgets.QFrame(self.contentBottom)
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content.setObjectName("content")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.content)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.content)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.status_label = QtWidgets.QLabel(self.frame_3)
        self.status_label.setStyleSheet("color: rgb(189, 147, 249);")
        self.status_label.setText("")
        self.status_label.setAlignment(QtCore.Qt.AlignCenter)
        self.status_label.setWordWrap(True)
        self.status_label.setObjectName("status_label")
        self.horizontalLayout_4.addWidget(self.status_label)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(self.content)
        self.frame_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout.setHorizontalSpacing(30)
        self.gridLayout.setVerticalSpacing(25)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 4, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 9, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.input_price = QtWidgets.QLineEdit(self.frame_2)
        self.input_price.setObjectName("input_price")
        self.gridLayout.addWidget(self.input_price, 8, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 8, 0, 1, 1)
        self.input_quantity = QtWidgets.QLineEdit(self.frame_2)
        self.input_quantity.setObjectName("input_quantity")
        self.gridLayout.addWidget(self.input_quantity, 6, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 3, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 6, 1, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 8, 3, 1, 1)
        self.input_name = QtWidgets.QLineEdit(self.frame_2)
        self.input_name.setObjectName("input_name")
        self.gridLayout.addWidget(self.input_name, 4, 2, 1, 1)
        self.chooseFile_button = QtWidgets.QPushButton(self.frame_2)
        self.chooseFile_button.setMinimumSize(QtCore.QSize(0, 0))
        self.chooseFile_button.setAutoFillBackground(False)
        self.chooseFile_button.setStyleSheet("\n"
"QPushButton { \n"
"font-size: 14px;\n"
" background-color: rgb(23, 26, 30); \n"
"border: 1px solid white;\n"
"  border-radius: 5px; \n"
"padding: 10px}\n"
"QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/images/icons/cil-options-horizontal.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chooseFile_button.setIcon(icon)
        self.chooseFile_button.setObjectName("chooseFile_button")
        self.gridLayout.addWidget(self.chooseFile_button, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 1, 1, 1)
        self.input_author = QtWidgets.QLineEdit(self.frame_2)
        self.input_author.setObjectName("input_author")
        self.gridLayout.addWidget(self.input_author, 5, 2, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 5, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 5, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.content)
        self.frame.setStyleSheet("\n"
"/* Top Buttons */\n"
"QPushButton {  background-color: rgb(23, 26, 30); border: none;  border-radius: 5px; padding: 10px}\n"
"QPushButton:hover { background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.add_buttton = QtWidgets.QPushButton(self.frame)
        self.add_buttton.setMinimumSize(QtCore.QSize(100, 0))
        self.add_buttton.setStyleSheet("border: 1px solid white; border-radius: 10px;")
        self.add_buttton.setObjectName("add_buttton")
        self.verticalLayout_3.addWidget(self.add_buttton)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 3)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_6.addWidget(self.content)
        self.verticalLayout_2.addWidget(self.contentBottom)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Image"))
        self.label_5.setText(_translate("MainWindow", "Price"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Quanity"))
        self.chooseFile_button.setText(_translate("MainWindow", "Choose File"))
        self.label.setText(_translate("MainWindow", "Author"))
        self.add_buttton.setText(_translate("MainWindow", "ADD"))
from . import resources_rc
