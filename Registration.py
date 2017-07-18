from tkinter import *
from tkinter import messagebox
import mysql.connector
import subprocess
conn=mysql.connector.connect(host='localhost',database='kbp_users',user='root',password='sipl')
file=open('user.txt','w')
curr=conn.cursor()
curr.autocommit=True
main=Tk()
main.title("Get yourself registered !")
var1=StringVar()
var2=StringVar()
def Submit():
    a=var1.get()
    b=var2.get()
    data='insert into users value('+'"'+a+'"'+','+'"'+str(b)+'"'+','+'Null);'
    print(data)
    curr.execute('insert into users value('+'"'+a+'"'+','+'"'+str(b)+'"'+','+"Null"+')'+';')
    file.write(a)
    file.close()
    messagebox.showinfo('done','sucessfully registered ! welcome '+var1.get())
    subprocess.Popen('Gameplay.py',shell=True)
    conn.close()
    quit()
    
    
main.attributes('-alpha',0.88)
main.geometry('1100x650')
main.resizable(height=False,width=False)
BG=PhotoImage(file='bg2.png')
BL=Label(main,image=BG)
L1=Label(main,text='Welcome New User',font=('Comic Sans MS',20,'bold'),fg="White",bg="Black")
L2=Label(main,text='Enter Your Name ',font=("Comic Sans MS",10,'bold'),fg='white',background='black')
L3=Label(main,text='Enter Your Class',font=("Comic Sans MS",10,'bold'),fg='white',background='black')
E1=Entry(main,textvariable=var1)
E2=Entry(main,textvariable=var2)
B1=Button(main,command=Submit,text='submit',font=("Comic Sans MS",15,'bold'),fg='white',bg='black')
BL.place(x=0,y=0,relwidth=0.98,relheight=0.98)
L1.place(x=500,y=50)
L2.place(x=300,y=250)
E1.place(x=600,y=250)
L3.place(x=300,y=350)
E2.place(x=600,y=350)
B1.place(x=450,y=420)
main.mainloop()
