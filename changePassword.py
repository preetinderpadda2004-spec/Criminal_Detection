import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk


class Main:
    def __init__(self,email):
        self.email=email
        self.root = tkinter.Tk()
        self.root.geometry("600x600")
        self.root.title("Change Password")
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = "black"
        self.title = tkinter.Label(self.root, text="Change Admin Password", font=("Arial", "20", "bold"),
                                   bg=self.secondaycolor, fg=self.txtcolor)
        self.title.pack(pady=40)

        self.formFont = ("Arial", 14)

        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root, bg=self.primarycolor, highlightthickness=2,
                                       highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont, bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont, relief="raised")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0,self.email)
        self.txt1.configure(state="readonly")

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Old Password", font=self.formFont, bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont, relief="raised")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter New Password", font=self.formFont, bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont, relief="raised", show="*")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Retype Password", font=self.formFont, bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont, show="*", relief="raised")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.buttonFrame = tkinter.Frame(self.root, bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3 = tkinter.Button(self.buttonFrame, text="Submit", font=self.formFont, command=self.changePass,
                                   width=12, bg=self.primarycolor, fg=self.txtcolor, relief="raised")
        self.btn3.grid(row=0, column=0, padx=10, pady=30)

        self.root.mainloop()

    def changePass(self):
        email = self.txt1.get()
        oldpass = self.txt2.get()
        newpass = self.txt3.get()
        retypepass = self.txt4.get()
        print(email)
        print(oldpass)
        print(newpass)
        print(retypepass)
        if email == "" or oldpass == "" or newpass == "" or retypepass == "":
            msg.showwarning("Warning", "Enter your Values", parent=self.root)
        else:
            q = f"select * from admin where email='{email}' and password='{oldpass}'"
            self.cur.execute(q)
            data = self.cur.fetchall()
            if len(data) == 0:
                msg.showwarning("Warning", "This Email/Password doesn't exist", parent=self.root)
            elif oldpass == newpass:
                msg.showwarning("Warning", "New Password is same as Old Password", parent=self.root)
            elif newpass == retypepass:
                q1 = f"update admin set password='{newpass}' where email='{email}'"
                self.cur.execute(q1)
                self.conn.commit()
                msg.showinfo("Success", "Password changed successfully", parent=self.root)
            else:
                msg.showwarning("Warning", "New Password is not same as Retype Password", parent=self.root)


if __name__ == "__main__":
    obj = Main("krrish@gmail.com")
