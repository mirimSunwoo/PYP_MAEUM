import tkinter

import MAEUM_MAIN
import START

class Thank_share:
    def __init__(self, thank_share):
        self.thank_share = thank_share

        # Thank_donate 화면 이미지
        self.Thank_donateBack = tkinter.PhotoImage(file="img/share_basket.png")
        self.Thank_donateBackL = tkinter.Label(image=self.Thank_donateBack)
        self.Thank_donateBackL.place(x=-2, y=-2)

        # home 버튼
        self.homeButton = tkinter.Button(self.thank_share, width=72, height=72, borderwidth=0, command=self.HomeButton)
        self.homeButton.place(x=755, y=11)
        self.homeButtonImg = tkinter.PhotoImage(file="img/home_b.png")
        self.homeButton.config(image=self.homeButtonImg)


    # home 페이지로 가기
    def HomeButton(self):
        MAEUM_MAIN.Maeum_main(self.thank_share)

