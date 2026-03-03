import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x500")
        self.root.title("Insert Form")
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = "black"
        self.title = tkinter.Label(self.root, text="Add Admin", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor,width=15)
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)


        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Mobile", font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password", font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont, show="*",relief="raised")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.formFrame, text="Enter Role", font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)

        # Define role values
        role_values = ["Admin", "Super Admin"]

        # Create the combobox
        self.role_combobox = ttk.Combobox(self.formFrame, values=role_values, font=self.formFont)
        self.role_combobox.grid(row=4, column=1, padx=10, pady=10)

        self.buttonFrame=tkinter.Frame(self.root,bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Submit",font=self.formFont,command=self.getFormValues,width=12,bg=self.primarycolor,fg=self.txtcolor,relief="raised")
        self.btn3.grid(row=0, column=0, padx=10, pady=30)

        # self.btn = tkinter.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues)
        # self.btn.pack(pady=10)

        self.root.mainloop()

    def getFormValues(self):
        self.name=self.txt1.get()
        self.email=self.txt2.get()
        self.mobile=self.txt3.get()
        self.password = self.txt4.get()
        self.role = self.role_combobox.get()

        if self.name == "" or self.email == "" or self.mobile == "" or self.password == "" or self.role=='':
            msg.showwarning("Warning", "Enter your Values", parent=self.root)
        else:
            q4=f"select * from admin where email='{self.email}'"
            self.cur.execute(q4)
            email=self.cur.fetchall()
            if len(email)==0:
                q5=f"select * from admin where mobile='{self.mobile}'"
                self.cur.execute(q5)
                mobile=self.cur.fetchall()
                if len(mobile)==0:
                    if email_valid(self.email):
                        if mobile_valid(self.mobile):
                            q=f"insert into admin values(null,'{self.name}', '{self.email}', '{self.mobile}','{self.password}','{self.role}')"
                            self.cur.execute(q)
                            self.conn.commit()
                            msg.showwarning("Success", "Admin has been added", parent=self.root)

                        else:
                            msg.showwarning("Warning","Enter valid mobile no", parent=self.root)

                    else:
                        msg.showwarning("Warning","enter valid email address", parent=self.root)
                        parent = self.root
                else:
                    msg.showwarning("Warning","mobile already exist", parent=self.root)
                    parent = self.root
            else:
                msg.showwarning("Warning","Email already exist", parent=self.root)
                parent = self.root




# obj=Main()
if __name__ == "__main__":
    obj = Main()