from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

class Ui_Window(QObject):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(1391, 619)
        self.centralwidget = QtWidgets.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.file_upload_area = QtWidgets.QFrame(self.centralwidget)
        self.file_upload_area.setGeometry(QtCore.QRect(20, 90, 1331, 43))
        self.file_upload_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.file_upload_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.file_upload_area.setObjectName("file_upload_area")
        self.gridLayout = QtWidgets.QGridLayout(self.file_upload_area)
        self.gridLayout.setObjectName("gridLayout")
        self.upload_instruction = QtWidgets.QLabel(self.file_upload_area)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.upload_instruction.setFont(font)
        self.upload_instruction.setObjectName("upload_instruction")
        self.gridLayout.addWidget(self.upload_instruction, 0, 0, 1, 1)
        self.path_indicator = QtWidgets.QLineEdit(self.file_upload_area)
        self.path_indicator.setObjectName("path_indicator")
        self.gridLayout.addWidget(self.path_indicator, 0, 1, 1, 1)
        self.browse_btn = QtWidgets.QPushButton(self.file_upload_area)
        self.browse_btn.setObjectName("browse_btn")
        self.gridLayout.addWidget(self.browse_btn, 0, 2, 1, 1)
        self.app_title = QtWidgets.QLabel(self.centralwidget)
        self.app_title.setGeometry(QtCore.QRect(20, 30, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.app_title.setFont(font)
        self.app_title.setObjectName("app_title")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 180, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.canvas_area = QtWidgets.QFrame(self.centralwidget)
        self.canvas_area.setGeometry(QtCore.QRect(282, 150, 1071, 401))
        self.canvas_area.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.canvas_area.setFrameShadow(QtWidgets.QFrame.Raised)
        self.canvas_area.setObjectName("canvas_area")
        self.canvas_grid = QtWidgets.QGridLayout(self.canvas_area)
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas_grid.addWidget(self.canvas, 0, 1, 10, 10)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(19, 149, 201, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.layoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-8, -1, 211, 351))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.preview_window = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.preview_window.setGeometry(QtCore.QRect(-8, -1, 211, 351))
        self.preview_window.setFrameShape(QtWidgets.QFrame.Box)
        self.preview_window.setText("")
        self.preview_window.setObjectName("preview_window")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.generate_btn = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.generate_btn.setFont(font)
        self.generate_btn.setObjectName("generate_btn")
        self.verticalLayout.addWidget(self.generate_btn)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 570, 1021, 25))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sub_plot_btn = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.sub_plot_btn.setFont(font)
        self.sub_plot_btn.setObjectName("sub_plot_btn")
        self.horizontalLayout_2.addWidget(self.sub_plot_btn)
        self.quick_path_btn = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.quick_path_btn.setFont(font)
        self.quick_path_btn.setObjectName("quick_path_btn")
        self.horizontalLayout_2.addWidget(self.quick_path_btn)
        self.Likely_path_btn = QtWidgets.QPushButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Likely_path_btn.setFont(font)
        self.Likely_path_btn.setObjectName("Likely_path_btn")
        self.horizontalLayout_2.addWidget(self.Likely_path_btn)
        window.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(window)
        self.statusbar.setObjectName("statusbar")
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        self.browse_btn.clicked.connect(self.browseSlot)
        self.Likely_path_btn.clicked.connect(self.likelyPathSlot)
        self.quick_path_btn.clicked.connect(self.quickPathSlot)
        self.sub_plot_btn.clicked.connect(self.subPlotSlot)
        self.generate_btn.clicked.connect(self.generateSlot)
        self.path_indicator.returnPressed.connect(self.pathSlot)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "Linknoide"))
        self.upload_instruction.setText(_translate("Window", "Select File"))
        self.browse_btn.setText(_translate("Window", "Browse"))
        self.app_title.setText(_translate("Window", "Linknoide"))
        self.generate_btn.setText(_translate("Window", "Generate"))
        self.sub_plot_btn.setText(_translate("Window", "Sub Plot"))
        self.quick_path_btn.setText(_translate("Window", "Quick Path"))
        self.Likely_path_btn.setText(_translate("Window", "Likely Path"))

    @pyqtSlot()
    def browseSlot(self):
        pass

    @pyqtSlot()
    def generateSlot(self):
        pass

    @pyqtSlot()
    def pathSlot(self):
        pass

    @pyqtSlot()
    def subPlotSlot(self):
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
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())