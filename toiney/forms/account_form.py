# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pycharmprojects/hi5/toiney/forms/uic/account_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_account_form(object):
    def setupUi(self, account_form):
        account_form.setObjectName("account_form")
        account_form.setWindowModality(QtCore.Qt.NonModal)
        account_form.resize(711, 393)
        account_form.setFocusPolicy(QtCore.Qt.NoFocus)
        self.gridFrame = QtWidgets.QFrame(account_form)
        self.gridFrame.setGeometry(QtCore.QRect(20, 30, 671, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridFrame.sizePolicy().hasHeightForWidth())
        self.gridFrame.setSizePolicy(sizePolicy)
        self.gridFrame.setAutoFillBackground(True)
        self.gridFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gridFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.gridFrame.setObjectName("gridFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.gridFrame)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 3, 15)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_22 = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_22.sizePolicy().hasHeightForWidth())
        self.pushButton_22.setSizePolicy(sizePolicy)
        self.pushButton_22.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/add_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_22.setIcon(icon)
        self.pushButton_22.setAutoDefault(False)
        self.pushButton_22.setDefault(False)
        self.pushButton_22.setFlat(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_2.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.pushButton_23.sizePolicy().hasHeightForWidth())
        self.pushButton_23.setSizePolicy(sizePolicy)
        self.pushButton_23.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../icons/edit_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_23.setIcon(icon1)
        self.pushButton_23.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_23.setFlat(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_2.addWidget(self.pushButton_23)
        self.line_6 = QtWidgets.QFrame(self.gridFrame)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_2.addWidget(self.line_6)
        self.pushButton = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../icons/import_items.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon2)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.line_7 = QtWidgets.QFrame(self.gridFrame)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.horizontalLayout_2.addWidget(self.line_7)
        self.pushButton_24 = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_24.sizePolicy().hasHeightForWidth())
        self.pushButton_24.setSizePolicy(sizePolicy)
        self.pushButton_24.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../icons/remove_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon3)
        self.pushButton_24.setDefault(False)
        self.pushButton_24.setFlat(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_2.addWidget(self.pushButton_24)
        self.pushButton_25 = QtWidgets.QPushButton(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_25.sizePolicy().hasHeightForWidth())
        self.pushButton_25.setSizePolicy(sizePolicy)
        self.pushButton_25.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../icons/delete_item.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_25.setIcon(icon4)
        self.pushButton_25.setFlat(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_2.addWidget(self.pushButton_25)
        self.label_15 = QtWidgets.QLabel(self.gridFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        self.label_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_15.setScaledContents(False)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.tableWidget = QtWidgets.QTableWidget(account_form)
        self.tableWidget.setGeometry(QtCore.QRect(20, 70, 671, 305))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)

        self.retranslateUi(account_form)
        QtCore.QMetaObject.connectSlotsByName(account_form)

    def retranslateUi(self, account_form):
        _translate = QtCore.QCoreApplication.translate
        account_form.setWindowTitle(_translate("account_form", "Form"))
        self.label_15.setText(_translate("account_form", "Total accounts: 0"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("account_form", "Email"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("account_form", "Password"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("account_form", "Proxy"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("account_form", "State"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("account_form", "Confirmed"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("account_form", "Status"))

