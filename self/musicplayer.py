import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Music Player")
        self.setGeometry(100, 100, 300, 200)

        self.play_button = QPushButton("Play", self)
        self.play_button.setGeometry(100, 50, 100, 30)
        self.play_button.clicked.connect(self.browse_music)

    def browse_music(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Select Music File", "", "Music Files (*.mp3 *.wav)")
        if file_path:
            self.play_music(file_path)

    def play_music(self, file_path):
        # Add code to play music here using the file_path
        print(f"Playing music: {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    player = MusicPlayer()
    player.show()
    sys.exit(app.exec_())
