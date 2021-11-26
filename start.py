import tkinter
import os
print (os.path.dirname(os.path.realpath(__file__)) ) #프로젝트 소스코드 파일 경로 출력

root=tkinter.Tk()
root.title("blog")
root.geometry("1440x800")
root.resizable(0, 0)
image=tkinter.PhotoImage(file="./image/Group 20.png") #PhotoImage를 통한 이미지 지정
label=tkinter.Label(root, image=image) #라벨 생성, 라벨에는 앞서 선언한 이미지가 들어감.
label.pack()

root.mainloop()