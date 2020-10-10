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
        self.pushButton_3.clicked.connect(self.Click_Add_New_Client_Main_Screen)
        self.pushButton.clicked.connect(self.Open_Main_Win)
        self.pushButton_6.clicked.connect(self.Open_Main_Win)
        self.pushButton_33.clicked.connect(self.Click_Add_New_Client)
########################################
    ######### Clients #################
    def Show_All_Clients(self):
       pass

    def Click_Add_New_Client(self):
        clint_name = self.lineEdit_24.text()
        clint_email =self.lineEdit_25.text()
        clint_phone = self.lineEdit_20.text()
        clint_start_date = self.dateTimeEdit.dateTime()
        formatted_datetime_SD = clint_start_date.toString('yyyy-MM-dd hh:mm:ss')
        clint_date_of_birth = self.dateEdit.date()
        formatted_date_DoB = clint_date_of_birth.toString('yyyy-MM-dd')
        clint_address = self.lineEdit_22.text()

        self.cur.execute('''

                    INSERT INTO person(name , email , phone ,TrainingStartDate,Address,birthday)
                    VALUES (%s , %s , %s , %s , %s , %s )
                ''', (clint_name, clint_email, clint_phone, formatted_datetime_SD, clint_address, formatted_date_DoB))
        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New CLient Added')
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(1)

    def Click_Add_New_Client_Main_Screen(self):
        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_6.setCurrentIndex(1)
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