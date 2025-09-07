# from tkinter import *

# window=Tk()

# window.title("My First GUI Program")
# window.geometry("400x300")
# window.resizable(1,0)

# lb1=Label(window, text="This is a label")
# lb2=Label(window, text="문자를", font=("궁서체",20,"bold"))
# lb3=Label(window, text="출력하는", bg="yellow", fg="red", anchor="w")
# lb4=Label(window, text="라벨입니다", width="20",height="3",bg="blue", fg="white", anchor="se")
# lb1.pack()
# lb2.pack()
# lb3.pack()
# lb4.pack()

# window.mainloop()

# from tkinter import *

# window=Tk()

# window.title("My First GUI Program")
# window.geometry("400x300")
# window.resizable(1,0)

# lb1=Label(window, text="This is a btns")
# lb2=Button(window,text="1번")
# lb3=Button(window,text="2번")
# lb1.pack()
# lb2.pack(side=LEFT, padx=10)
# lb3.pack(side=RIGHT, padx=10)

# window.mainloop()

# from tkinter import *

# def print_1():
#     lb1["text"]="첫번째, 버튼이 눌렸습니다"
# def print_2():
#     lb1["text"]="두번째, 버튼이 눌렸습니다"

# window=Tk()

# lb1=Label(window, text="결과 출력 레이블")
# btn1=Button(window, text="One", command=print_1)
# btn2=Button(window, text="Two", command=print_2)
# lb1.pack()
# btn1.pack()
# btn2.pack()

# window.mainloop()

# from tkinter import *

# def add():
#     a = int(ent1.get())
#     b = int(ent2.get())
#     lb1["text"] = f"결과: {a + b}"

# window = Tk()

# # Entry 위젯 정의
# ent1 = Entry(window)
# ent2 = Entry(window)

# # 레이블과 버튼 정의
# lb1 = Label(window, text="결과 출력 레이블")
# btn1 = Button(window, text="출력", command=add)  # 함수 참조만 넘겨야 하므로 괄호 X

# # 위젯 배치
# ent1.pack()
# ent2.pack()
# lb1.pack()
# btn1.pack()

# window.mainloop()

from tkinter import *

root=Tk()

top_btn=Button(root,text="Top")
top_btn.pack(side="top", fill=X)

bottom_btn=Button(root,text="Bottom")
bottom_btn.pack(side="bottom", fill=X)

left_btn=Button(root,text="Left")
left_btn.pack(side="left", fill=Y)

right_btn=Button(root,text="Right")
right_btn.pack(side="right", fill=Y)

center_label=Label(root,text="Center Area", bg="lightblue")
center_label.pack(expand=True, fill=BOTH)

root.mainloop()