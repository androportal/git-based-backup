from PyQt4 import QtCore,QtGui  
import os,sys,ui_restore
from subprocess import Popen, PIPE

class backup(QtGui.QMainWindow):
    returnedDate = ""
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        uifile = ui_restore.Ui_MainWindow()
        uifile.setupUi(self)

        self.connect(uifile.calenderRestore,QtCore.SIGNAL("clicked(QDate)"),self.userDate)
        self.connect(uifile.restoreButton,QtCore.SIGNAL("clicked()"),self.userDate)

    def userDate(self,date):
        selectedDate = QtCore.QDate.toString(date,"yyyy, MM, dd")
        self.returnedDate = selectedDate
        print self.returnedDate, type(str(selectedDate))
        self.parsegitLog()

    def gitCheckout(self,logDate):
        print logDate

    def parsegitLog(self):
        parseLog = Popen('git log  --pretty=oneline',shell=True, stdout=PIPE).stdout.readlines()
        for logLines in parseLog:
            catchLine = logLines.split(' ',3)    
            logDate = catchLine[3]
            if logDate.strip() == str(self.returnedDate):
                catchlogMsg = catchLine[0]
                checkout = 'git checkout ' + catchlogMsg
                os.system(checkout)
            else:
                pass


##############################################################################################################

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = backup()
    window.show()
    window.parsegitLog()
    sys.exit(app.exec_())
