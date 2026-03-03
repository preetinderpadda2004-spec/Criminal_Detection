import tkinter
from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
import captureImage

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

        self.mainLabel = Label(self.root, text='View Criminal',font=('Arial',28,'bold'),bg=self.secondaycolor,fg=self.txtcolor,width=14)
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search', font=('Arial', 14),bg=self.primarycolor)
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14),relief="solid")
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchCriminal,bg=self.primarycolor)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.resetCriminal,bg=self.primarycolor)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)
        self.btn3 = Button(self.searchFrame, text='Delete', font=('Arial', 14), command=self.deleteCriminal,bg=self.primarycolor)
        self.btn3.grid(row=0, column=4, pady=10, padx=10)
        self.btn4 = Button(self.searchFrame, text='Detect', font=('Arial', 14), command=self.captureCriminal,bg=self.primarycolor)
        self.btn4.grid(row=0, column=5, pady=10, padx=10)

        self.criminalTable = ttk.Treeview(self.root, columns=['id','name', 'gender', 'dob','mobile','address','family_member','member_contact','image','category'])
        self.criminalTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.criminalTable.heading('id', text="Id")
        self.criminalTable.heading('name', text="Name")
        self.criminalTable.heading('gender', text="Gender")
        self.criminalTable.heading('dob', text="DOB")
        self.criminalTable.heading('mobile', text="Mobile")
        self.criminalTable.heading('address', text="Address")
        self.criminalTable.heading('family_member', text="Family_member")
        self.criminalTable.heading('member_contact', text="Member_contact")
        self.criminalTable.heading('image', text="Image")
        self.criminalTable.heading('category', text="Category")
        self.criminalTable['show'] = 'headings'
        self.getValues()
        self.criminalTable.bind('<Double-1>',self.updateWindow)

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select * from criminal"
        self.cur.execute(q)
        result = self.cur.fetchall()
        for row in self.criminalTable.get_children():
            self.criminalTable.delete(row)

        index = 0
        for row in result:
            self.criminalTable.insert("", index=index, values=row)
            index += 1

    def resetCriminal(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchCriminal(self):
        text = self.txt1.get()
        q = f"select id,name, gender, dob,mobile,address,family_member,member_contact,image,category from criminal where id like '%{text}%' or name like '%{text}%' or gender like '%{text}%' or dob like '%{text}%' or mobile like '%{text}%' or address like '%{text}%' or family_member like '%{text}%' or member_contact like '%{text}%' or image like '%{text}%' or category like '%{text}%'"
        self.cur.execute(q)
        result = self.cur.fetchall()

        for row in self.criminalTable.get_children():
            self.criminalTable.delete(row)

        index = 0
        for row in result:
            self.criminalTable.insert("", index=index, values=row)
            index += 1

    def deleteCriminal(self):
        row = self.criminalTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "No Data Found", parent=self.root)
        else:
            row_name = row[0]
            items = self.criminalTable.item(row_name)
            data = items["values"]
            confirm = msg.askyesno("Warning", "Do you want to delete?", parent=self.root)
            if confirm:
                q = f"delete from criminal where id ='{data[0]}'"
                self.cur.execute(q)
                self.conn.commit()
                self.resetCriminal()
                msg.showinfo("Delete", "Deletion Successful", parent=self.root)
            else:
                msg.showinfo("Delete", "Deletion Failed", parent=self.root)

    def updateWindow(self,e):
        row = self.criminalTable.selection()
        row_id = row[0]
        items = self.criminalTable.item(row_id)
        data = items["values"]
        self.root1 = tkinter.Tk()
        self.root1.geometry("650x650")
        self.root1.title("Center")
        self.root1.configure(bg=self.secondaycolor)
        self.title = tkinter.Label(self.root1, text="Update Criminal", font=("Arial", "20", "bold"),bg=self.secondaycolor,fg=self.txtcolor,width=14)
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

        self.lb2 = tkinter.Label(self.formFrame, text="Enter Gender", font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = tkinter.Label(self.formFrame, text="Enter DOB", font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = tkinter.Label(self.formFrame, text="Enter Address", font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = tkinter.Label(self.formFrame, text="Enter Family_Member", font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = tkinter.Label(self.formFrame, text="Enter Member_contact", font=self.formFont,bg=self.primarycolor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.lb7 = tkinter.Label(self.formFrame, text="Enter Image", font=self.formFont,bg=self.primarycolor)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7 = tkinter.Entry(self.formFrame, font=self.formFont,relief="solid")
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.txt7.insert(0, data[6])

        self.lb8 = tkinter.Label(self.formFrame, text="Enter Category", font=self.formFont,bg=self.primarycolor)
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
        self.name = self.txt1.get()
        self.gender = self.txt2.get()
        self.dob = self.txt3.get()
        self.mobile = self.txt4.get()
        self.address = self.txt5.get()
        self.family_member = self.txt6.get()
        self.member_contact = self.txt7.get()
        self.image = self.txt8.get()
        self.category = self.txt9.get()

        if self.name == '' or self.gender == "" or self.dob == '' or self.mobile == "" or self.address == "" or self.family_member == "" or self.member_contact == "" or self.image == "" or self.category == "":
            msg.showwarning("Warning", "Please Enter Values.", parent=self.root1)
        else:
            q = f"update criminal set name='{self.name}' , gender='{self.gender}' , dob='{self.dob}' , address='{self.address}' , family_member='{self.family_member}' , member_contact='{self.member_contact}', image='{self.image}', category='{self.category}' where name='{self.name}'"
            self.cur.execute(q)
            self.conn.commit()
            self.getValues()
            msg.showinfo("Success","Updation Successful",parent=self.root1)
            self.root1.destroy()

    def captureCriminal(self):
        row = self.criminalTable.selection()
        row_id = row[0]
        items = self.criminalTable.item(row_id)
        data = items["values"]
        id=data[0]
        captureImage.CaptureImage(id=id)



if __name__ == "__main__":
    obj = Main()