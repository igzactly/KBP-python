from tkinter import *
import mysql.connector
from tkinter import messagebox
import time
import subprocess
conn1=mysql.connector.connect(user='root',password='sipl',database='kbp_questions')
curr1=conn1.cursor();
class kbp:
    def __init__(self):
        self.con=mysql.connector.connect(user='root',password='sipl',database='kbp_questions')
        self.con.autocommit=True
        self.log=Tk()
        self.BG=PhotoImage(file='bg2.png')
        self.L1=Label(self.log,image=self.BG)
        self.L1.place(x=0,y=0,relwidth=0.98,relheight=0.98)
        self.log.geometry('500x500')
        #self.main=Tk()
    def start(self):
        #self.log.pack()
        self.login()
    def execute(self,q):
        cursor=self.con.cursor()
        cursor.execute(q)
        cursor.close()
    def rexecute(self,q):
        cursor=self.con.cursor()
        cursor.execute(q)
        data=cursor.fetchall()
        cursor.close()
        return data
    def start(self):
        #self.log.pack()
        self.login()
    def login(self):
        Label(self.log,text="Welcome To KBP Admin Portal").place(relx=.5,rely=.45,anchor="center")
        self.p=Entry(self.log,show="*",font=("Symbol"))
        self.p.place(relx=.5, rely=.5, anchor="center")
        Button(self.log,text="Enter",command=self.varify,font=("Comic Sans MS",10,'bold'),background='black',fg='white').place(relx=.5, rely=.55, anchor="center")
    def varify(self):
        if self.p.get()!="Admin":
            self.log.destroy()
            self.home()
        else:
            messagebox.showinfo("ERROR!!!!!!!","Invalid password")
    def home(self):
        self.home_fr=Tk()
        self.home_fr.geometry('500x500')
        self.BG=PhotoImage(file='bg2.png')
        
        L1=Label(self.home_fr,image=self.BG)
        L1.place(x=0,y=0,relwidth=0.98,relheight=0.98)
        Button(self.home_fr,text="Edit Questions",font=("Comic Sans MS",10,'bold'),command=self.mid).place(x=100,y=20)
        #Button(self.home_fr,text="Add users",font=("Comic Sans MS",10,'bold'),background='black',fg='white').place(x=100,y=40)
        #Button(self.home_fr,text="Edit user",font=("Comic Sans MS",10,'bold'),background='black',fg='white').place(x=100,y=60)
        
        Button(self.home_fr,text="Show Score",font=("Comic Sans MS",10,'bold'),background='black',fg='white',command=self.show_score).place(x=100,y=80)

    def mid(self):
        self.home_fr.destroy()
        self.root=Tk()
        self.root.geometry('1200x750')
        self.root.resizable(height=False,width=False)
        self.a_fr=Frame(self.root,width=1200,height=750)
        self.a_fr.place(x=0,y=0)
        self.frame_info=Frame(self.a_fr,width=600,height=700)
        self.frame_info.place(x=10, y=60)
        self.fr_new=Frame(self.a_fr,width=650,height=700)
        self.fr_new.place(x=525,y=0)
        self.info()
        self.new()
    def onFrameConfigure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def info(self):
        Button(self.a_fr,text="Create New Question Set",font=20,command=self.set).place(x=10,y=20)
        self.canvas = Canvas(self.frame_info,width=475,height=700, borderwidth=0, background="#ffffff")
        self.frame = Frame(self.canvas, background="#ffffff")
        self.vsb = Scrollbar(self.frame_info, orient="vertical", command=self.canvas.yview)
        self.vsb.pack(side=RIGHT, fill=Y)
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.canvas.pack(side="left", fill="both")
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)
        z=self.rexecute("show tables")
        t=0
        for x in range(0,len(z)*11,11):
            s=0
            Label(self.frame,text="Set "+(z[t][0]).upper(),width=200,anchor='w').grid(row=x,column=1)
            td=self.rexecute("select * from "+z[t][0])
            Button(self.frame,text="Delete",command=lambda v=z[t][0]:self.delete_set(v)).grid(row=x,column=0)
            for y in range(x,x+len(td)):
                Button(self.frame,text=td[s][0],width=1).grid(row=y+1,column=0,sticky=NSEW)
                if len(td[s])==1:
                    Button(self.frame,text="        ",width=0,command= lambda g=td[s][0],h=z[t][0]:self.get(g,h),anchor='w').grid(row=y+1,column=1,sticky=NSEW)
                else:
                    Button(self.frame,text=td[s][1],width=0,command= lambda f=td[s][0],j=z[t][0]:self.get(f,j),anchor='w').grid(row=y+1,column=1,sticky=NSEW)
                s=s+1
            t=t+1
    def new(self):
        Label(self.fr_new,text="Question",font=(12)).place(x=10,y=20)
        self.qus=Text(self.fr_new,font=(20),width=65,height=7)
        self.qus.place(x=10,y=60)
        Label(self.fr_new,text="Option 1",font=(12)).place(x=10,y=210)
        self.op1=Text(self.fr_new,font=(20),width=65,height=3)
        self.op1.place(x=10,y=250)
        Label(self.fr_new,text="Option 2",font=(12)).place(x=10,y=325)
        self.op2=Text(self.fr_new,font=(20),width=65,height=3)
        self.op2.place(x=10,y=350)
        Label(self.fr_new,text="Option 3",font=(12)).place(x=10,y=425)
        self.op3=Text(self.fr_new,font=(20),width=65,height=3)
        self.op3.place(x=10,y=450)
        Label(self.fr_new,text="Option 4",font=(12)).place(x=10,y=525)
        self.op4=Text(self.fr_new,font=(20),width=65,height=3)
        self.op4.place(x=10,y=550)
        self.ans=Entry(self.fr_new,font=10,width=50)
        self.ans.place(x=75,y=625)
        self.score=Entry(self.fr_new,font=10,width=4)
        self.score.place(x=75,y=660)
        Label(self.fr_new,text="Answer",font=20).place(x=10,y=625)
        Label(self.fr_new,text="Score",font=20).place(x=10,y=660)
        

    def get(self,g,h):
        self.qus.config(bg='White')
        self.op1.config(bg='White')
        self.op2.config(bg='White')
        self.op3.config(bg='White')
        self.op4.config(bg='White')
        self.ans.config(bg='White')
        Button(self.fr_new,text="Delete",font=(12),command=lambda:self.q_delete(h,g)).place(x=300,y=660)
        Button(self.fr_new,text="Save",font=(12),command=lambda: self.save(h,g)).place(x=450,y=660)
        d=(self.rexecute("select * from "+h+" Where ID="+str(g)))[0]
        if len(self.qus.get('1.0',END))!=0:
            if d[1]!=None:
                self.qus.delete(1.0, END)
                self.qus.insert('1.0', d[1])
            else:
                self.qus.delete(1.0, END)
        if len(self.op1.get('1.0',END))!=0:
            if d[2]!=None:
                self.op1.delete(1.0, END)
                self.op1.insert('1.0', d[2])
            else:
                self.op1.delete(1.0, END)

        if len(self.op2.get('1.0',END))!=0:
            if d[3]!=None:
                self.op2.delete(1.0, END)
                self.op2.insert('1.0', d[3])
            else:
                self.op2.delete(1.0, END)


        if len(self.op3.get('1.0',END))!=0!=None:
            if d[4]!=None:
                self.op3.delete(1.0, END)
                self.op3.insert('1.0', d[4])
            else:
                self.op3.delete(1.0, END)
        if len(self.op4.get('1.0',END))!=0:
            if d[5]!=None:
                self.op4.delete(1.0, END)
                self.op4.insert('1.0', d[5])
            else:
                self.op4.delete('1.0', END)

        if len(self.ans.get())==0: 
            if d[6]!=None:
                c=str(d[6])
                self.ans.insert(END,c)
        else:
            if d[6]!=None:
                self.ans.delete(0,END)
                c=str(d[6])
                self.ans.insert(END,c)
            else:
                self.ans.delete(0,END)
        if len(self.score.get())==0: 
            if d[7]!=None:
                c=str(d[7])
                self.score.insert(END,c)
        else:
            if d[7]!=None:
                self.score.delete(0,END)
                c=str(d[7])
                self.score.insert(END,c)
            else:
                self.score.delete(0,END)
        

    def save(self,h,g):
        x=True
        if len(self.qus.get(1.0,END)[:-2])==0:
            self.qus.config(bg='Red')
            x=False
        if len(self.op1.get(1.0,END)[:-2])==0:
            self.op1.config(bg='Red')
            x=False
        if len(self.op2.get(1.0,END)[:-2])==0:
            self.op2.config(bg='Red')
            x=False
        if len(self.op3.get(1.0,END)[:-2])==0:
            self.op3.config(bg='Red')
            x=False
        if len(self.op4.get(1.0,END)[:-2])==0:
            self.op4.config(bg='Red')
            x=False
        if len(self.ans.get())==0:
            self.ans.config(bg='Red')
            x=False
        if len(self.score.get())==0:
            try:
                w=self.score.get()
                w=int(w)
            except:
                messagebox.showinfo("Error","Only numbers are allowed")
                self.score.config(bg='Red')
                x=False
        if x:
            self.execute("update "+h+" set Question='"+str((self.qus.get(1.0,END)[:-2]))+"',A='"+str((self.op1.get(1.0,END)[:-2]))+"',B='"+str((self.op2.get(1.0,END)[:-2]))+"',C='"+str((self.op3.get(1.0,END)[:-2]))+"',D='"+str((self.op4.get(1.0,END)[:-2]))+"',Correct='"+str(self.ans.get())+"',Score="+str(self.score.get())+" where ID="+str(g))
            self.fr_new.destroy()
            self.frame_info.destroy()
            self.fr_new=Frame(self.a_fr,width=650,height=700)
            self.fr_new.place(x=525,y=0)
            self.frame_info=Frame(self.a_fr,width=500,height=700)
            self.frame_info.place(x=10, y=60)
            self.info()
            self.new()
        else:

            messagebox.showinfo("Invalid","Empty box not allowed")
    def set(self):
        cursor=self.con.cursor(buffered=True)
        cursor.execute("show tables")
        data=cursor.fetchall()
        cursor.close()
        if len(data)!=0:
            c=chr(ord(data[(len(data)-1)][0])+1).upper()
        else:
            c='A'
        try:
            self.execute("create table "+c+"(sr_no int(2) primary key,question text(9999),op1 text(9999),op2 text(99999),op3 text(99999),op4 text(99999),ans int(1))")
            self.execute("create table "+c+"(ID int(2) primary key,Question text(9999),A text(9999),B text(99999),C text(99999),D text(99999),Correct text(99999),Score int)")
            for i in range(10):
                self.execute("insert into "+c+" values("+str(i+1)+",Null,Null,Null,Null,Null,Null,Null)")
        except:
            messagebox.showinfo("Error...","Database Error")
        else:
            self.frame_info.destroy()
            self.frame_info=Frame(self.a_fr,width=500,height=700)
            self.frame_info.place(x=10, y=60)
            self.info()
    def delete_set(self,s):
        r=Tk()
        Label(r,text="You want to delete the question set "+s+" entirely").grid(row=0, columnspan=4)
        Button(r,text="Confirm",command=lambda:self.sdelete(s,r)).grid(row=1,column=0)
        Button(r,text="Cancel",command=lambda:self.nothing(r)).grid(row=1,column=2)
    def sdelete(self,s,r):
        self.execute("drop table "+s)
        messagebox.showinfo("complete","Set is deleted")
        r.destroy()
        self.frame_info.destroy()
        self.frame_info=Frame(self.a_fr,width=500,height=700)
        self.frame_info.place(x=10, y=60)
        self.info()
    def nothing(self,r):
        r.destroy()
    def q_delete(self,t,sr):
        r=Tk()
        Label(r,text="You want to delete the question").grid(row=0, columnspan=4)
        Button(r,text="Confirm",command=lambda:self.qdelete(t,sr,r)).grid(row=1,column=0)
        Button(r,text="Cancel",command=lambda:self.nothing(r)).grid(row=1,column=2)
    def qdelete(self,t,sr,r):
        self.execute("update "+t+" set Question=Null,A=Null,B=Null,C=Null,D=Null,Correct=Null,Score=Null where ID="+str(sr))
        messagebox.showinfo("complete","Question is deleted")
        r.destroy()
        self.frame_info.destroy()
        self.frame_info=Frame(self.a_fr,width=500,height=700)
        self.frame_info.place(x=10, y=60)
        self.info()
    def show_score(self):
        self.home_fr.destroy()
        self.score_fr=Tk()
        self.score_fr.geometry('700x600')
        

        self.score()
        '''
self.sort_fr=Frame(self.score_fr,width=675,height=50)
        self.sort_fr.place(x=10,y=5)
        options = ["Increasing", "Decresing"]
        var = StringVar()
        #var.set("sort")
        drop1 = OptionMenu(self.user_fr,var,*options, command= lambda var,x=1:self.func(var,x))
        drop1.place(x=10, y=10)
        drop2 = OptionMenu(self.user_fr,var,*options, command= lambda var,x=2:self.func(var,x))
        drop2.place(x=10, y=10)
        '''
        
    def score(self):
        subprocess.Popen('ScoreBoard.py',shell=True)
        quit()

    def func(self,value,x):
        print(value)
        print(x)



k=kbp()
k.start()
k.log.mainloop()
