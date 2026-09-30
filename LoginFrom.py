from tkinter import *
from tkinter import messagebox
import database
import pymysql

def create_database():

    con = pymysql.connect(
        host="localhost",
        user="root",
        password=""
    )

    cur = con.cursor()

    # database create
    cur.execute("CREATE DATABASE IF NOT EXISTS kryptoradb")

    # database select
    cur.execute("USE kryptoradb")

    # table create
    cur.execute("""
        CREATE TABLE IF NOT EXISTS std_info(
        id INT AUTO_INCREMENT PRIMARY KEY,
        f_name VARCHAR(50),
        l_name VARCHAR(50),
        contact VARCHAR(20),
        email VARCHAR(50),
        password VARCHAR(50)
        )
    """)

    con.commit()
    con.close()

create_database()

class Login_Window:
    def __init__(self,root):

        self.root=root
        self.root.title("Login - Aseem Enterprises")
        self.root.geometry("900x500+200+100")
        self.root.config(bg="#021e2f")

#================ TITLE =================

        title=Label(self.root,text="Aseem Enterprises",
                    font=("Arial",30,"bold"),
                    bg="#021e2f",fg="white")
        title.pack(pady=30)

#================ LOGIN FRAME =================

        frame=Frame(self.root,bg="white")
        frame.place(x=250,y=150,width=400,height=250)

        Label(frame,text="Email",
              font=("Arial",15),bg="white").place(x=50,y=40)

        self.txt_email=Entry(frame,font=("Arial",12))
        self.txt_email.place(x=50,y=70,width=300)

        Label(frame,text="Password",
              font=("Arial",15),bg="white").place(x=50,y=110)

        self.txt_pass=Entry(frame,font=("Arial",12),show="*")
        self.txt_pass.place(x=50,y=140,width=300)

        Button(frame,text="LOGIN",
               command=self.login,
               bg="#033054",fg="white",
               font=("Arial",13)).place(x=50,y=190,width=120)

        Button(frame,text="REGISTER",
               command=self.register_window,
               bg="green",fg="white",
               font=("Arial",13)).place(x=230,y=190,width=120)

#================ FUNCTIONS =================

    def register_window(self):
        self.root.destroy()
        import Register

    def login(self):

        if self.txt_email.get()=="" or self.txt_pass.get()=="":
            messagebox.showerror("Error","All fields are required")
            return

        try:

            con=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="kryptoradb")

            cur=con.cursor()

            cur.execute("select * from std_info where email=%s and password=%s",
                        (self.txt_email.get(),self.txt_pass.get()))

            row=cur.fetchone()

            if row==None:
                messagebox.showerror("Error","Invalid Email or Password")
            else:
                self.root.destroy()
                import CMS_Form

            con.close()

        except Exception as es:
            messagebox.showerror("Error",f"Error : {str(es)}")

root=Tk()
obj=Login_Window(root)
root.mainloop()
