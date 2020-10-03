from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import pymysql



MainUI,_ = loadUiType('index.ui')


class Main(QMainWindow , MainUI):
    def __init__(self , perent=None):
        super(Main,self).__init__(perent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.DB_Connect()
        self.Handel_All_Buttons()
        self.UI_Chang()

#all the change that you whant to aberr in screen when the appliction start up
    def UI_Chang(self):
        self.tabWidget_2.tabBar().setVisible(False)
    

#the connection to the DataBase
    def DB_Connect(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Pa$$w0rd', db='my_app')
        self.cur= self.db.cursor()
        print('conect to DB')

#to handel all the buttons in the application
    def Handel_All_Buttons(self):
        self.pushButton_3.clicked.connect(self.Add_New_Client)
        self.pushButton.clicked.connect(self.Open_Main_Win)
########################################
    ######### Clients #################
    def Show_All_Clients(self):
       pass


    def Add_New_Client(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
    def Open_Main_Win(self):
        self.tabWidget.setCurrentIndex(0)

    def Search_Client(self):
        pass
    def Edit_Client(self):
        pass

    def Delete_Client(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()