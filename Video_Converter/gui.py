from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from main import *

class Ui_VideoConverter(object):
    def setupUi(self, VideoConverter):
        self.MainWindow = VideoConverter
        VideoConverter.setObjectName("VideoConverter")
        VideoConverter.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(VideoConverter)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.file_save)
        self.gridLayout.addWidget(self.saveButton, 2, 1, 1, 1)
        self.openButton = QtWidgets.QPushButton(self.centralwidget)
        self.openButton.setObjectName("openButton")
        self.openButton.clicked.connect(self.file_open)
        self.gridLayout.addWidget(self.openButton, 1, 1, 1, 1)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setObjectName("start")
        self.start.clicked.connect(self.start_fun)
        self.gridLayout.addWidget(self.start, 3, 0, 1, 2)
        self.OpenSrc = QtWidgets.QLabel(self.centralwidget)
        self.OpenSrc.setFrameShape(QtWidgets.QFrame.Box)
        self.OpenSrc.setText("")
        self.openSrcText = ""
        self.OpenSrc.setObjectName("OpenSrc")
        self.gridLayout.addWidget(self.OpenSrc, 1, 0, 1, 1)
        self.codeList = QtWidgets.QListWidget(self.centralwidget)
        self.codeList.setObjectName("codeList")
        self.gridLayout.addWidget(self.codeList, 4, 0, 1, 2)
        self.SaveSrc = QtWidgets.QLabel(self.centralwidget)
        self.SaveSrc.setFrameShape(QtWidgets.QFrame.Box)
        self.SaveSrc.setFrameShadow(QtWidgets.QFrame.Plain)
        self.SaveSrc.setText("")
        self.saveSrcText = ""
        self.SaveSrc.setObjectName("SaveSrc")
        self.gridLayout.addWidget(self.SaveSrc, 2, 0, 1, 1)
        VideoConverter.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VideoConverter)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        VideoConverter.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VideoConverter)
        self.statusbar.setObjectName("statusbar")
        VideoConverter.setStatusBar(self.statusbar)
        self.running = False

        self.retranslateUi(VideoConverter)
        QtCore.QMetaObject.connectSlotsByName(VideoConverter)

    def retranslateUi(self, VideoConverter):
        _translate = QtCore.QCoreApplication.translate
        VideoConverter.setWindowTitle(_translate("VideoConverter", "MainWindow"))
        self.saveButton.setText(_translate("VideoConverter", "Save Location"))
        self.openButton.setText(_translate("VideoConverter", "Open Video"))
        self.start.setText(_translate("VideoConverter", "Start conversion"))

    def file_open(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self.MainWindow, 'Open File', '', 'Videos (*.mov *.mp4 *.avi *.flv)')
        self.openSrcText = filename
        self.OpenSrc.setText(filename)

    def file_save(self):
        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self.MainWindow, 'Save File', '', 'Videos (*.mov *.mp4 *.avi *.flv)')
        self.saveSrcText = filename
        self.SaveSrc.setText(filename)

    def addToList(self, text):
        self.codeList.addItem(text)

    def checkFileType(self,text):
        videoTypes = ['.mp4', '.mov', '.flv', '.avi']
        if(text[-4:] in videoTypes):
            return True
        else:
            return False

    def start_fun(self):
        if(self.openSrcText != "" and self.saveSrcText != ""):
            if(self.checkFileType(self.openSrcText) and self.checkFileType(self.saveSrcText)):
                self.openButton.setEnabled(False)
                self.saveButton.setEnabled(False)
                self.start.setText("Cancel")
                self.addToList(self.openSrcText)
                self.MainWindow.hide()
                mainFunc(self.openSrcText, self.saveSrcText)
            elif(self.checkFileType(self.openSrcText)):
                self.addToList(str("'" + self.saveSrcText + "' is not a video"))
            else:
                self.addToList(str("'" + self.openSrcText + "' is not a video"))
        else:
            self.addToList("You need to select a video AND a name and location for the exported one")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    VideoConverter = QtWidgets.QMainWindow()
    ui = Ui_VideoConverter()
    ui.setupUi(VideoConverter)
    VideoConverter.show()
    sys.exit(app.exec_())