from tkinter import *

root = Tk()
root.title('사진불러오기')
root.geometry('800x600')

img = ImageTk.PhotoImage(Image.open('./002.png'))
label = Label(image=img)
label.pack()

quit = Button(root, text='종료하기', command=root.quit)
quit.pack()

root.mainloop()


