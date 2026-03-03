import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk

from connection import Connect


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Criminal')
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = 'black'
        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.mainLabel = Label(self.root, text='View Report', font=('Arial', 28, 'bold'),bg=self.secondaycolor,fg=self.txtcolor,width=14)
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search', font=('Arial', 14),bg=self.primarycolor)
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14),relief="solid")
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchreport,bg=self.primarycolor)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.resetreport,bg=self.primarycolor)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)
        self.btn3 = Button(self.searchFrame, text='Delete', font=('Arial', 14), command=self.deletereport,bg=self.primarycolor)
        self.btn3.grid(row=0, column=4, pady=10, padx=10)

        self.reportTable = ttk.Treeview(self.root,
                                        columns=['id', 'title', 'description', 'date', 'criminal_name', 'mobile',
                                                 'email', 'address'])
        self.reportTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.reportTable.heading('id', text="Id")
        self.reportTable.heading('title', text="Title")
        self.reportTable.heading('description', text="Description")
        self.reportTable.heading('date', text="Date")

        self.reportTable.heading('criminal_name', text="Criminal_name")
        self.reportTable.heading('mobile', text="Mobile")
        self.reportTable.heading('email', text="Email")
        self.reportTable.heading('address', text="Address")
        self.reportTable['show'] = 'headings'
        self.getValues()
        self.reportTable.bind('<Double-1>', self.updateWindow)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select * from report"
        self.cur.execute(q)
        result = self.cur.fetchall()
        for row in self.reportTable.get_children():
            self.reportTable.delete(row)

        index = 0
        for row in result:
            self.reportTable.insert("", index=index, values=row)
            index += 1

    def resetreport(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchreport(self):
        text = self.txt1.get()
        q = f"select id,title,description, date,criminal_name,contact,email,address from report where id like '%{text}%' or title like '%{text}%' or description like '%{text}%' or date like '%{text}%' or criminal_name like '%{text}%' or contact like '%{text}%' or email like '%{text}%' or address like '%{text}%' "
        self.cur.execute(q)
        result = self.cur.fetchall()

        for row in self.reportTable.get_children():
            self.reportTable.delete(row)

        index = 0
        for row in result:
            self.reportTable.insert("", index=index, values=row)
            index += 1

    def deletereport(self):
        row = self.reportTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "No Data Found", parent=self.root)
        else:
            row_name = row[0]
            items = self.reportTable.item(row_name)
            data = items["values"]
            print(data)
            confirm = msg.askyesno("Warning", "Do you want to delete?", parent=self.root)
            if confirm:
                q = f"delete from report where id ='{data[0]}'"
                self.cur.execute(q)
                self.conn.commit()
                self.resetreport()
                msg.showinfo("Delete", "Deletion Successful", parent=self.root)
            else:
                msg.showinfo("Delete", "Deletion Failed", parent=self.root)

    def updateWindow(self, e):
        row = self.reportTable.selection()
        row_id = row[0]
        items = self.reportTable.item(row_id)
        data = items["values"]
        self.root1 = tkinter.Tk()
        self.root1.geometry("650x650")
        self.root1.title("Center")
        self.root1.configure(bg=self.secondaycolor)
        self.title = tkinter.Label(self.root1, text="Update Report", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor,width=14)
        self.title.pack(pady=10)

        self.formFont = ("Arial", 14)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.formFrame = tkinter.Frame(self.root1,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tkinter.Label(self.formFrame, text="Enter Id", font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Title", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = tkinter.Label(self.formFrame, text="Enter Description", font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Date", font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = tkinter.Label(self.formFrame, text="Enter Criminal_name", font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = tkinter.Label(self.formFrame, text="Enter Mobile", font=self.formFont,bg=self.primarycolor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.lb7 = tkinter.Label(self.formFrame, text="Enter Email", font=self.formFont,bg=self.primarycolor)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.txt7.insert(0, data[6])

        self.lb8 = tkinter.Label(self.formFrame, text="Enter Address", font=self.formFont,bg=self.primarycolor)
        self.lb8.grid(row=7, column=0, padx=10, pady=10)
        self.txt8 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt8.grid(row=7, column=1, padx=10, pady=10)
        self.txt8.insert(0, data[7])

        self.buttonFrame = tkinter.Frame(self.root1,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.buttonFrame.pack()

        self.btn = tkinter.Button(self.buttonFrame, text="Update", font=self.formFont, command=self.getFormValues,bg=self.primarycolor)
        self.btn.grid(row=0, column=0, padx=10, pady=10)

        self.root1.mainloop()

    def getFormValues(self):
        self.id = self.txt1.get()
        self.title = self.txt2.get()
        self.description = self.txt3.get()
        self.date = self.txt4.get()
        self.criminal_name = self.txt5.get()
        self.mobile = self.txt6.get()
        self.email = self.txt7.get()
        self.address = self.txt8.get()

        if self.title == '' or self.description == "" or self.date == '' or self.criminal_name == "" or self.mobile == "" or self.email == "" or self.address == "":
            msg.showwarning("Warning", "Please Enter Values.", parent=self.root1)
        else:
            q = f"update report set title='{self.title}' , descripton='{self.description}' , date='{self.date}' , criminal_name='{self.criminal_name}' , mobile='{self.mobile}' , email='{self.email}', address='{self.address}'"
            self.cur.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success", "Updation Successful", parent=self.root1)
            self.root1.destroy()


if __name__ == "__main__":
    obj = Main()
# obj = Main()