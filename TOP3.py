import tkinter

import MAEUM_MAIN

class Top3:
    def __init__(self, top3):
        self.top3 = top3

        #화면 이미지
        self.top3Back = tkinter.PhotoImage(file = "img/top3_back.png")
        self.top3BackL = tkinter.Label(image=self.top3Back)
        self.top3BackL.place(x=-2, y=-2)

        #back 버튼
        self.backButton = tkinter.Button(self.top3, width=120, height=67, borderwidth=0, command=self.BackButton)
        self.backButton.place(x=750, y=27)
        self.backButtonImg = tkinter.PhotoImage(file="img/back_yellow.PNG")
        self.backButton.config(image=self.backButtonImg)

    def BackButton(self):
        MAEUM_MAIN.Maeum_main(self.top3)