# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'restore.ui'
#
# Created: Fri Mar 16 23:31:10 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(552, 214)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.calenderRestore = QtGui.QCalendarWidget(self.centralwidget)
        self.calenderRestore.setGeometry(QtCore.QRect(21, 31, 360, 150))
        self.calenderRestore.setObjectName(_fromUtf8("calenderRestore"))
        self.restoreButton = QtGui.QPushButton(self.centralwidget)
        self.restoreButton.setGeometry(QtCore.QRect(410, 90, 101, 41))
        self.restoreButton.setText(QtGui.QApplication.translate("MainWindow", "restore", None, QtGui.QApplication.UnicodeUTF8))
        self.restoreButton.setObjectName(_fromUtf8("restoreButton"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

