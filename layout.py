# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NCCU_Rent(object):
    def setupUi(self, NCCU_Rent):
        NCCU_Rent.setObjectName("NCCU_Rent")
        NCCU_Rent.resize(1200, 800)
        NCCU_Rent.setAutoFillBackground(True)
        NCCU_Rent.setStyleSheet("")
        self.toolButton_1 = QtWidgets.QToolButton(NCCU_Rent)
        self.toolButton_1.setGeometry(QtCore.QRect(50, 70, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton_1.setFont(font)
        self.toolButton_1.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_1.setIcon(icon)
        self.toolButton_1.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_1.setObjectName("toolButton_1")
        self.toolButton_2 = QtWidgets.QToolButton(NCCU_Rent)
        self.toolButton_2.setGeometry(QtCore.QRect(50, 230, 221, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.toolButton_2.setFont(font)
        self.toolButton_2.setStyleSheet("")
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(100, 100))
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")

        self.retranslateUi(NCCU_Rent)
        QtCore.QMetaObject.connectSlotsByName(NCCU_Rent)

    def retranslateUi(self, NCCU_Rent):
        _translate = QtCore.QCoreApplication.translate
        NCCU_Rent.setWindowTitle(_translate("NCCU_Rent", "NCCU_Rent"))
        self.toolButton_1.setText(_translate("NCCU_Rent", "我要租屋"))
        self.toolButton_2.setText(_translate("NCCU_Rent", "我要出租"))
import pic_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NCCU_Rent = QtWidgets.QWidget()
    ui = Ui_NCCU_Rent()
    ui.setupUi(NCCU_Rent)
    NCCU_Rent.show()
    sys.exit(app.exec_())