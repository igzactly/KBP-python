from tkinter import *
import mysql.connector
from tkinter import messagebox
import os
scoreboard=Tk()
scoreboard.geometry('1300x650')
scoreboard.attributes('-alpha',0.88)
scoreboard.resizable(height=False,width=False)
bg=PhotoImage(file='bg2.png')
Bg=Label(scoreboard,image=bg).place(x=0,y=0)

#scoreboard.geometry("1000x600")
conn=mysql.connector.connect(host='localhost',database='kbp_users',user='root',password='sipl')
curr=conn.cursor()

def donothing():
    messagebox.showinfo('hello','Heres the score')

def get_rank(n):
    if n==1:
        curr.execute('select * from users order by score;')
        a=curr.fetchall()
        b=a[2]
        r1nm = Label(scoreboard, text=b[0],font=("Comic Sans MS",20),bg="green",fg="white").place(x=150, y=150)
        r1cls = Label(scoreboard, text=b[1],font=("Comic Sans MS",20),bg="green",fg="white").place(x=350, y=150)
        r1cls = Label(scoreboard, text=b[2],font=("Comic Sans MS",20),bg="green",fg="white").place(x=450, y=150)
    elif n==2:
        curr.execute('select * from users order by score;')
        a=curr.fetchall()
        b=a[1]
        r1nm = Label(scoreboard, text=b[0],font=("Comic Sans MS",20),bg="orange",fg="white").place(x=150, y=210)
        r1cls = Label(scoreboard, text=b[1],font=("Comic Sans MS",20),bg="orange",fg="white").place(x=350, y=210)
        r1cls = Label(scoreboard, text=b[2],font=("Comic Sans MS",20),bg="orange",fg="white").place(x=450, y=210)
    elif n==3:
        curr.execute('select * from users order by score;')
        a = curr.fetchall()
        print(a)
        b = a[0]
        r1nm = Label(scoreboard, text=b[0],font=("Comic Sans MS",20),bg="yellow").place(x=150, y=270)
        r1cls = Label(scoreboard, text=b[1],font=("Comic Sans MS",20),bg="yellow").place(x=350, y=270)
        r1cls = Label(scoreboard, text=b[2],font=("Comic Sans MS",20),bg="yellow").place(x=450, y=270)






scoreboard.title('ScoreBoard')

l2=Label(scoreboard,text='Name',font=("Comic Sans MS",20),bg="black",fg="white").place(x=150,y=50)
l3=Label(scoreboard,text='Class',font=("Comic Sans MS",20),bg="black",fg="white").place(x=350,y=50)
l4=Label(scoreboard,text='Score',font=("Comic Sans MS",20),bg="black",fg="white").place(x=450,y=50)
l5=Label(scoreboard,text='Rank',font=("Comic Sans MS",20),bg="black",fg="white").place(x=10,y=90)
l6=Label(scoreboard,text='First',font=("Comic Sans MS",20),bg="green",fg="white").place(x=10,y=150)
l7=Label(scoreboard,text='Second',font=("Comic Sans MS",20),bg="orange",fg="white").place(x=10,y=210)
l8=Label(scoreboard,text='Third',font=("Comic Sans MS",20),bg="yellow").place(x=10,y=270)
get_rank(1)
get_rank(2)
get_rank(3)




scoreboard.mainloop()
