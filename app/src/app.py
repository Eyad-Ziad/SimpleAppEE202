import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QMessageBox,QAbstractButton
from  mainwindow import First
from login import Login 


def popup(title,msg):
        msg_popup= QMessageBox()
        msg_popup.setIcon(QMessageBox.Information)
        msg_popup.setText(msg)
        msg_popup.setWindowTitle(title)
        msg_popup.setStandardButtons(QMessageBox.Ok)
        msg_popup.exec()



def login():
         username_in=(username.text())
         password_in=(password.text())

         if (username_in !="Q" or password_in != "91"):
                popup("invalid username or password","Login Failed!")
         else:
                 print("Logged in successfully")
                 LW.close()
                 MW.show()


def hide_info_page():
        if MW.hide_show_button.isChecked():
                MW.main_left_widget.hide()

        else:
                MW.main_left_widget.show()
        




if __name__ =="__main__":

    app=QtWidgets.QApplication([])

    #Start event loop
    retVal = app.exec_()

    #Login Window
    LW = Login()
    #Main window
    MW = First()




    #Show program
    LW.show()
    
    #Take login data
    username= LW.username_line
    password= LW.password_line
    
    #Check
    LW.login_in_button.clicked.connect(login)


    #Hide or show left menubar
    MW.hide_show_button.clicked.connect(hide_info_page)




    #Close program
    exit(retVal)





