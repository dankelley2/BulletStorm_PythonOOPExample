from tkinter import PhotoImage

class Sprite:
    def __init__(self,imgPath):
        self.img = PhotoImage(file=imgPath)
        self.img = self.img.subsample(4,4)