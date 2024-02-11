from tkinter import *
import random
# define the function
def generate():
    n=random.sample(range(10),6)
    B1.configure(text=n[0])
    B2.configure(text=n[1])
    B3.configure(text=n[2])
    B4.configure(text=n[3])
    B5.configure(text=n[4])
    B6.configure(text=n[5])
def reset():
    B1.configure(test="---")
    B2.configure(test="---")
    B3.configure(test="---")
    B4.configure(test="---")
    B5.configure(test="---")
    B6.configure(test="---")
w=Tk()
# design all componets
img=PhotoImage(file="D:/abc/download.png")
Limg=Label(w,image=img)
B1=Button(w,text="---",width=2,font=('arial',15,'bold'),relief='solid')
B2=Button(w,text="---",width=2,font=('arial',15,'bold'),relief='solid')
B3=Button(w,text="---",width=2,font=('arial',15,'bold'),relief='solid')
B4=Button(w,text="---",width=2,font=('arial',15,'bold'),relief='solid')
B5=Button(w,text="---",width=2,font=('arial',15,'bold'),relief='solid')
B6=Button(w,text="---",width=2,font=('arial',15,'bold'),relief='solid')
B7=Button(w,text="GET YOUR LUCKY NO",font=('arial',15,'bold'),relief='solid',command=generate)
B8=Button(w,text="RESET",width=5,font=('arial',15,'bold'),relief='solid',command=reset)
# place the componet at proper position
Limg.grid(row=1,column=1,rowspan=2)
B1.grid(row=1,column=2)
B2.grid(row=1,column=3)
B3.grid(row=1,column=4)
B4.grid(row=1,column=5)
B5.grid(row=1,column=6)
B6.grid(row=1,column=7)
B7.grid(row=2,column=2,columnspan=4)
B8.grid(row=2,column=6,columnspan=3)

w.mainloop()