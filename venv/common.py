# -*- coding: utf-8 -*-

import sys
import cmath
import numpy as np
import pandas as pd
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDesktopWidget, QComboBox, QLabel, QLineEdit
from task import SummaryWindow


class WindowApp(QWidget):

    def __init__(self):
        super().__init__()
        self. InitUi()

    def InitUi(self):

        self.ui = SummaryWindow()
        self.ui.setupUi(self)


        self.center()
        self.show()


    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',
            "Вы дейтсвительно хотите выйти?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

