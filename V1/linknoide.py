from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, pyqtSlot
from final import Ui_MainWindow
from model import Model
import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

class HomeUIClass(Ui_MainWindow):
    def __init__(self):
        '''Initialize the super class
        '''
        super().__init__()
        self.model = Model()
        
    def setupUi(self, MW):
        ''' Setup the UI of the super class, and add here code
        that relates to the way we want our UI to operate.
        '''
        super().setupUi(MW)

    def refreshAll(self):
        '''
        Updates the widgets whenever an interaction happens.
        Typically some interaction takes place, the UI responds,
        and informs the model of the change. Then this method
        is called, pulling from the model information that is
        updated in the GUI.
        '''
        self.path_indicator.setText(self.model.getFileName())
        self.preview_window.setText(self.model.getFileContents())
        self.generate_btn.setEnabled(True)

    def makeNetwork(self):
        #Load the data
        fileName = self.model.getFileName()
        df = pd.read_csv(fileName)

        #Automate using predictions for full scale version
        g = nx.DiGraph()

        #Add edges into the network
        for i, elrow in df.iterrows():
           g.add_edge(elrow[1], elrow[0], attr_dict=elrow[2])

        for i, elrow in df.iterrows():
            g.add_node(elrow[0])
        return g

    # def subgraph(self, term):
    #     fileName = self.model.getFileName()
    #     df = pd.read_csv(fileName)
    #     # automate using predictions for full scale version
    #     color = pd.DataFrame(
    #         data=['silver'] * len(df.index))
    #     df['color'] = color
    #     df_sub = df.loc[df['Task_ID'] == term]
    #     g = nx.DiGraph()
 
    #     # Add edges into network
    #     for i, elrow in df_sub.iterrows():
    #         g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2])
    #     return g

    # slot
    def pathSlot(self):
        ''' Called when the user enters a string in the line edit and
        presses the ENTER key.
        '''
        fileName =  self.path_indicator.text()
        if self.model.isValid(fileName):
            self.model.setFileName(self.path_indicator.text())
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName)
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.path_indicator.setText("")
            self.refreshAll()
            self.debugPrint("Invalid file specified: " + fileName)

    # slot
    def browseSlot(self):
        ''' Called when the user presses the Browse button
        '''
        options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "Select File",
                        "",
                        "All Files (*);;CSV Files (*.csv)",
                        options=options)
        if fileName:
            self.model.setFileName(fileName)
            self.refreshAll()

    # slot
    def generateSlot(self):
        ''' Called when the user presses the Generate button
        '''
        self.figure.clf()

        g = self.makeNetwork()

        #labels = nx.get_edge_attributes(g, elrow[2])
        nPos = nx.spring_layout(g)
        #nx.draw(g, pos)
        nx.draw_networkx(g, pos=nPos, node_size=500, alpha=.45, node_color='r', edge_color='silver', arrows=True, with_labels=True)
        labels = nx.get_edge_attributes(g, "attr_dict")
        nx.draw_networkx_edge_labels(g, pos=nPos, edge_labels=labels, font_color="k", alpha=.2)
        plt.title('Project Activity Sequence', size=13)
        plt.axis("on")
        self.canvas.draw()
        self.generate_btn.setEnabled(False)
        # self.sub_plot_btn.setEnabled(True)

    # def subPlotSlot(self, name):
    #     self.figure.clf()
    #     g = self.subgraph(name)
    #     nPos = nx.spring_layout(g)
    #     nx.draw_networkx(g, pos=nPos, node_size=500, alpha=.45, node_color='r', arrows=True, with_labels=True)
    #     labels = nx.get_edge_attributes(g, "attr_dict")
    #     nx.draw_networkx_edge_labels(g, pos=nPos, edge_labels=labels, font_color='black', alpha=.2)
    #     plt.title('Project Activity Sequence \n filtered by \'' + name + '\'', size=13)
    #     plt.axis("off")
    #     self.canvas.draw()

    # def onclick(self, event):
    #     clickX = event.x
    #     clickY = event.y


def main():
    """
    This is the MAIN ENTRY POINT of our application. The code at the end
    of the mainwindow.py script will not be executed, since this script is now
    our main program. We have simply copied the code from mainwindow.py here
    since it was automatically generated by '''pyuic5'''.

    """
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()