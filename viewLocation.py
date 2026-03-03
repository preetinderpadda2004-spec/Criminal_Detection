from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Python MySQL Read Operation')
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = 'black'
        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.mainLabel = Label(self.root, text='View Location',font=('Arial',28,'bold'),bg=self.secondaycolor,fg=self.txtcolor,width=14)
        self.mainLabel.pack(pady=20)

        self.searchFrame = Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.searchFrame.pack(pady=20)

        self.lbl = Label(self.searchFrame, text='Search', font=('Arial', 14),bg=self.primarycolor)
        self.lbl.grid(row=0, column=0, pady=10, padx=10)
        self.txt1 = Entry(self.searchFrame, font=('Arial', 14),relief="solid")
        self.txt1.grid(row=0, column=1, pady=10, padx=10)
        self.btn1 = Button(self.searchFrame, text='Search', font=('Arial', 14), command=self.searchLocation,bg=self.primarycolor)
        self.btn1.grid(row=0, column=2, pady=10, padx=10)
        self.btn2 = Button(self.searchFrame, text='Refresh', font=('Arial', 14), command=self.resetLocation,bg=self.primarycolor)
        self.btn2.grid(row=0, column=3, pady=10, padx=10)
        self.btn3 = Button(self.searchFrame, text='Delete', font=('Arial', 14), command=self.deleteLocation,bg=self.primarycolor)
        self.btn3.grid(row=0, column=4, pady=10, padx=10)


        self.locationTable = ttk.Treeview(self.root, columns=['state','city'])
        self.locationTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.locationTable.heading('state', text="State")
        self.locationTable.heading('city', text="City")
        self.locationTable['show'] = 'headings'
        self.getValues()

        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 14), rowheight=40)
        style.configure("Treeview.Heading", font=("Arial", 14))

        self.root.mainloop()

    def getValues(self):
        q = f"select * from location"
        self.cur.execute(q)
        result = self.cur.fetchall()
        for row in self.locationTable.get_children():
            self.locationTable.delete(row)

        index = 0
        for row in result:
            self.locationTable.insert("", index=index, values=row)
            index += 1

    def resetLocation(self):
        self.txt1.delete(0, 'end')
        self.getValues()

    def searchLocation(self):
        text = self.txt1.get()
        q = f"select * from location where state like '%{text}%' or city like '%{text}%'"
        self.cur.execute(q)
        result = self.cur.fetchall()

        for row in self.locationTable.get_children():
            self.locationTable.delete(row)

        index = 0
        for row in result:
            self.locationTable.insert("", index=index, values=row)
            index += 1

    def deleteLocation(self):
        row= self.locationTable.selection()
        if len(row)==0:
            msg.showwarning("Warning","No Data Found", parent=self.root)
        else:
            row_state=row[0]
            items=self.locationTable.item(row_state)
            data=items["values"]
            confirm=msg.askyesno("Warning","Do you want to delete?", parent=self.root)
            if confirm:
                q=f"delete from location where state ='{data[0]}'"
                self.cur.execute(q)
                self.conn.commit()
                self.resetLocation()
                msg.showinfo("Delete","Deletion Successful", parent=self.root)
            else:
                msg.showinfo("Delete","Deletion Failed", parent=self.root)


if __name__ == "__main__":
    obj = Main()