import tkinter

import THANK_DONATE

class Shirts_donate:
    def __init__(self, shirts_donate):
        self.shirts_donate = shirts_donate

        # 화면 이미지
        self.Shirts_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Shirts_donateBackL = tkinter.Label(image=self.Shirts_donateBack)
        self.Shirts_donateBackL.place(x=-2, y=-2)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.Shirts_donate)