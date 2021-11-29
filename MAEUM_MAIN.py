
import tkinter

import SHARE
import DONATE
import TOP3
import LOGIN

class Maeum_main:
    def __init__(self, main):
        self.main = main

        # Maeum_main 화면 이미지
        self.Maeum_mainBack = tkinter.PhotoImage(file="img/background.gif")
        self.Maeum_mainBackL = tkinter.Label(image=self.Maeum_mainBack)
        self.Maeum_mainBackL.place(x=-2, y=-2)

        # share 버튼
        self.shareButton = tkinter.Button(self.main, width=437, height=133, borderwidth=0, command=self.ShareButton)
        self.shareButton.place(x=200, y=100)
        self.shareButtonImg = tkinter.PhotoImage(file="img/Group 103.png")
        self.shareButton.config(image=self.shareButtonImg)

        # donate 버튼
        self.donateButton = tkinter.Button(self.main, width=437, height=133, borderwidth=0, command=self.DonateButton)
        self.donateButton.place(x=200, y=270)
        self.donateButtonImg = tkinter.PhotoImage(file="img/Group 106.png")
        self.donateButton.config(image=self.donateButtonImg)

        # top3 버튼
        self.top3Button = tkinter.Button(self.main, width=437, height=133, borderwidth=0, command=self.Top3Button)
        self.top3Button.place(x=200, y=440)
        self.top3ButtonImg = tkinter.PhotoImage(file="img/Group 107.png")
        self.top3Button.config(image=self.top3ButtonImg)

        # 회원가입 버튼
        self.loginButton = tkinter.Button(self.main, width=81, height=81, borderwidth=0, command=self.LoginButton)
        self.loginButton.place(x=720, y=30)
        self.loginButtonImg = tkinter.PhotoImage(file="img/Group 102.png")
        self.loginButton.config(image=self.loginButtonImg)

    # SHARE 페이지로 넘기기
    def ShareButton(self):
        SHARE.Share(self.main)

    # DONATE 페이지로 넘기기
    def DonateButton(self):
        DONATE.Donate(self.main)

    # TOP3 페이지로 넘기기
    def Top3Button(self):
        TOP3.Top3(self.main)

    # LOGIN 페이지로 넘기기
    def LoginButton(self):
        LOGIN.Login(self.main)
