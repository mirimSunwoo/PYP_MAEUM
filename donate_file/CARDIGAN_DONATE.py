import tkinter

import THANK_DONATE

class Cardigan_donate:
    def __init__(self, cardigan_donate):
        self.cardigan_donate = cardigan_donate

        # 화면 이미지
        self.Cardigan_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Cardigan_donateBackL = tkinter.Label(image=self.Cardigan_donateBack)
        self.Cardigan_donateBackL.place(x=-2, y=-2)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.cardigan_donate) #선우 여기 있니