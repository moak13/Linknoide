from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot

class Ui_Task(QObject):
    def setupUi(self, Task):
        Task.setObjectName("Task")
        Task.setEnabled(True)
        Task.resize(780, 574)
        self.centralwidget = QtWidgets.QWidget(Task)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(145, 30, 601, 491))
        self.textBrowser.setObjectName("textBrowser")
        self.subplot_btn = QtWidgets.QPushButton(self.centralwidget)
        self.subplot_btn.setGeometry(QtCore.QRect(20, 72, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.subplot_btn.setFont(font)
        self.subplot_btn.setObjectName("subplot_btn")
        self.quickest_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.quickest_path_btn.setGeometry(QtCore.QRect(20, 150, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.quickest_path_btn.setFont(font)
        self.quickest_path_btn.setObjectName("quickest_path_btn")
        self.likely_path_btn = QtWidgets.QPushButton(self.centralwidget)
        self.likely_path_btn.setGeometry(QtCore.QRect(20, 230, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.likely_path_btn.setFont(font)
        self.likely_path_btn.setObjectName("likely_path_btn")
        Task.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Task)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 780, 21))
        self.menubar.setObjectName("menubar")
        Task.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Task)
        self.statusbar.setObjectName("statusbar")
        Task.setStatusBar(self.statusbar)

        self.retranslateUi(Task)
        self.subplot_btn.clicked.connect(self.subplotSlot)
        self.quickest_path_btn.clicked.connect(self.quickPathSlot)
        self.likely_path_btn.clicked.connect(self.likelyPathSlot)
        QtCore.QMetaObject.connectSlotsByName(Task)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Task", "Linknoide Tasks"))
        self.subplot_btn.setText(_translate("Task", "Subplots"))
        self.quickest_path_btn.setText(_translate("Task", "Quickest Path"))
        self.likely_path_btn.setText(_translate("Task", "Likely Path"))

    @pyqtSlot()
    def subplotSlot(self):
        pass

    @pyqtSlot()
    def quickPathSlot(self):
        pass

    @pyqtSlot()
    def likelyPathSlot(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Task = QtWidgets.QMainWindow()
    ui = Ui_Task()
    ui.setupUi(Task)
    Task.show()
    sys.exit(app.exec_())

