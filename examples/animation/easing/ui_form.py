# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Wed Feb 16 22:14:47 2011
#      by: pyside-uic 0.2.6 running on PySide 1.0.0~beta5
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(545, 471)
        self.gridLayout = QtGui.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.easingCurvePicker = QtGui.QListWidget(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.easingCurvePicker.sizePolicy().hasHeightForWidth())
        self.easingCurvePicker.setSizePolicy(sizePolicy)
        self.easingCurvePicker.setMaximumSize(QtCore.QSize(16777215, 120))
        self.easingCurvePicker.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.easingCurvePicker.setMovement(QtGui.QListView.Static)
        self.easingCurvePicker.setProperty("isWrapping", False)
        self.easingCurvePicker.setViewMode(QtGui.QListView.IconMode)
        self.easingCurvePicker.setSelectionRectVisible(False)
        self.easingCurvePicker.setObjectName("easingCurvePicker")
        self.gridLayout.addWidget(self.easingCurvePicker, 0, 0, 1, 2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineRadio = QtGui.QRadioButton(self.groupBox_2)
        self.lineRadio.setChecked(True)
        self.lineRadio.setObjectName("lineRadio")
        self.buttonGroup = QtGui.QButtonGroup(Form)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.lineRadio)
        self.verticalLayout_2.addWidget(self.lineRadio)
        self.circleRadio = QtGui.QRadioButton(self.groupBox_2)
        self.circleRadio.setObjectName("circleRadio")
        self.buttonGroup.addButton(self.circleRadio)
        self.verticalLayout_2.addWidget(self.circleRadio)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtGui.QGroupBox(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.periodSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.periodSpinBox.setEnabled(False)
        self.periodSpinBox.setMinimum(-1.0)
        self.periodSpinBox.setSingleStep(0.1)
        self.periodSpinBox.setProperty("value", -1.0)
        self.periodSpinBox.setObjectName("periodSpinBox")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.periodSpinBox)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.amplitudeSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.amplitudeSpinBox.setEnabled(False)
        self.amplitudeSpinBox.setMinimum(-1.0)
        self.amplitudeSpinBox.setSingleStep(0.1)
        self.amplitudeSpinBox.setProperty("value", -1.0)
        self.amplitudeSpinBox.setObjectName("amplitudeSpinBox")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.amplitudeSpinBox)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.overshootSpinBox = QtGui.QDoubleSpinBox(self.groupBox)
        self.overshootSpinBox.setEnabled(False)
        self.overshootSpinBox.setMinimum(-1.0)
        self.overshootSpinBox.setSingleStep(0.1)
        self.overshootSpinBox.setProperty("value", -1.0)
        self.overshootSpinBox.setObjectName("overshootSpinBox")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.overshootSpinBox)
        self.verticalLayout.addWidget(self.groupBox)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(Form)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Easing curves", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Path type", None, QtGui.QApplication.UnicodeUTF8))
        self.lineRadio.setText(QtGui.QApplication.translate("Form", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.circleRadio.setText(QtGui.QApplication.translate("Form", "Circle", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Period", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Amplitude", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Overshoot", None, QtGui.QApplication.UnicodeUTF8))

