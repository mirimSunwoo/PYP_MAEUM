
import tkinter

import START
import MAEUM_MAIN
import DONATE

import THANK_DONATE

class Cardigan_donate:
    def __init__(self, cardigan_donate):
        self.cardigan_donate = cardigan_donate

        # 화면 이미지
        self.Cardigan_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Cardigan_donateBackL = tkinter.Label(image=self.Cardigan_donateBack)
        self.Cardigan_donateBackL.place(x=-2, y=-2)

        # go_dona 버튼
        self.go_donaButton = tkinter.Button(self.cardigan_donate, width=366, height=70, borderwidth=0, command=self.T_D_Button)
        self.go_donaButton.place(x=250, y=150)
        self.go_donaButtonImg = tkinter.PhotoImage(file="img/go_dona.png")
        self.go_donaButton.config(image=self.go_donaButtonImg)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.cardigan_donate)