from tkinter import *
from subprocess import *
import os
from tkinter import messagebox
main=Tk()

def admin():
    Popen('kbp.py',shell=True)
    quit()
    
def normal():
    messagebox.showinfo("Welcome","Lets GO !!!")
    Popen('Registration.py',shell=True)
    quit()
main.title('Kaun Banega Physicist ')
main.attributes('-alpha',0.88)
main.geometry('1300x650')
main.resizable(height=False,width=False)
img=PhotoImage(file='bg2.png')
L=Label(main,image=img)
L1=Label(main,text='Welcome To Kaun Banega Phyicist By Physics Department',font=('Comic Sans MS',12,'bold'),bg="Black",fg="White")
b1=Button(main,text='Admin Page',command=admin,font=('Comic Sans MS',12,'bold'),bg="Black",fg="White")
b2=Button(main,text='Lets Go ',command=normal,font=('Comic Sans MS',12,'bold'),bg="Black",fg="White")
L.place(x=0,y=0)
L1.place(x=400,y=190)
b1.place(x=900,y=300)
b2.place(x=200,y=300)
main.mainloop()
