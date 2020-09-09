# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5_design_custom_data_resizable.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_custom_data_window(object):
    def setupUi(self, custom_data_window):
        custom_data_window.setObjectName("custom_data_window")
        custom_data_window.resize(1005, 603)
        self.centralwidget = QtWidgets.QWidget(custom_data_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(985, 100))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.observation_combo_box = QtWidgets.QComboBox(self.frame)
        self.observation_combo_box.setEnabled(False)
        self.observation_combo_box.setGeometry(QtCore.QRect(110, 50, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.observation_combo_box.setFont(font)
        self.observation_combo_box.setObjectName("observation_combo_box")
        self.observation_combo_box.addItem("")
        self.select_period_type_label_2 = QtWidgets.QLabel(self.frame)
        self.select_period_type_label_2.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label_2.setFont(font)
        self.select_period_type_label_2.setObjectName("select_period_type_label_2")
        self.season_type_combo_box = QtWidgets.QComboBox(self.frame)
        self.season_type_combo_box.setEnabled(True)
        self.season_type_combo_box.setGeometry(QtCore.QRect(110, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.season_type_combo_box.setFont(font)
        self.season_type_combo_box.setAcceptDrops(False)
        self.season_type_combo_box.setObjectName("season_type_combo_box")
        self.season_type_combo_box.addItem("")
        self.season_type_combo_box.addItem("")
        self.season_type_combo_box.addItem("")
        self.season_type_combo_box.addItem("")
        self.season_type_combo_box.addItem("")
        self.select_period_type_label = QtWidgets.QLabel(self.frame)
        self.select_period_type_label.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label.setFont(font)
        self.select_period_type_label.setObjectName("select_period_type_label")
        self.data_size_spin_box = QtWidgets.QSpinBox(self.frame)
        self.data_size_spin_box.setGeometry(QtCore.QRect(500, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_size_spin_box.setFont(font)
        self.data_size_spin_box.setMinimum(28)
        self.data_size_spin_box.setMaximum(31)
        self.data_size_spin_box.setObjectName("data_size_spin_box")
        self.select_period_type_label_3 = QtWidgets.QLabel(self.frame)
        self.select_period_type_label_3.setGeometry(QtCore.QRect(380, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label_3.setFont(font)
        self.select_period_type_label_3.setObjectName("select_period_type_label_3")
        self.default_value_double_spin_box = QtWidgets.QDoubleSpinBox(self.frame)
        self.default_value_double_spin_box.setGeometry(QtCore.QRect(500, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.default_value_double_spin_box.setFont(font)
        self.default_value_double_spin_box.setMinimum(-90.0)
        self.default_value_double_spin_box.setMaximum(60.0)
        self.default_value_double_spin_box.setObjectName("default_value_double_spin_box")
        self.select_period_type_label_4 = QtWidgets.QLabel(self.frame)
        self.select_period_type_label_4.setGeometry(QtCore.QRect(380, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label_4.setFont(font)
        self.select_period_type_label_4.setObjectName("select_period_type_label_4")
        self.reset_push_button = QtWidgets.QPushButton(self.frame)
        self.reset_push_button.setGeometry(QtCore.QRect(580, 20, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_push_button.setFont(font)
        self.reset_push_button.setObjectName("reset_push_button")
        self.select_period_type_label_5 = QtWidgets.QLabel(self.frame)
        self.select_period_type_label_5.setGeometry(QtCore.QRect(680, 10, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label_5.setFont(font)
        self.select_period_type_label_5.setObjectName("select_period_type_label_5")
        self.max_temperature_double_spin_box = QtWidgets.QDoubleSpinBox(self.frame)
        self.max_temperature_double_spin_box.setGeometry(QtCore.QRect(770, 10, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.max_temperature_double_spin_box.setFont(font)
        self.max_temperature_double_spin_box.setMinimum(-90.0)
        self.max_temperature_double_spin_box.setMaximum(60.0)
        self.max_temperature_double_spin_box.setProperty("value", 10.0)
        self.max_temperature_double_spin_box.setObjectName("max_temperature_double_spin_box")
        self.select_period_type_label_6 = QtWidgets.QLabel(self.frame)
        self.select_period_type_label_6.setGeometry(QtCore.QRect(680, 50, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label_6.setFont(font)
        self.select_period_type_label_6.setObjectName("select_period_type_label_6")
        self.min_temperature_double_spin_box = QtWidgets.QDoubleSpinBox(self.frame)
        self.min_temperature_double_spin_box.setGeometry(QtCore.QRect(770, 50, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.min_temperature_double_spin_box.setFont(font)
        self.min_temperature_double_spin_box.setMinimum(-90.0)
        self.min_temperature_double_spin_box.setMaximum(60.0)
        self.min_temperature_double_spin_box.setProperty("value", -10.0)
        self.min_temperature_double_spin_box.setObjectName("min_temperature_double_spin_box")
        self.update_limits_push_button = QtWidgets.QPushButton(self.frame)
        self.update_limits_push_button.setGeometry(QtCore.QRect(850, 20, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.update_limits_push_button.setFont(font)
        self.update_limits_push_button.setObjectName("update_limits_push_button")
        self.verticalLayout.addWidget(self.frame)
        self.sliders_horizontal_layout = QtWidgets.QHBoxLayout()
        self.sliders_horizontal_layout.setObjectName("sliders_horizontal_layout")
        self.verticalLayout.addLayout(self.sliders_horizontal_layout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.diagram_vertical_layout = QtWidgets.QVBoxLayout()
        self.diagram_vertical_layout.setObjectName("diagram_vertical_layout")
        self.horizontalLayout.addLayout(self.diagram_vertical_layout)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(0, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        custom_data_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(custom_data_window)
        self.statusbar.setObjectName("statusbar")
        custom_data_window.setStatusBar(self.statusbar)

        self.retranslateUi(custom_data_window)
        QtCore.QMetaObject.connectSlotsByName(custom_data_window)

    def retranslateUi(self, custom_data_window):
        _translate = QtCore.QCoreApplication.translate
        custom_data_window.setWindowTitle(_translate("custom_data_window", "Custom data"))
        self.observation_combo_box.setItemText(0, _translate("custom_data_window", "(None)"))
        self.select_period_type_label_2.setText(_translate("custom_data_window", "Observation"))
        self.season_type_combo_box.setItemText(0, _translate("custom_data_window", "(None)"))
        self.season_type_combo_box.setItemText(1, _translate("custom_data_window", "Winter"))
        self.season_type_combo_box.setItemText(2, _translate("custom_data_window", "Spring"))
        self.season_type_combo_box.setItemText(3, _translate("custom_data_window", "Summer"))
        self.season_type_combo_box.setItemText(4, _translate("custom_data_window", "Fall"))
        self.select_period_type_label.setText(_translate("custom_data_window", "Season"))
        self.select_period_type_label_3.setText(_translate("custom_data_window", "Data size"))
        self.select_period_type_label_4.setText(_translate("custom_data_window", "Default value"))
        self.reset_push_button.setText(_translate("custom_data_window", "Reset"))
        self.select_period_type_label_5.setText(_translate("custom_data_window", "Max temp"))
        self.select_period_type_label_6.setText(_translate("custom_data_window", "Min temp"))
        self.update_limits_push_button.setText(_translate("custom_data_window", "Update limits"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    custom_data_window = QtWidgets.QMainWindow()
    ui = Ui_custom_data_window()
    ui.setupUi(custom_data_window)
    custom_data_window.show()
    sys.exit(app.exec_())