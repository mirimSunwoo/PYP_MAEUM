import tkinter

import MAEUM_MAIN
import THANK_DONATE


class Share:
    def __init__(self, share):
        self.share =share

        #화면 이미지
        self.shareBack = tkinter.PhotoImage(file = "img/share_back.png")
        self.shareBackL = tkinter.Label(image=self.shareBack)
        self.shareBackL.place(x=-2, y=-2)

        #share 버튼
        self.shareButton = tkinter.Button(self.share, width=210, height=60, borderwidth=0, command=self.T_D_Button)
        self.shareButton.place(x=570, y=500)
        self.shareButtonImg = tkinter.PhotoImage(file='img/share_btn.png')
        self.shareButton.config(image=self.shareButtonImg)

        # 입력
        self.ent1 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent1.place(x=350, y=200)

        self.ent2 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent2.place(x=350, y=280)

        self.ent3 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent3.place(x=350, y=360)

        self.ent4 = tkinter.Entry(share)  # TD라는 창에 입력창 생성
        self.ent4.place(x=350, y=440)

        # back 버튼
        self.backButton = tkinter.Button(self.share, width=120, height=67, borderwidth=0, command=self.BackButton)
        self.backButton.place(x=750, y=9)
        self.backButtonImg = tkinter.PhotoImage(file="img/back_yellow.PNG")
        self.backButton.config(image=self.backButtonImg)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.share)

    def BackButton(self):
        MAEUM_MAIN.Maeum_main(self.share)
