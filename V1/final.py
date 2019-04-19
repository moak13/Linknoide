from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbarfrom


class Ui_MainWindow(QObject):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1365, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(20, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.app_title.setFont(font)
        self.app_title.setObjectName("app_title")
        self.file_upload_area = QtWidgets.QFrame(self.centralwidget)
        self.file_upload_area.setGeometry(QtCore.QRect(20, 60, 1331, 43))
        self.file_upload_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_upload_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_upload_area.setObjectName("file_upload_area")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.file_upload_area)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.upload_instruction = QtWidgets.QLabel(self.file_upload_area)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.upload_instruction.setFont(font)
        self.upload_instruction.setObjectName("upload_instruction")
        self.horizontalLayout.addWidget(self.upload_instruction)
        self.path_indicator = QtWidgets.QLineEdit(self.file_upload_area)
        self.path_indicator.setObjectName("path_indicator")
        self.horizontalLayout.addWidget(self.path_indicator)
        self.browse_btn = QtWidgets.QPushButton(self.file_upload_area)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        self.browse_btn.setFont(font)
        self.browse_btn.setObjectName("browse_btn")
        self.browse_btn.setStyleSheet("background-color: skyblue")
        self.horizontalLayout.addWidget(self.browse_btn)
        self.canvas_window = QtWidgets.QFrame(self.centralwidget)
        self.canvas_window.setGeometry(QtCore.QRect(319, 129, 1031, 511))
        self.canvas_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.canvas_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.canvas_window.setObjectName("canvas_window")
        self.canvas_grid = QtWidgets.QGridLayout(self.canvas_window)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas_grid.addWidget(self.canvas, 0, 1, 10, 10)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 130, 261, 511))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.preview_window = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.preview_window.setFont(font)
        self.preview_window.setFrameShape(QtWidgets.QFrame.Box)
        self.preview_window.setText("")
        self.preview_window.setObjectName("preview_window")
        self.verticalLayout.addWidget(self.preview_window)
        self.generate_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate_btn.setFont(font)
        self.generate_btn.setObjectName("generate_btn")
        self.generate_btn.setStyleSheet("background-color: lightgreen")
        self.generate_btn.setEnabled(False)
        self.verticalLayout.addWidget(self.generate_btn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1365, 21))
        self.menubar.setObjectName("menubar")
        self.app_Options = QtWidgets.QMenu(self.menubar)
        self.app_Options.setObjectName("app_Options")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Save_option = QtWidgets.QAction(MainWindow)
        self.Save_option.setObjectName("Save_option")
        self.Save_option.setShortcut('Ctrl+S')
        self.Save_option.triggered.connect(self.saveFile)
        self.Print_option = QtWidgets.QAction(MainWindow)
        self.Print_option.setObjectName("Print_option")
        self.Print_option.setShortcut('Ctrl+P')
        self.Print_option.triggered.connect(self.printFile)
        self.app_Options.addAction(self.Save_option)
        self.app_Options.addAction(self.Print_option)
        self.menubar.addAction(self.app_Options.menuAction())

        self.retranslateUi(MainWindow)
        self.browse_btn.clicked.connect(self.browseSlot)
        self.path_indicator.returnPressed.connect(self.pathSlot)
        self.generate_btn.clicked.connect(self.generateSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Linknoide"))
        MainWindow.setWindowIcon(QtGui.QIcon('asset/logo/app_icon.png'))
        self.app_title.setText(_translate("MainWindow", "Linknoide"))
        self.upload_instruction.setText(
            _translate("MainWindow", "Select File"))
        self.browse_btn.setText(_translate("MainWindow", "Browse"))
        self.generate_btn.setText(_translate("MainWindow", "Generate"))
        self.app_Options.setTitle(_translate("MainWindow", "File"))
        self.Save_option.setText(_translate("MainWindow", "Save"))
        self.Print_option.setText(_translate("MainWindow", "Print"))

    @pyqtSlot()
    def browseSlot(self):
        pass

    @pyqtSlot()
    def pathSlot(self):
        pass

    @pyqtSlot()
    def generateSlot(self):
        pass

    def saveFile(self):
        pass

    def printFile(self):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
