import tkinter
import tkinter.font

import START
import MAEUM_MAIN

class Donate:
    def __init__(self, donate):
        self.donate = donate

        # donate 화면 이미지
        self.donateBack = tkinter.PhotoImage(file="img/background.gif")
        self.donateBackL = tkinter.Label(img=self.donateBack)
        self.donateBackL.place(x=-2, y=-2)
