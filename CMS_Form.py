from tkinter import *
from tkinter import ttk,messagebox
import pymysql
import time

class CMS:
    def __init__(self,root):

        self.root=root
        self.root.title("Aseem Enterprises - Dashboard")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

#================ TITLE =================

        title=Label(self.root,text="Aseem Enterprises Management System",
                    font=("times new roman",30,"bold"),
                    bg="#033054",fg="white")
        title.place(x=0,y=0,relwidth=1,height=70)

#================ CLOCK =================

        self.lbl_clock=Label(self.root,text="Welcome",
                             font=("times new roman",15),
                             bg="#4d636d",fg="white")

        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        self.update_clock()

#================ MENU =================

        menu_frame=Frame(self.root,bg="#262626")
        menu_frame.place(x=0,y=100,width=200,height=600)

        btn1=Button(menu_frame,text="User Details",
                    font=("times new roman",15,"bold"),
                    bg="#262626",fg="white",
                    cursor="hand2",
                    command=self.show_users)

        btn1.place(x=10,y=50,width=180,height=40)

        btn2=Button(menu_frame,text="Reports",
                    font=("times new roman",15,"bold"),
                    bg="#262626",fg="white",
                    cursor="hand2",
                    command=self.show_reports)

        btn2.place(x=10,y=120,width=180,height=40)

        btn3=Button(menu_frame,text="Settings",
                    font=("times new roman",15,"bold"),
                    bg="#262626",fg="white",
                    cursor="hand2",
                    command=self.show_settings)

        btn3.place(x=10,y=190,width=180,height=40)

        btn4=Button(menu_frame,text="Logout",
                    font=("times new roman",15,"bold"),
                    bg="red",fg="white",
                    cursor="hand2",
                    command=self.logout)

        btn4.place(x=10,y=260,width=180,height=40)

#=============== CONTENT AREA =================

        self.frame=Frame(self.root,bg="white")
        self.frame.place(x=200,y=100,width=1150,height=600)

        Label(self.frame,text="Welcome To Aseem Enterprises",
              font=("times new roman",35,"bold"),
              bg="white",fg="#033054").pack(pady=50)

#=============== FUNCTIONS =================

    def update_clock(self):

        time_=time.strftime("%I:%M:%S %p")
        date_=time.strftime("%d-%m-%Y")

        self.lbl_clock.config(text=f"Welcome to Aseem Enterprises   Date: {date_}   Time: {time_}")

        self.lbl_clock.after(1000,self.update_clock)

#=============== USER DETAILS =================

    def show_users(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        title=Label(self.frame,text="Registered Users",
        font=("times new roman",25,"bold"),bg="white")
        title.pack(pady=20)

        table=ttk.Treeview(self.frame,
                           columns=("fname","lname","email","contact"),
                           show="headings")

        table.heading("fname",text="First Name")
        table.heading("lname",text="Last Name")
        table.heading("email",text="Email")
        table.heading("contact",text="Contact")

        table.pack(fill=BOTH,expand=1)

        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="kryptoradb")
            cur=con.cursor()

            cur.execute("select f_name,l_name,email,contact from std_info")
            rows=cur.fetchall()

            for r in rows:
                table.insert("",END,values=r)

            con.close()

        except:
            messagebox.showerror("Error","Database connection error")

#=============== REPORTS =================

    def show_reports(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        try:
            con=pymysql.connect(host="localhost",user="root",password="",database="kryptoradb")
            cur=con.cursor()

            cur.execute("select count(*) from std_info")
            total=cur.fetchone()[0]

            Label(self.frame,text="System Reports",
            font=("times new roman",25,"bold"),
            bg="white").pack(pady=20)

            Label(self.frame,text=f"Total Registered Users : {total}",
            font=("times new roman",20),
            bg="white").pack(pady=20)

            con.close()

        except:
            messagebox.showerror("Error","Database error")

#=============== SETTINGS =================

    def show_settings(self):

        for widget in self.frame.winfo_children():
            widget.destroy()

        Label(self.frame,text="System Settings",
        font=("times new roman",25,"bold"),
        bg="white").pack(pady=20)

        Label(self.frame,text="Settings Panel (Coming Soon)",
        font=("times new roman",18),
        bg="white").pack(pady=20)

#=============== LOGOUT =================

    def logout(self):

        self.root.destroy()
        import LoginForm

#=============== RUN APP =================

root=Tk()
obj=CMS(root)
root.mainloop()
