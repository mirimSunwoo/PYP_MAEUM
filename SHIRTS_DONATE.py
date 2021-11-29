import tkinter
from tkinter import *  # tkinter 라이브러리에 모든 함수를 사용하겠다.
from tkinter import ttk

import START
import MAEUM_MAIN
import DONATE

import THANK_DONATE

class Shirts_donate:
    def __init__(self, shirts_donate):
        self.shirts_donate = shirts_donate

        # 화면 이미지
        self.Shirts_donateBack = tkinter.PhotoImage(file="img/donate_back.png")
        self.Shirts_donateBackL = tkinter.Label(image=self.Shirts_donateBack)
        self.Shirts_donateBackL.place(x=-2, y=-2)

        # shirtsEx 이미지
        self.shirtsEx = tkinter.Button(self.shirts_donate, width=210, height=205, borderwidth=0)
        self.shirtsEx.place(x=150, y=200)
        self.shirtsExImg = tkinter.PhotoImage(file="img/shirts.png")
        self.shirtsEx.config(image=self.shirtsExImg)

        # 레이블 박스
        school = ["미림마이스터고", "선린인터넷고", "디지털미디어고"]  # 콤보 박스에 나타낼 항목 리스트
        combobox = ttk.Combobox(shirts_donate)  # root라는 창에 콤보박스 생성
        combobox.config(height=100)  # 높이 설정
        combobox.config(values=school)  # 나타낼 항목 리스트(a) 설정
        combobox.config(state="readonly")  # 콤보 박스에 사용자가 직접 입력 불가
        combobox.set("학교 선택")  # 맨 처음 나타낼 값 설정
        combobox.place(x=500, y=150)  # 콤보 박스 배치

        # 레이블 선택되었음
        def school_check():
            school = []
            school.append(combobox.get())
            school.append("선택")
            school_lb.config(text=school)
            school_lb.place(x=500, y=175)

        # 레이블 박스 버튼
        btn = Button(shirts_donate)  # root라는 창에 버튼 생성
        btn.config(text="선택")  # 버튼 내용
        btn.config(width=10)  # 버튼 크기
        btn.config(command=school_check)  # 버튼 기능 (btnpree() 함수 호출)
        btn.place(x=670, y=148)  # 버튼 배치

        # 레이블 선택되었음 대기
        school_lb = Label(shirts_donate)  # root라는 창에 레이블 생성
        school_lb.place(x=670, y=148)  # 레이블 배치

        # size 라디오
        size_lang_var = StringVar()  # str 형으로 변수 저장
        btn_size1 = Radiobutton(shirts_donate, text="S ", value="S", variable=size_lang_var)
        btn_size1.select()  # 기본값 선택
        btn_size2 = Radiobutton(shirts_donate, text="M", value="M", variable=size_lang_var)
        btn_size3 = Radiobutton(shirts_donate, text="L ", value="L", variable=size_lang_var)

        btn_size1.place(x=500, y=210)  # 라디오 버튼 배치
        btn_size2.place(x=500, y=240)
        btn_size3.place(x=500, y=270)

        # size 선택되었음
        def size_check():
            size = []
            size.append(size_lang_var.get())
            size.append("선택")
            size_lb.config(text=size)
            size_lb.place(x=570, y=255)

        # size 버튼
        size_btn = Button(shirts_donate)  # root라는 창에 버튼 생성
        size_btn.config(text="선택")  # 버튼 내용
        size_btn.config(width=10)  # 버튼 크기
        size_btn.config(command=size_check)  # 버튼 기능 (btnpree() 함수 호출)
        size_btn.place(x=570, y=225)  # 버튼 배치

        # size 선택되었음 대기
        size_lb = Label(shirts_donate)  # root라는 창에 레이블 생성
        size_lb.place(x=570, y=225)  # 레이블 배치

        # gender 라디오
        gender_lang_var = StringVar()  # str 형으로 변수 저장
        btn_gender1 = Radiobutton(shirts_donate, text="남", value="남", variable=gender_lang_var)
        btn_gender1.select()  # 기본값 선택
        btn_gender2 = Radiobutton(shirts_donate, text="여", value="여", variable=gender_lang_var)

        btn_gender1.place(x=500, y=315)  # 라디오 버튼 배치
        btn_gender2.place(x=500, y=345)

        # gender 선택되었음
        def gender_check():
            gender = []
            gender.append(gender_lang_var.get())
            gender.append("선택")
            gender_lb.config(text=gender)
            gender_lb.place(x=570, y=345)

        # gender 버튼
        gender_btn = Button(shirts_donate)  # root라는 창에 버튼 생성
        gender_btn.config(text="선택")  # 버튼 내용
        gender_btn.config(width=10)  # 버튼 크기
        gender_btn.config(command=gender_check)  # 버튼 기능 (btnpree() 함수 호출)
        gender_btn.place(x=570, y=315)  # 버튼 배치

        # gender 선택되었음 대기
        gender_lb = Label(shirts_donate)  # root라는 창에 레이블 생성
        gender_lb.place(x=570, y=320)  # 레이블 배치

        # defect 라디오
        defect_lang_var = StringVar()  # str 형으로 변수 저장
        btn_defect1 = Radiobutton(shirts_donate, text="1 ", value="약", variable=defect_lang_var)
        btn_defect1.select()  # 기본값 선택
        btn_defect2 = Radiobutton(shirts_donate, text="3 ", value="중", variable=defect_lang_var)
        btn_defect3 = Radiobutton(shirts_donate, text="5 ", value="강", variable=defect_lang_var)

        btn_defect1.place(x=500, y=390)  # 라디오 버튼 배치
        btn_defect2.place(x=500, y=420)
        btn_defect3.place(x=500, y=450)

        # defect 선택되었음
        def defect_check():
            defect = []
            defect.append(defect_lang_var.get())
            defect.append("선택")
            defect_lb.config(text=defect)
            defect_lb.place(x=570, y=435)

        # defect 버튼
        defect_btn = Button(shirts_donate)  # root라는 창에 버튼 생성
        defect_btn.config(text="선택")  # 버튼 내용
        defect_btn.config(width=10)  # 버튼 크기
        defect_btn.config(command=defect_check)  # 버튼 기능 (btnpree() 함수 호출)
        defect_btn.place(x=570, y=405)  # 버튼 배치

        # defect 선택되었음 대기
        defect_lb = Label(shirts_donate)  # root라는 창에 레이블 생성
        defect_lb.place(x=570, y=405)  # 레이블 배치

        # go_dona 버튼
        self.go_donaButton = tkinter.Button(self.shirts_donate, width=268, height=68, borderwidth=0, command=self.T_D_Button)
        self.go_donaButton.place(x=500, y=500)
        self.go_donaButtonImg = tkinter.PhotoImage(file="img/go_dona.png")
        self.go_donaButton.config(image=self.go_donaButtonImg)

        # back 버튼
        self.backButton = tkinter.Button(self.shirts_donate, width=130, height=75, borderwidth=0, command=self.BackButton)
        self.backButton.place(x=750, y=9)
        self.backButtonImg = tkinter.PhotoImage(file="img/back_blue.PNG")
        self.backButton.config(image=self.backButtonImg)

    def T_D_Button(self):
        THANK_DONATE.Thank_donate(self.shirts_donate)

    def BackButton(self):
        DONATE.Donate(self.shirts_donate)