from __future__ import unicode_literals
import sys
from PyQt5 import QtWidgets,QtGui,QtCore
import youtube_dl

class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui()
        
    def ui(self):
        
        self.setGeometry(100,60,1000,350)
        
        self.setStyleSheet("background-color: black;")
        self.setWindowTitle("Youtube Video Translate")
        
        pixmap = QtWidgets.QLabel("Youtube",self)
        pixmap.setPixmap(QtGui.QPixmap("youtube.png"))
        pixmap.setAlignment(QtCore.Qt.AlignCenter)
        
        self.url = QtWidgets.QLineEdit()
        self.url.setStyleSheet("background-color: grey;color:white;")
        
        self.cbox = QtWidgets.QComboBox()
        self.cbox.setStyleSheet("background-color: grey;color:white;")
        self.cbox.addItems(["mp3","wav"])
        
        self.button = QtWidgets.QPushButton("İndir")
        self.button.setStyleSheet("background-color: green;color:white;")
        self.button.clicked.connect(self.cevir)
        
        h_box = QtWidgets.QHBoxLayout()
        v_box = QtWidgets.QVBoxLayout(self)
        
        
        h_box.addWidget(self.url)
        h_box.addWidget(self.cbox)
        
        v_box.addWidget(pixmap)
        v_box.addLayout(h_box)
        v_box.addWidget(self.button)
        v_box.addStretch()
        
        self.show()
        
    def cevir(self):
        link = self.url.text()
        ydl_format = self.cbox.currentText()
        
        ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': ydl_format,
                'preferredquality': '320',}],
                "dowload_archive" : "/home/batu"
                    }

        ydl = youtube_dl.YoutubeDL(ydl_opts)
        ydl.download([link])
        
        
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())