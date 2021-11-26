import tkinter
import tkinter.font

import SHARE
import DONATE
import TOP3


class Maeum_main:
    def __init__(self, main):
        self.main = main

        #Maeum_main 화면 이미지
        self.Maeum_mainBack = tkinter.PhotoImage(file = "img/background.gif")
        self.Maeum_mainBackL = tkinter.Label(image=self.Maeum_mainBack)
        self.Maeum_mainBackL.place(x=-2, y=-2)

        #share 버튼
        self.shareButton = tkinter.Button(self.main, width=350, height=50, borderwidth=0, command=self.ShareButton)
        self.shareButton.place(x=15, y=390)
        self.shareButtonImg = tkinter.PhotoImage(file="img/share.PNG")
        self.shareButton.config(image=self.shareButtonImg)


        #self.shareButton = tkinter.PhotoImage(file="img/share.png")
        #self.shareButton = tkinter.Button(self.main, command=self.ShareButton)
        #self.shareButton.place(x=360, y=60)

        #donate 버튼
        #self.donateButton = tkinter.PhotoImage(file="img/donate.png")
        #self.donateButton = tkinter.Button(self.main, command=self.DonateButton)
        #self.donateButton.place(x=360, y=230)

        #top3 버튼
        #self.top3Button = tkinter.PhotoImage(file="img/top3.png")
        #self.top3Button = tkinter.Button(self.main, command=self.Top3Button)
        #self.top3Button.place(x=360, y=400)

        #회원가입 버튼
        #self.loginButton = tkinter.PhotoImage(file="")
        #self.loginButton = tkinter.Button(self.main, command=self.LoginButton)
        #self.loginButton.place(x=500, y=30)

    # SHARE 페이지로 넘기기
    def ShareButton(self):
        mainShareButton = SHARE.Share(self.main)

    # DONATE 페이지로 넘기기
    def DonateButton(self):
        mainDonateButton = DONATE.Donate(self.main)



    # TOP3 페이지로 넘기기
    def Top3Button(self):
        mainTop3Button = TOP3.Top3(self.main)


