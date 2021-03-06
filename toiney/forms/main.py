# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("toiney.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.consoleBox = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.consoleBox.setGeometry(QtCore.QRect(30, 330, 531, 201))
        self.consoleBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.consoleBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.consoleBox.setReadOnly(True)
        self.consoleBox.setObjectName("consoleBox")
        self.mainTable = QtWidgets.QTableWidget(self.centralwidget)
        self.mainTable.setGeometry(QtCore.QRect(30, 20, 531, 301))
        self.mainTable.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mainTable.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainTable.setTextElideMode(QtCore.Qt.ElideLeft)
        self.mainTable.setGridStyle(QtCore.Qt.SolidLine)
        self.mainTable.setObjectName("mainTable")
        self.mainTable.setColumnCount(3)
        self.mainTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.mainTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(2, item)
        self.mainTable.horizontalHeader().setVisible(True)
        self.mainTable.horizontalHeader().setCascadingSectionResizes(False)
        self.mainTable.horizontalHeader().setSortIndicatorShown(False)
        self.mainTable.horizontalHeader().setStretchLastSection(False)
        self.mainTable.verticalHeader().setCascadingSectionResizes(False)
        self.mainTable.verticalHeader().setSortIndicatorShown(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 798, 21))
        self.menuBar.setDefaultUp(False)
        self.menuBar.setNativeMenuBar(True)
        self.menuBar.setObjectName("menuBar")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        MainWindow.insertToolBarBreak(self.toolBar)
        self.actionConfiguration = QtWidgets.QAction(MainWindow)
        self.actionConfiguration.setObjectName("actionConfiguration")
        self.action_account = QtWidgets.QAction(MainWindow)
        self.action_account.setPriority(QtWidgets.QAction.NormalPriority)
        self.action_account.setObjectName("action_account")
        self.actionDevice_Manager = QtWidgets.QAction(MainWindow)
        self.actionDevice_Manager.setObjectName("actionDevice_Manager")
        self.actionLocation_Manager = QtWidgets.QAction(MainWindow)
        self.actionLocation_Manager.setObjectName("actionLocation_Manager")
        self.actionVariable_Manager = QtWidgets.QAction(MainWindow)
        self.actionVariable_Manager.setObjectName("actionVariable_Manager")
        self.actionEvent_Log = QtWidgets.QAction(MainWindow)
        self.actionEvent_Log.setCheckable(True)
        self.actionEvent_Log.setChecked(True)
        self.actionEvent_Log.setObjectName("actionEvent_Log")
        self.actionStatus_Bar = QtWidgets.QAction(MainWindow)
        self.actionStatus_Bar.setObjectName("actionStatus_Bar")
        self.actionStatistics = QtWidgets.QAction(MainWindow)
        self.actionStatistics.setObjectName("actionStatistics")
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionConfiguration)
        self.menuView.addSeparator()
        self.menuView.addAction(self.action_account)
        self.menuView.addAction(self.actionDevice_Manager)
        self.menuView.addAction(self.actionLocation_Manager)
        self.menuView.addAction(self.actionVariable_Manager)
        self.menuView.addSeparator()
        self.menuView.addAction(self.actionEvent_Log)
        self.menuView.addAction(self.actionStatus_Bar)
        self.menuView.addAction(self.actionStatistics)
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        self.action_account.triggered.connect(MainWindow.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Toiney - v1.0"))
        item = self.mainTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id"))
        item = self.mainTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Account"))
        item = self.mainTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionConfiguration.setText(_translate("MainWindow", "Configuration"))
        self.action_account.setText(_translate("MainWindow", "Account Manager"))
        self.actionDevice_Manager.setText(_translate("MainWindow", "Device Manager"))
        self.actionLocation_Manager.setText(_translate("MainWindow", "Location Manager"))
        self.actionVariable_Manager.setText(_translate("MainWindow", "Variable Manager"))
        self.actionEvent_Log.setText(_translate("MainWindow", "Event Log"))
        self.actionStatus_Bar.setText(_translate("MainWindow", "Status Bar"))
        self.actionStatistics.setText(_translate("MainWindow", "Statistics"))

