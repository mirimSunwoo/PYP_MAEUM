
import tkinter
import tkinter.font

import START
import MAEUM_MAIN

class Share:
    def __init__(self, share):
        self.share = share

        #share 화면 이미지
        self.shareBack = tkinter.PhotoImage(file="img/background.gif")
        self.shareBackL = tkinter.Label(image=self.shareBack)
        self.shareBackL.place(x=-2, y=-2)








