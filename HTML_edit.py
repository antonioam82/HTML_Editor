import sys
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import (QWidget, QApplication, QLineEdit,
QVBoxLayout, QHBoxLayout, QPushButton, QMessageBox, QTextEdit, QMainWindow, QFileDialog, QAction)

class HTMLeditor(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 750)
        self.setWindowTitle('HTML Editor')
        self.file_path = None

        self.nav_bar = QHBoxLayout()

        self.html = """
       <!DOCTYPE HTML>
       <html>
       <body>
       <h1>Hello To Your HTML Editor</h1>
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
        root.addWidget(self.web_view)
        root.addWidget(self.textEdit)
        root.addWidget(self.btnTry)
        root.addWidget(self.btnSave)
        

        self.setLayout(root)

    def get_code(self):
        self.mytext = self.textEdit.toPlainText()
        if self.mytext != "":
            self.html=self.mytext
            self.web_view.setHtml(self.html)
            #print(mytext)

    def save_doc(self):
        if not self.file_path:
            new_file_path, filter_type = QFileDialog.getSaveFileName(self, "Save this file as...", "", "HTML Files(*.html);;Text Files(*.txt)")
            if new_file_path:
                self.file_path = new_file_path
                print("ok1")
            else:
                self.invalid_path_alert_message()
                return False
        file_contents = self.textEdit.toPlainText()
        print("ok2")
        with open(self.file_path, "w") as f:
            f.write(file_contents)
        print("OK3")
        self.file_path = None
        print("ok4")

    
    def invalid_path_alert_message(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Invalid file")
        messageBox.setText("Selected filename or path is not valid. Please select a valid file.")
        messageBox.exec()                
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = HTMLeditor()
    win.show()
    sys.exit(app.exec_())

