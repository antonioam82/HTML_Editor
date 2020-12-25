import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QMainWindow, QAction)

class HTMLeditor(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(780, 650)
        self.setWindowTitle('HTML Editor') 

        self.nav_bar = QHBoxLayout()

        self.html = """
       <!DOCTYPE HTML>
       <html>

        </html>

        """
        
        self.web_view = QWebEngineView() 
        self.web_view.setHtml(self.html)

        root = QVBoxLayout()
        self.textEdit = QTextEdit(self)
        self.btnTry = QPushButton("PROBAR")
        self.btnTry.clicked.connect(self.hello)
        root.addWidget(self.web_view)
        root.addWidget(self.textEdit)
        root.addWidget(self.btnTry)
        

        self.setLayout(root)

    def hello(self):
        print("Hello")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HTMLeditor()
    win.show()
    sys.exit(app.exec_())
