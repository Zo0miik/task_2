# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class SummaryWindow(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1050, 600)
        #рабочее окно
        self.graphicsView = QtWidgets.QGraphicsView(Form)
        self.graphicsView.setGeometry(QtCore.QRect(400, 50, 600, 480))
        self.graphicsView.setObjectName("graphicsView")
        #таблица
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(50, 50, 300, 480))
        self.tableView.setObjectName("tableView")
        #таблица
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(165, 20, 70, 20))
        self.label.setObjectName("label")
        #график
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(665, 20, 70, 20))
        self.label_2.setObjectName("label_2")
        #поехали
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(150, 550, 100, 30))
        self.pushButton.setObjectName("pushButton")
        #сохранить
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 550, 125, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        #загрузить
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 550, 125, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Задание №2"))
        self.label.setText(_translate("Form", "Таблица"))
        self.label_2.setText(_translate("Form", "График"))
        self.pushButton.setText(_translate("Form", "Поехали"))
        self.pushButton_2.setText(_translate("Form", "Сохранить в hdf"))
        self.pushButton_3.setText(_translate("Form", "Загрузить из hdf"))

