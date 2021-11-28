import tkinter

import THANK_DONATE

class Pants_donate:
    def __init__(self, pants_donate):
        self.pants_donate = pants_donate

        # 화면 이미지
        self.Pants_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Pants_donateBackL = tkinter.Label(image=self.Pants_donateBack)
        self.Pants_donateBackL.place(x=-2, y=-2)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.Pants_donate)