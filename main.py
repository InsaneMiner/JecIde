from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDir



import libs.syntax as syntax
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.width = 700
        self.height = 500

        self.setMinimumWidth(self.width)
        self.setMinimumHeight(self.height)
        self.setWindowTitle("Bottle Ide")

        self.initWindow()
    def ColourModes(self,mode):
        if mode == 1:
            pass
        elif mode == 2:
            pass
    def initMainMenu(self):
        
        ColourModes = QtWidgets.QPushButton("Colour Modes")

        exitAct = QtWidgets.QAction('Exit', self)

        toolbar = self.addToolBar("Exit")

        
        

        Save = QtWidgets.QAction("Save",self)

        

        toolbar.addAction(Save)


        toolbar.addAction(exitAct)

        
        toolbar.addWidget(ColourModes)

        menu = QtWidgets.QMenu()
        menu.addAction("Light")
        menu.addAction("Dark")
        ColourModes.setMenu(menu)


        exitAct.triggered.connect(lambda: self.close())

        menu.triggered.connect(lambda action: self.MenuBarColourModes(action))
    

    def MenuBarColourModes(self,type):
        if type.text() == "Light":
            self.ColourModes(1)
        elif type.text() == "Dark":
            self.ColourModes(2)
    def initMainText(self):

        self.texter = QtWidgets.QPlainTextEdit()

        self.highlight = syntax.PythonHighlighter(self.texter.document())

        self.show()

        self.infile = open('simple.jec', 'r')
        self.texter.setPlainText(self.infile.read())

        self.setCentralWidget(self.texter)
    def filesystem(self):
        pass
        #this function displays a tree of the current directory

    def initWindow(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        self.initMainMenu()
        self.show()
        self.initMainText()
        self.show()
        self.filesystem()
        self.show()
        

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
