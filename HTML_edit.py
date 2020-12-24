import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit, QMainWindow, QAction)

class HTMLeditor(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(740, 520)
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
        self.textEdit.resize(200,100)
        self.btnTry = QPushButton("PROBAR")
        root.addWidget(self.web_view)
        root.addWidget(self.textEdit)
        root.addWidget(self.btnTry)

        self.setLayout(root)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HTMLeditor()
    win.show()
    sys.exit(app.exec_())
