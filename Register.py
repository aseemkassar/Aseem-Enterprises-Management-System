from tkinter import *
from tkinter import messagebox
import database
import pymysql

class Register:

    def __init__(self,root):

        self.root=root
        self.root.title("Register - Aseem Enterprises")
        self.root.geometry("900x550+200+80")
        self.root.config(bg="white")

#================ TITLE =================

        title=Label(self.root,text="Create New Account",
                    font=("Arial",25,"bold"),
                    bg="white",fg="#033054")

        title.pack(pady=20)

#================ FRAME =================

        frame=Frame(self.root,bg="white")
        frame.pack()

        Label(frame,text="First Name",font=("Arial",12),
              bg="white").grid(row=0,column=0,padx=20,pady=10)

        self.fname=Entry(frame,font=("Arial",12))
        self.fname.grid(row=0,column=1)

        Label(frame,text="Last Name",font=("Arial",12),
              bg="white").grid(row=1,column=0,padx=20,pady=10)

        self.lname=Entry(frame,font=("Arial",12))
        self.lname.grid(row=1,column=1)

        Label(frame,text="Contact",font=("Arial",12),
              bg="white").grid(row=2,column=0,padx=20,pady=10)

        self.contact=Entry(frame,font=("Arial",12))
        self.contact.grid(row=2,column=1)

        Label(frame,text="Email",font=("Arial",12),
              bg="white").grid(row=3,column=0,padx=20,pady=10)

        self.email=Entry(frame,font=("Arial",12))
        self.email.grid(row=3,column=1)

        Label(frame,text="Password",font=("Arial",12),
              bg="white").grid(row=4,column=0,padx=20,pady=10)

        self.password=Entry(frame,font=("Arial",12),show="*")
        self.password.grid(row=4,column=1)

        Button(self.root,text="REGISTER",
               command=self.register_data,
               bg="green",fg="white",
               font=("Arial",14)).pack(pady=20)

        Button(self.root,text="Back to Login",
               command=self.login_window,
               bg="#033054",fg="white",
               font=("Arial",12)).pack()

#================ FUNCTIONS =================

    def login_window(self):
        self.root.destroy()
        import LoginForm

    def register_data(self):

        if self.fname.get()=="" or self.email.get()=="" or self.password.get()=="":
            messagebox.showerror("Error","All fields are required")
            return

        try:

            con=pymysql.connect(host="localhost",
                                user="root",
                                password="",
                                database="kryptoradb")

            cur=con.cursor()

            cur.execute("insert into std_info(f_name,l_name,contact,email,password) values(%s,%s,%s,%s,%s)",
                        (self.fname.get(),
                         self.lname.get(),
                         self.contact.get(),
                         self.email.get(),
                         self.password.get()))

            con.commit()
            con.close()

            messagebox.showinfo("Success","Registration Successful")

        except Exception as es:
            messagebox.showerror("Error",f"Error : {str(es)}")

root=Tk()
obj=Register(root)
root.mainloop()
