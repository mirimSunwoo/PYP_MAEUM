import tkinter

import THANK_DONATE

class Vest_donate:
    def __init__(self, vest_donate):
        self.vest_donate = vest_donate

        # 화면 이미지
        self.Vest_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Vest_donateBackL = tkinter.Label(image=self.Vest_donateBack)
        self.Vest_donateBackL.place(x=-2, y=-2)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.Vest_donate)