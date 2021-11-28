import tkinter

import THANK_DONATE

class Jacket_donate:
    def __init__(self, jacket_donate):
        self.jacket_donate = jacket_donate

        # 화면 이미지
        self.Jacket_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Jacket_donateBackL = tkinter.Label(image=self.Jacket_donateBack)
        self.Jacket_donateBackL.place(x=-2, y=-2)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.jacket_donate)