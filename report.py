import tkinter
from tkinter import messagebox as msg
from connection import *
from tkinter import ttk
from tkcalendar import DateEntry

class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("750x750")
        self.root.title("Report")
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = 'black'
        self.title = tkinter.Label(self.root, text="Add Report", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor,width=10)
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)

        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Title", font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=20, pady=20)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt1.grid(row=0, column=1, padx=20, pady=20)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Description", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=20, pady=20)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt2.grid(row=1, column=1, padx=20, pady=20)

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Date", font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=20, pady=20)
        self.txt3 =DateEntry(self.formFrame, font=self.formFont,relief="solid",date_pattern="dd/mm/yyyy")
        self.txt3.grid(row=2, column=1, padx=20, pady=20)

        self.lb4 = tkinter.Label(self.formFrame, text="Criminal Name", font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=20, pady=20)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt4.grid(row=3, column=1, padx=20, pady=20)

        self.lb5 = tkinter.Label(self.formFrame, text="Contact", font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=20, pady=20)
        self.txt5 = tkinter.Entry(self.formFrame, font=self.formFont, relief="solid")
        self.txt5.grid(row=4, column=1, padx=20, pady=20)

        self.lb6 = tkinter.Label(self.formFrame, text="Email", font=self.formFont, bg=self.primarycolor)
        self.lb6.grid(row=5, column=0, padx=20, pady=20)
        self.txt6 = tkinter.Entry(self.formFrame, font=self.formFont, relief="solid")
        self.txt6.grid(row=5, column=1, padx=20, pady=20)

        self.lb7 = tkinter.Label(self.formFrame, text="Address", font=self.formFont, bg=self.primarycolor)
        self.lb7.grid(row=6, column=0, padx=20, pady=20)
        self.txt7 = tkinter.Entry(self.formFrame, font=self.formFont, relief="solid")
        self.txt7.grid(row=6, column=1, padx=20, pady=20)

        self.buttonFrame=tkinter.Frame(self.root,bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Submit",font=self.formFont,command=self.getFormValues,width=12,bg=self.primarycolor,fg=self.txtcolor,relief="raised")
        self.btn3.grid(row=0, column=0, padx=20, pady=20)

        self.root.mainloop()

    def getFormValues(self):
        self.title=self.txt1.get()
        self.description=self.txt2.get()
        self.date=self.txt3.get()
        self.criminal_name = self.txt4.get()
        self.contact = self.txt5.get()
        self.email = self.txt6.get()
        self.address = self.txt7.get()

        if self.title == "" or self.description == "" or self.date == "" or self.criminal_name == "" or self.contact=='' or self.email=='' or self.address=='':
            msg.showwarning("Warning", "Enter your Values", parent=self.root)
        else:
            q = f"insert into report values(null,'{self.title}', '{self.description}', '{self.date}','{self.criminal_name}','{self.contact}','{self.email}','{self.address}')"
            self.cur.execute(q)
            self.conn.commit()
            msg.showwarning("Success", "Report has been added", parent=self.root)


# obj=Main()
if __name__ == "__main__":
    obj = Main()