import tkinter
import tkinter.font

class Donate:
    def __init__(self, donate):
        self.donate = donate

        # donate 화면 이미지
        self.donateBack = tkinter.PhotoImage(file="img/background.gif")
        self.donateBackL = tkinter.Label(img=self.shareBack)
        self.donateBackL.place(x=-2, y=-2)
