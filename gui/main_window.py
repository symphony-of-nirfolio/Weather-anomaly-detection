# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5_design_resizable.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1514, 790)
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.main_horizontal_layout = QtWidgets.QHBoxLayout()
        self.main_horizontal_layout.setObjectName("main_horizontal_layout")
        self.controller_frame = QtWidgets.QFrame(self.centralwidget)
        self.controller_frame.setMinimumSize(QtCore.QSize(350, 750))
        self.controller_frame.setMaximumSize(QtCore.QSize(350, 16777215))
        self.controller_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.controller_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controller_frame.setObjectName("controller_frame")
        self.station_id_label = QtWidgets.QLabel(self.controller_frame)
        self.station_id_label.setGeometry(QtCore.QRect(10, 170, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.station_id_label.setFont(font)
        self.station_id_label.setObjectName("station_id_label")
        self.station_id_line_edit = QtWidgets.QLineEdit(self.controller_frame)
        self.station_id_line_edit.setGeometry(QtCore.QRect(10, 210, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.station_id_line_edit.setFont(font)
        self.station_id_line_edit.setObjectName("station_id_line_edit")
        self.select_training_observations_group_box = QtWidgets.QGroupBox(self.controller_frame)
        self.select_training_observations_group_box.setGeometry(QtCore.QRect(10, 480, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_training_observations_group_box.setFont(font)
        self.select_training_observations_group_box.setObjectName("select_training_observations_group_box")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.select_training_observations_group_box)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(9, 20, 311, 91))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.select_training_observation_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.select_training_observation_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.select_training_observation_vertical_layout.setObjectName("select_training_observation_vertical_layout")
        self.extract_data_push_button = QtWidgets.QPushButton(self.controller_frame)
        self.extract_data_push_button.setGeometry(QtCore.QRect(10, 250, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.extract_data_push_button.setFont(font)
        self.extract_data_push_button.setObjectName("extract_data_push_button")
        self.data_extraction_status_text_label = QtWidgets.QLabel(self.controller_frame)
        self.data_extraction_status_text_label.setGeometry(QtCore.QRect(10, 300, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_extraction_status_text_label.setFont(font)
        self.data_extraction_status_text_label.setObjectName("data_extraction_status_text_label")
        self.data_extraction_status_value_label = QtWidgets.QLabel(self.controller_frame)
        self.data_extraction_status_value_label.setGeometry(QtCore.QRect(10, 330, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.data_extraction_status_value_label.setFont(font)
        self.data_extraction_status_value_label.setText("")
        self.data_extraction_status_value_label.setObjectName("data_extraction_status_value_label")
        self.site_text_label = QtWidgets.QLabel(self.controller_frame)
        self.site_text_label.setGeometry(QtCore.QRect(10, 40, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.site_text_label.setFont(font)
        self.site_text_label.setObjectName("site_text_label")
        self.site_hyperlink_label = QtWidgets.QLabel(self.controller_frame)
        self.site_hyperlink_label.setGeometry(QtCore.QRect(50, 40, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.site_hyperlink_label.setFont(font)
        self.site_hyperlink_label.setTextFormat(QtCore.Qt.RichText)
        self.site_hyperlink_label.setOpenExternalLinks(True)
        self.site_hyperlink_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.site_hyperlink_label.setObjectName("site_hyperlink_label")
        self.training_status_value_label = QtWidgets.QLabel(self.controller_frame)
        self.training_status_value_label.setGeometry(QtCore.QRect(10, 690, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.training_status_value_label.setFont(font)
        self.training_status_value_label.setText("")
        self.training_status_value_label.setObjectName("training_status_value_label")
        self.training_status_text_label = QtWidgets.QLabel(self.controller_frame)
        self.training_status_text_label.setGeometry(QtCore.QRect(10, 660, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.training_status_text_label.setFont(font)
        self.training_status_text_label.setObjectName("training_status_text_label")
        self.train_push_button = QtWidgets.QPushButton(self.controller_frame)
        self.train_push_button.setEnabled(False)
        self.train_push_button.setGeometry(QtCore.QRect(10, 610, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.train_push_button.setFont(font)
        self.train_push_button.setObjectName("train_push_button")
        self.line_2 = QtWidgets.QFrame(self.controller_frame)
        self.line_2.setGeometry(QtCore.QRect(0, 370, 351, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.usa_tutorial_push_button = QtWidgets.QPushButton(self.controller_frame)
        self.usa_tutorial_push_button.setGeometry(QtCore.QRect(10, 70, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.usa_tutorial_push_button.setFont(font)
        self.usa_tutorial_push_button.setObjectName("usa_tutorial_push_button")
        self.all_other_tutorial_push_button = QtWidgets.QPushButton(self.controller_frame)
        self.all_other_tutorial_push_button.setGeometry(QtCore.QRect(10, 120, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.all_other_tutorial_push_button.setFont(font)
        self.all_other_tutorial_push_button.setObjectName("all_other_tutorial_push_button")
        self.select_station_id_for_training_combo_box = QtWidgets.QComboBox(self.controller_frame)
        self.select_station_id_for_training_combo_box.setGeometry(QtCore.QRect(100, 430, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_station_id_for_training_combo_box.setFont(font)
        self.select_station_id_for_training_combo_box.setObjectName("select_station_id_for_training_combo_box")
        self.select_station_id_for_training_combo_box.addItem("")
        self.station_id_label_2 = QtWidgets.QLabel(self.controller_frame)
        self.station_id_label_2.setGeometry(QtCore.QRect(10, 430, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.station_id_label_2.setFont(font)
        self.station_id_label_2.setObjectName("station_id_label_2")
        self.data_extraction_label = QtWidgets.QLabel(self.controller_frame)
        self.data_extraction_label.setGeometry(QtCore.QRect(10, 0, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.data_extraction_label.setFont(font)
        self.data_extraction_label.setAlignment(QtCore.Qt.AlignCenter)
        self.data_extraction_label.setObjectName("data_extraction_label")
        self.train_label = QtWidgets.QLabel(self.controller_frame)
        self.train_label.setGeometry(QtCore.QRect(10, 390, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.train_label.setFont(font)
        self.train_label.setAlignment(QtCore.Qt.AlignCenter)
        self.train_label.setObjectName("train_label")
        self.main_horizontal_layout.addWidget(self.controller_frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.main_horizontal_layout.addWidget(self.line)
        self.diagram_and_parameters_vertical_layout = QtWidgets.QVBoxLayout()
        self.diagram_and_parameters_vertical_layout.setObjectName("diagram_and_parameters_vertical_layout")
        self.diagram_parameters_frame = QtWidgets.QFrame(self.centralwidget)
        self.diagram_parameters_frame.setEnabled(True)
        self.diagram_parameters_frame.setMinimumSize(QtCore.QSize(720, 170))
        self.diagram_parameters_frame.setMaximumSize(QtCore.QSize(16777215, 170))
        self.diagram_parameters_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diagram_parameters_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diagram_parameters_frame.setObjectName("diagram_parameters_frame")
        self.select_period_type_label = QtWidgets.QLabel(self.diagram_parameters_frame)
        self.select_period_type_label.setGeometry(QtCore.QRect(10, 80, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label.setFont(font)
        self.select_period_type_label.setObjectName("select_period_type_label")
        self.select_diagram_observations_group_box = QtWidgets.QGroupBox(self.diagram_parameters_frame)
        self.select_diagram_observations_group_box.setGeometry(QtCore.QRect(510, 30, 321, 121))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_diagram_observations_group_box.setFont(font)
        self.select_diagram_observations_group_box.setObjectName("select_diagram_observations_group_box")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.select_diagram_observations_group_box)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(9, 20, 301, 91))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.select_diagram_observation_vertical_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.select_diagram_observation_vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.select_diagram_observation_vertical_layout.setObjectName("select_diagram_observation_vertical_layout")
        self.select_period_type_combo_box = QtWidgets.QComboBox(self.diagram_parameters_frame)
        self.select_period_type_combo_box.setGeometry(QtCore.QRect(240, 80, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_combo_box.setFont(font)
        self.select_period_type_combo_box.setObjectName("select_period_type_combo_box")
        self.select_period_type_combo_box.addItem("")
        self.select_period_type_combo_box.addItem("")
        self.select_period_type_combo_box.addItem("")
        self.select_period_type_combo_box.addItem("")
        self.select_period_type_combo_box.addItem("")
        self.diagrams_label = QtWidgets.QLabel(self.diagram_parameters_frame)
        self.diagrams_label.setGeometry(QtCore.QRect(180, 0, 321, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.diagrams_label.setFont(font)
        self.diagrams_label.setAlignment(QtCore.Qt.AlignCenter)
        self.diagrams_label.setObjectName("diagrams_label")
        self.station_id_label_3 = QtWidgets.QLabel(self.diagram_parameters_frame)
        self.station_id_label_3.setGeometry(QtCore.QRect(10, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.station_id_label_3.setFont(font)
        self.station_id_label_3.setObjectName("station_id_label_3")
        self.select_station_id_for_diagram_combo_box = QtWidgets.QComboBox(self.diagram_parameters_frame)
        self.select_station_id_for_diagram_combo_box.setGeometry(QtCore.QRect(240, 40, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_station_id_for_diagram_combo_box.setFont(font)
        self.select_station_id_for_diagram_combo_box.setObjectName("select_station_id_for_diagram_combo_box")
        self.select_station_id_for_diagram_combo_box.addItem("")
        self.select_observation_for_anomaly_combo_box = QtWidgets.QComboBox(self.diagram_parameters_frame)
        self.select_observation_for_anomaly_combo_box.setEnabled(False)
        self.select_observation_for_anomaly_combo_box.setGeometry(QtCore.QRect(240, 120, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_observation_for_anomaly_combo_box.setFont(font)
        self.select_observation_for_anomaly_combo_box.setObjectName("select_observation_for_anomaly_combo_box")
        self.select_observation_for_anomaly_combo_box.addItem("")
        self.select_period_type_label_2 = QtWidgets.QLabel(self.diagram_parameters_frame)
        self.select_period_type_label_2.setGeometry(QtCore.QRect(10, 120, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.select_period_type_label_2.setFont(font)
        self.select_period_type_label_2.setObjectName("select_period_type_label_2")
        self.diagram_and_parameters_vertical_layout.addWidget(self.diagram_parameters_frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(100, 20))
        self.label.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.periods_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.periods_list_widget.setMinimumSize(QtCore.QSize(200, 0))
        self.periods_list_widget.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.periods_list_widget.setFont(font)
        self.periods_list_widget.setObjectName("periods_list_widget")
        self.verticalLayout_2.addWidget(self.periods_list_widget)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(700, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 0))
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout.addWidget(self.widget_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.diagram_vertical_layout = QtWidgets.QVBoxLayout()
        self.diagram_vertical_layout.setObjectName("diagram_vertical_layout")
        self.horizontalLayout_4.addLayout(self.diagram_vertical_layout)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMaximumSize(QtCore.QSize(0, 16777215))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.diagram_and_parameters_vertical_layout.addLayout(self.horizontalLayout_3)
        self.main_horizontal_layout.addLayout(self.diagram_and_parameters_vertical_layout)
        self.main_horizontal_layout.setStretch(2, 80)
        self.horizontalLayout_2.addLayout(self.main_horizontal_layout)
        main_window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Weather anomaly detection"))
        self.station_id_label.setText(_translate("main_window", "Station ID"))
        self.station_id_line_edit.setText(_translate("main_window", "UPM00033345"))
        self.select_training_observations_group_box.setTitle(_translate("main_window", "Select observations for training"))
        self.extract_data_push_button.setText(_translate("main_window", "Extract data"))
        self.data_extraction_status_text_label.setText(_translate("main_window", "Data extraction status:"))
        self.site_text_label.setText(_translate("main_window", "Site:"))
        self.site_hyperlink_label.setText(_translate("main_window", "<a href=\"https://gis.ncdc.noaa.gov/maps/ncei/cdo/daily\">gis.ncdc.noaa.gov</a>"))
        self.training_status_text_label.setText(_translate("main_window", "Training status:"))
        self.train_push_button.setText(_translate("main_window", "Train"))
        self.usa_tutorial_push_button.setText(_translate("main_window", "Tutorial for USA country"))
        self.all_other_tutorial_push_button.setText(_translate("main_window", "Tutorial for All other countries"))
        self.select_station_id_for_training_combo_box.setItemText(0, _translate("main_window", "(None)"))
        self.station_id_label_2.setText(_translate("main_window", "Station ID"))
        self.data_extraction_label.setText(_translate("main_window", "Data extraction"))
        self.train_label.setText(_translate("main_window", "Train"))
        self.select_period_type_label.setText(_translate("main_window", "Select period type"))
        self.select_diagram_observations_group_box.setTitle(_translate("main_window", "Select observations for showing diagram"))
        self.select_period_type_combo_box.setItemText(0, _translate("main_window", "(None)"))
        self.select_period_type_combo_box.setItemText(1, _translate("main_window", "Month"))
        self.select_period_type_combo_box.setItemText(2, _translate("main_window", "Season"))
        self.select_period_type_combo_box.setItemText(3, _translate("main_window", "Year"))
        self.select_period_type_combo_box.setItemText(4, _translate("main_window", "All"))
        self.diagrams_label.setText(_translate("main_window", "Diagrams"))
        self.station_id_label_3.setText(_translate("main_window", "Station ID"))
        self.select_station_id_for_diagram_combo_box.setItemText(0, _translate("main_window", "(None)"))
        self.select_observation_for_anomaly_combo_box.setItemText(0, _translate("main_window", "(None)"))
        self.select_period_type_label_2.setText(_translate("main_window", "Select observation for anomaly"))
        self.label.setText(_translate("main_window", "Periods"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
