from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #ชื่อโปรแกรม
GUI.geometry('500x400') #ขนาดโปรแกรม


L1 = Label(GUI,text='ประวัติบันทึกยอดสั่งซื้อลูกค้า',font=('Angsana New',30),fg='green')
L1.place(x=60,y=20)
####################
def Button2():
    text = 'ตอนนี้มีลูกค้าอยู่ 5 คน'
    messagebox.showinfo('มีลูกค้าอยู่กี่คน',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)
    
FB1 = LabelFrame(GUI) #คล้ายกระดาน
FB1.place(x=0,y=100)
B2 = ttk.Button(FB1,text='มีลูกค้าอยู่กี่คน',command=Button2)
B2.pack(ipadx=20,ipady=20) 
####################
def Button3():
    text = 'Xs S L XXL มากที่สุด'
    messagebox.showinfo('ลูกค้าซื้อไซต์ไหนมากที่่สุด',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)
FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=0,y=180)
B3 = ttk.Button(FB2,text='ลูกค้าซื้อไซต์ไหนมากที่สุด',command=Button3)
B3.pack(ipadx=20,ipady=20)
#######################
def Button4():
    text = 'XXL Super Vip'
    messagebox.showinfo('ลูกค้าไซต์ไหนซื้อบ่อยมากที่สุด',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)
FB3 = Frame(GUI) #คล้ายกระดาน
FB3.place(x=0,y=260)
B4 = ttk.Button(FB3,text='ลูกค้าไซต์ไหนซื้อบ่อยมากที่สุด',command=Button4)
B4.pack(ipadx=20,ipady=20)
#######################
def Button5():
    text = 'มีจำนวน 2 ราย'
    messagebox.showinfo('ลูกค้าที่โดนยึดมัดจำ',text)
    #messagebox.showwarning('เงินในบัญชี',text)
    #messagebox.showerror('เงินในบัญชี',text)
FB4 = Frame(GUI) #คล้ายกระดาน
FB4.place(x=0,y=350)
B5 = ttk.Button(FB4,text='ลูกค้าที่โดนยึดมัดจำ',command=Button5)
B5.pack(ipadx=20,ipady=20)
GUI.mainloop()
