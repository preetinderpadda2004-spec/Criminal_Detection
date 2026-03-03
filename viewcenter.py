import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Center')
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = 'black'
        self.root.configure(bg=self.secondaycolor)


        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.mainLabel = Label(self.root, text='View Center',font=('Arial',28,'bold'),bg=self.secondaycolor,fg=self.txtcolor,width=10)
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search', font=('Arial', 14),bg=self.primarycolor)
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14),relief="solid")
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchCenter,bg=self.primarycolor)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.resetCenter,bg=self.primarycolor)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)
        self.btn3 = Button(self.searchFrame, text='Delete', font=('Arial', 14), command=self.deleteCenter,bg=self.primarycolor)
        self.btn3.grid(row=0, column=4, pady=10, padx=10)

        self.centerTable = ttk.Treeview(self.root, columns=['name', 'email', 'mobile', 'password', 'state', 'city'])
        self.centerTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.centerTable.heading('name', text="Name")
        self.centerTable.heading('email', text="Email")
        self.centerTable.heading('mobile', text="Mobile")
        self.centerTable.heading('password', text="Password")
        self.centerTable.heading('state', text="State")
        self.centerTable.heading('city', text="City")
        self.centerTable['show'] = 'headings'
        self.getValues()
        self.centerTable.bind('<Double-1>',self.updateWindow)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select name,email,mobile,password,state,city from center"
        self.cur.execute(q)
        result = self.cur.fetchall()
        for row in self.centerTable.get_children():
            self.centerTable.delete(row)

        index = 0
        for row in result:
            self.centerTable.insert("", index=index, values=row)
            index += 1

    def resetCenter(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchCenter(self):
        text = self.txt1.get()
        q = f"select name, email, mobile, password, state, city from center where name like '%{text}%' or email like '%{text}%' or mobile like '%{text}%' or password like '%{text}%' or state like '%{text}%' or city like '%{text}%'"
        self.cur.execute(q)
        result = self.cur.fetchall()

        for row in self.centerTable.get_children():
            self.centerTable.delete(row)

        index = 0
        for row in result:
            self.centerTable.insert("", index=index, values=row)
            index += 1

    def deleteCenter(self):
        row = self.centerTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "No Data Found", parent=self.root)
        else:
            row_name = row[0]
            items = self.centerTable.item(row_name)
            data = items["values"]
            confirm = msg.askyesno("Warning", "Do you want to delete?", parent=self.root)
            if confirm:
                print(data)
                q = f"delete from center where name ='{data[0]}'"
                self.cur.execute(q)
                self.conn.commit()
                self.resetCenter()
                msg.showinfo("Delete", "Deletion Successful", parent=self.root)
            else:
                msg.showinfo("Delete", "Deletion Failed", parent=self.root)

    def updateWindow(self,e):
        row = self.centerTable.selection()
        row_id = row[0]
        items = self.centerTable.item(row_id)
        data = items["values"]
        self.root1 = tkinter.Tk()
        self.root1.geometry("650x650")
        self.root1.title("Center")
        self.root1.configure(bg=self.secondaycolor)
        self.title = tkinter.Label(self.root1, text="Update Center", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor,width=14)
        self.title.pack(pady=10)

        self.formFont = ("Arial", 14)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root1,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Name", font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Mobile", font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Password", font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = tkinter.Label(self.formFrame, text="Enter State", font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = tkinter.Label(self.formFrame, text="Enter State", font=self.formFont,bg=self.primarycolor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.buttonFrame = tkinter.Frame(self.root1,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.buttonFrame.pack()

        self.btn = tkinter.Button(self.buttonFrame, text="Update", font=self.formFont, command=self.getFormValues,bg=self.primarycolor)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        self.root1.mainloop()

    def getFormValues(self):
        self.name = self.txt1.get()
        self.email = self.txt2.get()
        self.mobile = self.txt3.get()
        self.password = self.txt4.get()
        self.state = self.txt5.get()
        self.city = self.txt6.get()

        if self.name == "" or self.email == "" or self.mobile == "" or self.password == '' or self.state=='' or self.city=='':
            msg.showwarning("Warning", "Enter your Values", parent=self.root1)
        else:
            q = f"update center set name='{self.name}' , email='{self.email}' , mobile='{self.mobile}' , password='{self.password}' , state='{self.state}' , city='{self.city}' where name='{self.name}'"
            self.cur.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success","Updation Successful",parent=self.root1)
            self.root1.destroy()


if __name__ == "__main__":
    obj = Main()