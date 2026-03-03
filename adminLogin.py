import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk
import dashboard


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x500")
        self.root.title("Login")
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = "black"
        self.title = tkinter.Label(self.root, text="Admin Login", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor,width=10)
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)

        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Password", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid",show="*")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.buttonFrame = tkinter.Frame(self.root, bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Login",font=self.formFont,command=self.adminLogin,width=12,bg=self.primarycolor,fg=self.txtcolor,relief="raised")
        self.btn3.grid(row=0, column=0, padx=10, pady=30)

        # self.btn = tkinter.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues)
        # self.btn.pack(pady=10)

        self.root.mainloop()

    def adminLogin(self):
        email=self.txt1.get()
        password=self.txt2.get()
        q=f"select * from admin where email='{email}' and password='{password}'"
        self.cur.execute(q)
        res=self.cur.fetchall()
        print(res)
        if len(res)==0:
            msg.showwarning("Warning", "Invalid Email/Password",parent=self.root)
        else:
            msg.showinfo("Success","Login Successful",parent=self.root)
            self.root.destroy()
            dashboard.Main(adminDetails=res)


if __name__ == "__main__":
    obj = Main()