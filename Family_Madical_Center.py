from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import *
from UImain import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("FAMILY MADICAL CENTER")
        self.ui.lineEdit.setPlaceholderText("Search Here...")
        self.ui.tabs.setTabText(0,"HOME")
        self.ui.tabs.setTabText(3,"Results")
        self.ui.tabs.setTabText(2,"doctor2")
        self.ui.tabs.setTabText(-1,"History")
        self.ui.tabs.setTabText(1,self.ui.doc3.text().replace("Dr.",""))
        self.ui.lineEdit.returnPressed.connect(self.search)
        self.ui.doc3.clicked.connect(lambda: self.ui.tabs.setCurrentWidget(self.ui.doctor1))
        self.ui.pushButton_5.clicked.connect(self.add_doctor)
        self.ui.normal.clicked.connect(self.azra_normal)
        self.ui.doc5.setVisible(False)
        self.ui.lineEdit_2.setVisible(False)
        self.ui.lineEdit_2.returnPressed.connect(self.add_doc)
        self.ui.frame_8.setVisible(False)
        self.ui.lineEdit_3.setVisible(False)
        self.ui.lineEdit_3.returnPressed.connect(self.search)
        self.lineazra = QShortcut(QKeySequence('/'),self)
        self.lineazra.activated.connect(self.show_lineazra)
        

    

    def search(self):
        search = self.ui.lineEdit.text().upper()
        self.ui.tabs.setCurrentWidget(self.ui.search_tab)
        if search not in self.ui.label_9.text():
            self.ui.search_label.setText("NO Results Found")
            self.ui.frame_5.setVisible(False) 

        elif search in self.ui.label_9.text():
            self.ui.search_label.setText("Results Found")
            self.ui.frame_5.setVisible(True)
        self.ui.lineEdit_3.setVisible(False)
    
    def add_doc(self):
        self.ui.doc5.setText(self.ui.lineEdit_2.text())
        self.ui.lineEdit_2.setVisible(False)

    def add_doctor(self):
        self.ui.lineEdit_2.setVisible(True)
        self.ui.doc5.setVisible(True)
        
    def azra_normal(self):   
        if self.ui.normal.isChecked(): 
            self.ui.frame_8.setVisible(True)
            
        elif self.ui.normal.isChecked()==False:
            self.ui.frame_8.setVisible(False)
    
    def show_lineazra(self):
        if self.ui.tabs.currentWidget()==self.ui.doctor1:
            self.ui.lineEdit_3.setVisible(True)
        elif self.ui.tabs.currentWidget() != self.ui.doctor1:
            self.ui.lineEdit_3.setVisible(False)
    

            
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec_())