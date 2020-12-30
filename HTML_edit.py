import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QWidget, QLineEdit, QMainWindow, QApplication,
QPushButton,QVBoxLayout,QMessageBox,QTextEdit, QMainWindow, QFileDialog)

class HTMLeditor(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 750)
        self.setWindowTitle('HTML Editor')
        self.file_path = None
        

        self.html = """
       <!DOCTYPE HTML>
       <html>
       <body>
       <h1>Hello To Your HTML Editor...</h1>
       <h2>Use the bottom box to prove you HTML code</h2>
       </body>
        </html>
        """
        
        self.web_view = QWebEngineView() 
        self.web_view.setHtml(self.html)

        root = QVBoxLayout()
        self.textEdit = QTextEdit(self)
        self.btnTry = QPushButton("PROBAR")
        self.btnTry.clicked.connect(self.get_code)
        self.btnSave = QPushButton("GUARDAR")
        self.btnSave.clicked.connect(self.save_doc)
        self.btnOpen = QPushButton("ABRIR")
        self.btnOpen.clicked.connect(self.open_file)
        root.addWidget(self.web_view)
        root.addWidget(self.textEdit)
        root.addWidget(self.btnTry)
        root.addWidget(self.btnSave)
        root.addWidget(self.btnOpen)
        

        self.setLayout(root)

    def get_code(self):
        self.mytext = self.textEdit.toPlainText()
        if self.mytext != "":
            self.html=self.mytext
            self.web_view.setHtml(self.html)

    def save_doc(self):
        try:
            if not self.file_path:
                new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Save this file as...", "", "HTML Files(*.html);;Text Files(*.txt)")
                if new_file_path:
                    self.file_path = new_file_path
                else:
                    self.window_message("NO CREATED","File not created.")
                    return False
            file_contents = self.textEdit.toPlainText()
            with open(self.file_path, "w") as f:
                f.write(file_contents)
            self.window_message("TASK COMPLETED","File created successfully.")
            
        except Exception as e:
            self.window_message("ERROR",str(e))
        self.file_path = None

    def window_message(self,title,message):
        messageBox = QMessageBox()
        messageBox.setWindowTitle(title)
        messageBox.setText(message)
        messageBox.exec()

    def open_file(self):
        text_file = QFileDialog.getOpenFileName(self, 'Open File', 'C:\\', 'Text Files (*.txt)')

        if text_file[0]:
            with open(text_file[0], 'r') as f:
                datos = '#'+f.read()
            self.textEdit.setText(datos)
            self.get_code()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HTMLeditor()
    win.show()
    sys.exit(app.exec_())


