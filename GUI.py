import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QLabel, QComboBox
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import design



class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'MultiLingual Speech Converter(MSC)'
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.left = 10
        self.top = 50
        self.width = 400
        self.height = 650
        self.setObjectName("main_window")
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet(design.stylesheet)
        self.initUI()

    def initUI(self):
        self.r1 = sr.Recognizer()
        self.r2 = sr.Recognizer()
        self.r3 = sr.Recognizer()
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.frame_for_message = QFrame(self)
        self.frame_for_message.setGeometry(20, 200, 350, 200)
        self.frame_for_message.setObjectName("msg")
        self.frame_for_message.setFrameShape(QFrame.StyledPanel)
        self.frame = QFrame(self)
        self.frame.setObjectName("Source_lang")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(0.6)
        self.frame1 = QFrame(self)
        self.frame1.setObjectName("destination_lang")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setLineWidth(0.6)
        self.frame.setGeometry(20, 100, 350, 200)
        self.frame1.setGeometry(20, 320, 350, 200)
        self.button = QComboBox(self.frame_for_message)
        self.button.setObjectName('B1')
        self.button1 = QComboBox(self.frame_for_message)
        self.button1.setObjectName('B2')
        self.button.addItem('English')
        self.button.addItem('Hindi')
        self.button.addItem('Punjabi')
        self.button1.addItem('Hindi')
        self.button1.addItem('English')
        self.button1.addItem('Punjabi')
        # self.button.setIcon(QtGui.QIcon('icon1.jpg'))
        # self.button.setIconSize(QtCore.QSize(50,40))
        # self.button1.setIcon(QtGui.QIcon('exit.jpg'))
        # self.button1.setIconSize(QtCore.QSize(50, 40))
        # self.button.clicked.connect(self.on_click)
        # self.button1.clicked.connect(self.action_b1)
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.button.setVisible(False)
        self.button1.setVisible(False)
        self.label = QLabel(self.frame_for_message)
        self.label.setObjectName('msg1')
        self.label.setText("Welcome to MSC")
        self.label.move(70, 50)
        self.start_btn = QPushButton("Start..", self.frame_for_message)
        self.start_btn.setObjectName("start")
        self.start_btn.move(100, 100)
        self.start_btn.clicked.connect(self.start_action)
        self.go_btn = QPushButton("Go.", self.frame_for_message)
        self.go_btn.setObjectName("Go")
        self.go_btn.setVisible(False)
        self.go_btn.clicked.connect(self.go_action)
        self.conversation = QPushButton("Speak", self)
        self.conversation.setObjectName("Speak")
        self.conversation.move(120, 550)
        self.conversation.setVisible(False)
        self.conversation.clicked.connect(self.conv_action)
        self.label1 = QLabel(self.frame)
        self.label1.setObjectName("lang1")
        self.label1.move(120, 5)
        self.label1.setFixedSize(350, 30)
        self.label2 = QLabel(self.frame1)
        self.label2.setFixedSize(350, 30)
        self.label2.setObjectName("lang2")
        self.label2.move(120, 5)
        self.back_arrow1 = QLabel(self)
        self.back_arrow1.setObjectName("back_arrow1")
        self.back_arrow1.move(35, 50)
        self.back_arrow1.setTextFormat(Qt.RichText)
        self.back_arrow1.setText("&#8592")
        self.back_arrow1.setVisible(False)
        self.back_arrow1.mousePressEvent = self.back_action
        self.lang1=QLabel(self.frame)
        self.lang2=QLabel(self.frame1)
        self.lang1.setObjectName("l1")
        self.lang2.setObjectName("l2")
        self.lang1.move(20, 50)
        self.lang2.move(20, 50)
        self.lang1.setFixedSize(350, 30)
        self.lang2.setFixedSize(350, 30)
        self.show()

    @pyqtSlot()
    def conv_action(self):
        with sr.Microphone() as source:
            print('Speak now')
            audio = self.r3.listen(source)
        if 'hi' in self.r2.recognize_google(audio):
            r2 = sr.Recognizer()
            url = 'https://www.youtube.com/results?search_query='
            # while(1):
            with sr.Microphone() as source:
                # print('search your query: ')
                audio = r2.listen(source)

                try:
                    get = r2.recognize_google(audio)
                    if 'exit' in get:
                        exit(0)
                    print(get)
                    # wb.get().open_new(url+get)

                except sr.UnknownValueError:
                    print('error')
                except sr.RequestError as e:
                    print('failed'.format(e))
        mytext = get
        self.lang1.setText(mytext)
        translator = Translator()
        result = translator.translate(mytext, dest='hi')
        print(result.text)
        self.lang2.setText(result.text)
        language = 'hi'
        myobj = gTTS(text=result.text, lang=language, slow=False)
        myobj.save("welcome.mp3")
        os.system("welcome.mp3")



    def start_action(self):
        self.start_btn.setVisible(False)
        self.label.move(5, 40)
        self.label.resize(335, 50)
        self.label.setText("Choose your corresponding Languages")
        self.button.setVisible(True)
        self.button1.setVisible(True)
        self.button.move(50, 100)
        self.button1.move(150, 100)
        self.go_btn.setVisible(True)
        self.go_btn.move(100, 150)

    def go_action(self):
        self.l1 = self.button.currentText()
        self.l2 = self.button1.currentText()
        # print(self.l1)
        # print(self.l2)
        self.frame_for_message.setVisible(False)
        self.button1.setVisible(False)
        self.button.setVisible(False)
        self.frame.setVisible(True)
        self.frame1.setVisible(True)
        self.conversation.setVisible(True)
        self.label1.setText(self.l1)
        self.label2.setText(self.l2)
        self.back_arrow1.setVisible(True)

    def back_action(self,event):
        self.frame.setVisible(False)
        self.frame1.setVisible(False)
        self.conversation.setVisible(False)
        self.back_arrow1.setVisible(False)
        self.frame_for_message.setVisible(True)
        self.button1.setVisible(True)
        self.button.setVisible(True)
        self.go_btn.setVisible(True)
        self.label.setVisible(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())