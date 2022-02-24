# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from window import Window
import sys



if __name__ == "__main__":   
    syntaxe ="Syntaxe: "+sys.argv[0]
    if(len(sys.argv) != 1):
        print(syntaxe)
        exit
    
    app = QApplication([])
    mw = Window()
    app.exec_()
    