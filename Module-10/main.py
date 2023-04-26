""" 
My camera application

author:-- Antar Chandra Nath
 """

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2

class window(QWidget):
    """ Main app window """
    def __init__(self):
        super().__init__()

        # variable for app window
        self.window_width = 640
        self.window_height = 400

        # image variable
        self.img_width = 640
        self.img_height = 400

        # setup the window
        self.setWindowTitle("My Camera App")
        self.setGeometry(0, 0, self.window_width, self.window_height)
        self.setFixedSize(self.window_width, self.window_height)
        
        self.ui()
    
    def ui(self):
        """ contains all ui thing"""
        # image label
        self.image_lebel = QLabel(self)
        self.image_lebel.setGeometry(0, 0, self.img_width, self.img_height)

        self.show()

    def update(self):
        """ update frames """

    def save_imag(self):
        """ save image from camera """
        pass
    
    def record(self):
        """ record video """
        pass

# run
app = QApplication(sys.argv)
win = window() 
sys.exit(app.exec_())