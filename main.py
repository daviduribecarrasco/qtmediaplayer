import sys

from PySide2.QtUiTools import QUiLoader #allows us to import .ui files
from PySide2.QtWidgets import QApplication, QLineEdit, QPushButton, QFileDialog, QAction, QSlider
from PySide2.QtCore import QFile, QObject, QUrl
from PySide2.QtMultimedia import QMediaPlayer

class MainWindow(QObject):

    #class constructor
    def __init__(self, ui_file, parent=None):
        
        
 
        #reference to our music player
        self.music_player = QMediaPlayer()
        self.music_player.setVolume(100)

        #call parent QObject constructor
        super(MainWindow, self).__init__(parent)

        #load the UI file into Python
        ui_file = QFile(ui_file)
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        self.window = loader.load(ui_file)
        
        
        ui_file.close()
        


        volume_slider = self.window.findChild(QSlider,'volume_slider')
        volume_slider.valueChanged.connect(self.volumeChanged)


        open_action = self.window.findChild(QAction, 'action_open')
        open_action.triggered.connect(self.open_action_triggered)

        quit_action = self.window.findChild(QAction, 'action_quit')
        quit_action.triggered.connect(self.quit_action_triggered)

        play_button = self.window.findChild(QPushButton, 'play_button')
        play_button.clicked.connect(self.play_button_clicked)

        pause_button = self.window.findChild(QPushButton, 'pause_button')
        pause_button.clicked.connect(self.pause_button_clicked)

        #show window to user
        self.window.show()

    def open_action_triggered(self):
        file_name = QFileDialog.getOpenFileName(self.window)
        self.music_player.setMedia(QUrl.fromLocalFile(file_name[0]))

    def pause_button_clicked(self):
        self.music_player.pause()

    def quit_action_triggered(self):
        self.window.close()

    def play_button_clicked(self):
        self.music_player.play()
    
    def volumeChanged(self):
        volume = self.window.findChild(QSlider,'volume_slider').value()
        self.music_player.setVolume(volume)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow('MainWindow.ui')
    sys.exit(app.exec_())
