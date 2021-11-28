
import tkinter

import START
# import MAEUM_MAIN
# import DONATE

import THANK_DONATE

class Necktie_donate:
    def __init__(self, necktie_donate):
        self.necktie_donate = necktie_donate

        # 화면 이미지
        self.Necktie_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Necktie_donateBackL = tkinter.Label(image=self.Necktie_donateBack)
        self.Necktie_donateBackL.place(x=-2, y=-2)

        # go_dona 버튼
        self.go_donaButton = tkinter.Button(self.necktie_donate, width=366, height=70, borderwidth=0, command=self.T_D_Button)
        self.go_donaButton.place(x=250, y=150)
        self.go_donaButtonImg = tkinter.PhotoImage(file="img/go_dona.png")
        self.go_donaButton.config(image=self.go_donaButtonImg)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.necktie_donate)