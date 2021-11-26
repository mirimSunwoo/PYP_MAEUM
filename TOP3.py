import tkinter
import tkinter.font

import START
import MAEUM_MAIN

class Top3:
    def __init__(self, top3):
        self.top3 = top3

        # share 화면 이미지
        self.top3Back = tkinter.PhotoImage(file="img/background.gif")
        self.top3BackL = tkinter.Label(img=self.top3Back)
        self.top3BackL.place(x=-2, y=-2)