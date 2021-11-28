import tkinter

import MAEUM_MAIN
import subprocess
class Top3:
    def __init__(self):
        self.TD = TD
        #화면 이미지
        self.startBack = tkinter.PhotoImage(file = "img/top3_back.png")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)
        self.homeBtn = tkinter.PhotoImage(file='img/back_yellow.PNG')
        self.btn = tkinter.Button(TD, image=self.homeBtn, comand=None, borderwidth=0)
        self.btn.pack()
        self.btn.place(x=700, y=30)
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

    TD = Top3()
    TD.play()