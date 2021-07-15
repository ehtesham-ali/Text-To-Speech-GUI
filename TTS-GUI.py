from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser
import pyttsx3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(445, 427)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.engine = pyttsx3.init()
        self.volume = self.engine.getProperty('volume')
        self.rate = self.engine.getProperty('rate')
        self.voices = self.engine.getProperty('voices')

        self.volume_name = 10
        self.volume_data = 0.1
        self.speechrate_value = 100

        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(0, 0, 441, 91))
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 60, 361, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.textedit_message = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.textedit_message.setGeometry(QtCore.QRect(20, 90, 251, 181))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.textedit_message.setFont(font)
        self.textedit_message.setObjectName("textedit_message")

        self.label_volume = QtWidgets.QLabel(self.centralwidget)
        self.label_volume.setGeometry(QtCore.QRect(310, 90, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_volume.setFont(font)
        self.label_volume.setAlignment(QtCore.Qt.AlignCenter)
        self.label_volume.setObjectName("label_volume")

        self.combobox_volume = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_volume.setGeometry(QtCore.QRect(310, 120, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combobox_volume.setFont(font)
        self.combobox_volume.setObjectName("combobox_volume")
        for _ in range(1, 11):
            self.combobox_volume.addItem(f'{self.volume_name}%', str(self.volume_data))
            self.volume_name += 10
            self.volume_data += 0.10

        self.combobox_speechrate = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_speechrate.setGeometry(QtCore.QRect(310, 180, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combobox_speechrate.setFont(font)
        self.combobox_speechrate.setEditable(True)
        self.combobox_speechrate.setObjectName("combobox_speechrate")
        for _ in range(1,11):
            self.combobox_speechrate.addItem(str(self.speechrate_value))
            self.speechrate_value += 100


        self.label_speechrate = QtWidgets.QLabel(self.centralwidget)
        self.label_speechrate.setGeometry(QtCore.QRect(290, 150, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_speechrate.setFont(font)
        self.label_speechrate.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speechrate.setObjectName("label_speechrate")

        self.label_misc1 = QtWidgets.QLabel(self.centralwidget)
        self.label_misc1.setGeometry(QtCore.QRect(20, 280, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_misc1.setFont(font)
        self.label_misc1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_misc1.setObjectName("label_misc1")

        self.label_misc2 = QtWidgets.QLabel(self.centralwidget)
        self.label_misc2.setGeometry(QtCore.QRect(20, 290, 381, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_misc2.setFont(font)
        self.label_misc2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_misc2.setObjectName("label_misc2")

        self.label_voice = QtWidgets.QLabel(self.centralwidget)
        self.label_voice.setGeometry(QtCore.QRect(290, 210, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_voice.setFont(font)
        self.label_voice.setAlignment(QtCore.Qt.AlignCenter)
        self.label_voice.setObjectName("label_voice")

        self.combobox_voice = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_voice.setGeometry(QtCore.QRect(310, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.combobox_voice.setFont(font)
        self.combobox_voice.setEditable(False)
        self.combobox_voice.setObjectName("combobox_voice")
        self.combobox_voice.addItem('Male', self.engine.setProperty('voice', self.voices[0].id))
        self.combobox_voice.addItem('Female', self.engine.setProperty('voice', self.voices[1].id))

        self.button_listen = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_listen())
        self.button_listen.setGeometry(QtCore.QRect(50, 340, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_listen.setFont(font)
        self.button_listen.setObjectName("button_listen")
        def func_listen():
            self.engine.setProperty('rate', int(self.combobox_speechrate.currentText()))
            self.engine.setProperty('volume', float(self.combobox_volume.currentData()))
            self.engine.setProperty('voice', self.combobox_voice.currentData())

            print(f'''
RATE: {int(self.combobox_speechrate.currentText())}
VOLUME: {float(self.combobox_volume.currentData())}
VOICE: {self.combobox_voice.currentData()} # None expected, read the docs
            ''')

            self.engine.say(str(self.textedit_message.toPlainText()))

            self.engine.runAndWait()
            self.engine.stop()

        self.button_download = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_download())
        self.button_download.setGeometry(QtCore.QRect(250, 340, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.button_download.setFont(font)
        self.button_download.setObjectName("button_download")
        def func_download():
            self.label_status.setText('Downloading TTS...')
            self.engine.save_to_file(str(self.textedit_message.toPlainText()), 'TextToSpeechFile.mp3')

            self.engine.runAndWait()
            self.engine.stop()

            self.label_status.setText('Download Complete!')


        self.button_help = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: func_help())
        self.button_help.setGeometry(QtCore.QRect(420, 400, 21, 23))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        self.button_help.setFont(font)
        self.button_help.setObjectName("button_help")
        def func_help():
            webbrowser.open('https://www.notion.so/Text-To-Speech-GUI-e8f03601dea04ffd90a2901496c18358')

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(100, 400, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setObjectName("label_status")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Text To Speech"))
        self.label_title.setText(_translate("MainWindow", "Text To Speech Creator"))
        self.textedit_message.setPlainText(_translate("MainWindow", "Enter TTS message here"))
        self.label_volume.setText(_translate("MainWindow", "Volume"))
        self.label_speechrate.setText(_translate("MainWindow", "Speech Rate"))
        self.label_misc1.setText(_translate("MainWindow", "The lower the speech rate, the slower it will speak;"))
        self.label_misc2.setText(_translate("MainWindow", "The higher the speech rate, the faster it will speak; 200 is normal"))
        self.label_voice.setText(_translate("MainWindow", "Voice"))
        self.button_listen.setText(_translate("MainWindow", "Listen"))
        self.button_download.setText(_translate("MainWindow", "Download"))
        self.button_help.setText(_translate("MainWindow", "?"))
        self.label_status.setText(_translate("MainWindow", "..."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
