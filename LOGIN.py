
import tkinter
import tkinter.font

import START
import MAEUM_MAIN

class Login:
    def __init__(self, login):
        self.login = login

        #share 화면 이미지
        self.loginBack = tkinter.PhotoImage(file="img/background.gif")
        self.loginBackL = tkinter.Label(img=self.loginBack)
        self.loginBackL.place(x=-2, y=-2)