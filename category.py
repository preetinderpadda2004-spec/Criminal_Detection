import tkinter
from tkinter import messagebox as msg
from connection import Connect
from tkinter import ttk


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("600x600")
        self.root.title("Insert Form")
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = "black"
        self.root.configure(bg=self.secondaycolor)
        self.title = tkinter.Label(self.root, text="Add Category", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor)
        self.title.pack(pady=10)

        self.formFont = ("Arial", 14)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root, bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.formFont,bg=self.primarycolor,fg=self.txtcolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.btn1=tkinter.Button(self.formFrame,text="Search",command=self.searchCategory,font=self.formFont,bg=self.secondaycolor,fg=self.txtcolor)
        self.btn1.grid(row=0, column=2, padx=10, pady=10)
        self.btn2 = tkinter.Button(self.formFrame, text="Reset", command=self.resetCategory, font=self.formFont,bg=self.secondaycolor,fg=self.txtcolor)
        self.btn2.grid(row=0, column=3, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Description", font=self.formFont,bg=self.primarycolor,fg=self.txtcolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.buttonFrame=tkinter.Frame(self.root,bg=self.secondaycolor)
        self.buttonFrame.pack()

        self.btn3=tkinter.Button(self.buttonFrame,text="Update",font=self.formFont,command=self.getFormValues,bg=self.secondaycolor,fg=self.txtcolor)
        self.btn3.grid(row=0, column=0, padx=10, pady=10)

        self.btn4 = tkinter.Button(self.buttonFrame, text="Delete", font=self.formFont, command=self.deleteCategory,bg=self.secondaycolor,fg=self.txtcolor)
        self.btn4.grid(row=0, column=1, padx=10, pady=10)

        self.root.mainloop()

    def getFormValues(self):
        self.name=self.txt1.get()
        self.description=self.txt2.get()

        if self.name == "" or self.description == "" :
            msg.showwarning("Warning", "Enter your Values", parent=self.root)
        else:
            q=f"insert into category values('{self.name}', '{self.description}')"
            self.cur.execute(q)
            self.conn.commit()
            msg.showwarning("Success", "Category added", parent=self.root)

    def searchCategory(self):
        self.name=self.txt1.get()
        q1=f"select * from category where name='{self.name}'"
        self.cur.execute(q1)
        self.conn.commit()
        res=self.cur.fetchall()
        if len(res)==0:
            msg.showwarning("Warning", "Enter correct name.", parent=self.root)
            parent = self.root
        else:
            admin=res[0]
            self.txt2.insert(0,admin[1])

    def resetCategory(self):
        self.txt1.delete(0,"end")
        self.txt2.delete(0, "end")

    def deleteCategory(self):
        self.name=self.txt1.get()
        q2=f"delete from category where name='{self.name}'"
        self.cur.execute(q2)
        self.conn.commit()
        msg.showwarning("Warning", "Category deleted successfully", parent=self.root)
        parent = self.root
        self.resetCategory()


if __name__ == "__main__":
    obj = Main()