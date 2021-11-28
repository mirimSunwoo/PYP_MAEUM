import tkinter

import THANK_DONATE

class Necktie_donate:
    def __init__(self, necktie_donate):
        self.necktie_donate = necktie_donate

        # 화면 이미지
        self.Necktie_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Necktie_donateBackL = tkinter.Label(image=self.Necktie_donateBack)
        self.Necktie_donateBackL.place(x=-2, y=-2)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.Necktie_donate)