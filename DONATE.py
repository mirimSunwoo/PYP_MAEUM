import tkinter
import tkinter.font

import START
import MAEUM_MAIN

import JACKET_DONATE
import CARDIGAN_DONATE
import PANTS_DONATE
import SHIRTS_DONATE
import VEST_DONATE
import NECKTIE_DONATE


class Donate:
    def __init__(self, donate):
        self.donate = donate

        # 화면 이미지
        self.startBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        # jacket 버튼
        self.jacketButton = tkinter.Button(self.donate, width=210, height=205, borderwidth=0, command=self.JacketButton)
        self.jacketButton.place(x=100, y=140)
        self.jacketButtonImg = tkinter.PhotoImage(file="img/jacket.png")
        self.jacketButton.config(image=self.jacketButtonImg)

        # cardigan 버튼
        self.cardiganButton = tkinter.Button(self.donate, width=210, height=205, borderwidth=0, command=self.CardiganButton)
        self.cardiganButton.place(x=330, y=140)
        self.cardiganButtonImg = tkinter.PhotoImage(file="img/cardigan.png")
        self.cardiganButton.config(image=self.cardiganButtonImg)

        # pants 버튼
        self.pantsButton = tkinter.Button(self.donate, width=210, height=205, borderwidth=0, command=self.PantsButton)
        self.pantsButton.place(x=560, y=140)
        self.pantsButtonImg = tkinter.PhotoImage(file="img/pants.png")
        self.pantsButton.config(image=self.pantsButtonImg)

        # shirts 버튼
        self.shirtsButton = tkinter.Button(self.donate, width=210, height=205, borderwidth=0, command=self.ShirtsButton)
        self.shirtsButton.place(x=100, y=375)
        self.shirtsButtonImg = tkinter.PhotoImage(file="img/shirts.png")
        self.shirtsButton.config(image=self.shirtsButtonImg)

        # vest 버튼
        self.vestButton = tkinter.Button(self.donate, width=210, height=205, borderwidth=0, command=self.VestButton)
        self.vestButton.place(x=330, y=375)
        self.vestButtonImg = tkinter.PhotoImage(file="img/vest.png")
        self.vestButton.config(image=self.vestButtonImg)

        # necktie 버튼
        self.necktieButton = tkinter.Button(self.donate, width=210, height=205, borderwidth=0, command=self.NecktieButton)
        self.necktieButton.place(x=560, y=375)
        self.necktieButtonImg = tkinter.PhotoImage(file="img/necktie.png")
        self.necktieButton.config(image=self.necktieButtonImg)

    def JacketButton(self):
        JACKET_DONATE.Jacket_donate(self.donate)

    def CardiganButton(self):
        CARDIGAN_DONATE.Cardigan_donate(self.donate)

    def PantsButton(self):
        PANTS_DONATE.Pants_donate(self.donate)

    def ShirtsButton(self):
        SHIRTS_DONATE.Shirts_donate(self.donate)

    def VestButton(self):
        VEST_DONATE.Vest_donate(self.donate)

    def NecktieButton(self):
        NECKTIE_DONATE.Necktie_donate(self.donate)
