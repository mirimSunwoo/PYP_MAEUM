
import tkinter

class Thank_donate:
    def __init__(self, thank_donate):
        self.thank_donate = thank_donate

        # Thank_donate 화면 이미지
        self.Thank_donateBack = tkinter.PhotoImage(file="img/donate_basket.png")
        self.Thank_donateBackL = tkinter.Label(image=self.Thank_donateBack)
        self.Thank_donateBackL.place(x=-2, y=-2)