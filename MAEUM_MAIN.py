import tkinter

import SHARE
import DONATE
import TOP3
import LOGIN

class Maeum_main:
    def __init__(self, main):
        self.main = main

        #Maeum_main 화면 이미지
        self.Maeum_mainBack = tkinter.PhotoImage(file = "img/background.gif")
        self.Maeum_mainBackL = tkinter.Label(image=self.Maeum_mainBack)
        self.Maeum_mainBackL.place(x=-2, y=-2)

        #share 버튼
        self.shareButton = tkinter.Button(self.main, width=366, height=70,
                                          borderwidth=0, command=self.ShareButton)
        self.shareButton.place(x=250, y=150)
        self.shareButtonImg = tkinter.PhotoImage(file="img/share.PNG")
        self.shareButton.config(image=self.shareButtonImg)

        #donate 버튼
        self.donateButton = tkinter.Button(self.main, width=366, height=70, borderwidth=0, command=self.DonateButton)
        self.donateButton.place(x=250, y=298)
        self.donateButtonImg = tkinter.PhotoImage(file="img/donate.png")
        self.donateButton.config(image=self.donateButtonImg)

        #top3 버튼
        self.top3Button = tkinter.Button(self.main, width=366, height=70, borderwidth=0, command=self.Top3Button)
        self.top3Button.place(x=250, y=450)
        self.top3ButtonImg = tkinter.PhotoImage(file="img/top3.png")
        self.top3Button.config(image=self.top3ButtonImg)

        #회원가입 버튼
        self.loginButton = tkinter.Button(self.main, width=366, height=70, borderwidth=0, command=self.LoginButton)
        self.loginButton.place(x=250, y=450)
        self.loginButtonImg = tkinter.PhotoImage(file="img/login.png")
        self.loginButton.config(image=self.top3ButtonImg)

    # SHARE 페이지로 넘기기
    def ShareButton(self):
        mainShareButton = SHARE.Share(self.main)

    # DONATE 페이지로 넘기기
    def DonateButton(self):
       mainDonateButton = DONATE.Donate(self.main)

    # TOP3 페이지로 넘기기
    def Top3Button(self):
       mainTop3Button = TOP3.Top3(self.main)

    # LOGIN 페이지로 넘기기
    def LoginButton(self):
       mainLoginButton = LOGIN.Login(self.main)


