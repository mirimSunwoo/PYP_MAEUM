import tkinter
from tkinter import *
import MAEUM_MAIN

class Start:
    def __init__(self, start):
        self.start = start

        # 화면 이미지
        self.startBack = tkinter.PhotoImage(file = "./image/background.png")
        self.startBackL = tkinter.Label(image=self.startBack)
        self.startBackL.place(x=-2, y=-2)

        # start 버튼

        self.ws = Tk()
        # ws.title('PythonGuides')
        # ws.geometry('300x200')
        self.dwnd = PhotoImage(file='image/btn_start.png')
        self.Button(ws, image=dwnd, command=None, borderwidth=0).pack(pady=10)

        self.ws.mainloop()
    def move(self):
        start_move = MAEUM_MAIN.Maeum_main.maeum_main(self.start)
        pass

    def play(self):
        self.start.mainloop()

if __name__ == '__main__':
    start = tkinter.Tk()
    start.title("마음을 나눠요")
    start.geometry("882x628")
    start.resizable(False, False)

    start = Start(start)
    start.play()
