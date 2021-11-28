import tkinter

import MAEUM_MAIN
import subprocess
class SHARE:
    def __init__(self):
        self.TD = TD
        #화면 이미지
        self.startBack = tkinter.PhotoImage(file = "img/share_back.png")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)
        self.homeBtn = tkinter.PhotoImage(file='img/back_yellow.PNG')
        self.btn = tkinter.Button(TD, image=self.homeBtn, comand=None, borderwidth=0)
        self.btn.pack()
        self.btn.place(x=700, y=20)

        self.Share = tkinter.PhotoImage(file='img/btn_share.png')
        self.Sbtn = tkinter.Button(TD, image=self.Share, comand=None, borderwidth=0)
        self.Sbtn.pack()
        self.Sbtn.place(x=570, y=500)

        self.ent1 = tkinter.Entry(TD)  # TD라는 창에 입력창 생성
        self.ent1.place(x=350,y=200)

        self.ent2 = tkinter.Entry(TD)  # TD라는 창에 입력창 생성
        self.ent2.place(x=350, y=280)

        self.ent3 = tkinter.Entry(TD)  # TD라는 창에 입력창 생성
        self.ent3.place(x=350, y=360)

        self.ent4 = tkinter.Entry(TD)  # TD라는 창에 입력창 생성
        self.ent4.place(x=350, y=440)



    def move(self):
        start_move = MAEUM_MAIN.Maeum_main(self.start)

    def play(self):
        self.TD.mainloop()

    def Button(self, TD, image, command):
        pass

if __name__ == '__main__':
    TD = tkinter.Tk()
    TD.title("Thank Share")
    TD.geometry("882x628+250+250")
    TD.resizable(False, False)

    TD = SHARE()
    TD.play()