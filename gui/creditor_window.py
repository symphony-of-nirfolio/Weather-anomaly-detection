# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5_design_creditor_resizable.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_creditor_window(object):
    def setupUi(self, creditor_window):
        creditor_window.setObjectName("creditor_window")
        creditor_window.resize(601, 330)
        self.centralwidget = QtWidgets.QWidget(creditor_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(538, 56))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        creditor_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(creditor_window)
        self.statusbar.setObjectName("statusbar")
        creditor_window.setStatusBar(self.statusbar)

        self.retranslateUi(creditor_window)
        QtCore.QMetaObject.connectSlotsByName(creditor_window)

    def retranslateUi(self, creditor_window):
        _translate = QtCore.QCoreApplication.translate
        creditor_window.setWindowTitle(_translate("creditor_window", "Creditor"))
        self.label.setText(_translate("creditor_window", "Sound and music effects obtained from <a href=\"https://www.zapsplat.com\">https://www.zapsplat.com</a>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    creditor_window = QtWidgets.QMainWindow()
    ui = Ui_creditor_window()
    ui.setupUi(creditor_window)
    creditor_window.show()
    sys.exit(app.exec_())