import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
from connection import *

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x600')
        self.root.title('Insert Form')
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = "black"
        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.title = tk.Label(self.root, text='Add Center', font=("Arial", '20', 'bold'),bg=self.secondaycolor)
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)

        self.formFrame = tk.Frame(self.root, bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tk.Label(self.formFrame, text='Enter Name', font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tk.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tk.Label(self.formFrame, text='Enter Email', font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tk.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tk.Label(self.formFrame, text='Enter Mobile', font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tk.Entry(self.formFrame, font=self.formFont,relief="raised")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tk.Label(self.formFrame, text='Enter Password', font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tk.Entry(self.formFrame, show='*', font=self.formFont,relief="raised")
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tk.Label(self.formFrame, text='Select State', font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = ttk.Combobox(self.formFrame, values=self.getstate(), font=self.formFont, state='readonly')
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.bind("<<ComboboxSelected>>", self.update_cities)

        self.lb6 = tk.Label(self.formFrame, text='Select City', font=self.formFont,bg=self.primarycolor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = ttk.Combobox(self.formFrame, values=[], font=self.formFont, state='readonly')
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.btn = tk.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues,bg=self.primarycolor)
        self.btn.pack(pady=10)
        self.resetcenter()

        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.pack(pady=10)

        self.root.mainloop()

    def getstate(self):
        q = f"select distinct state from location"
        self.cr.execute(q)
        rows = self.cr.fetchall()
        return [row[0] for row in rows]

    def update_cities(self, event):
        selected_state = self.txt5.get()
        q = f"select city from location where state = '{selected_state}'"
        self.cr.execute(q)
        rows = self.cr.fetchall()
        city_list = [row[0] for row in rows]
        self.txt6['values'] = city_list
        if city_list:
            self.txt6.current(0)

    def getFormValues(self):
        self.name = self.txt1.get()
        self.email = self.txt2.get()
        self.mobile = self.txt3.get()
        self.password = self.txt4.get()
        self.state = self.txt5.get()
        self.city = self.txt6.get()

        if not all([self.name, self.email, self.mobile, self.password, self.state, self.city]):
            msg.showwarning("Warning", "Please Enter Values.", parent=self.root)
            return

        if not email_valid(self.email):
            msg.showwarning("Warning", "Enter correct email.", parent=self.root)
            return

        if not mobile_valid(self.mobile):
            msg.showwarning("Warning", "Enter correct mobile.", parent=self.root)
            return

        q = f"select * from center where email='{self.email}'"
        self.cr.execute(q)
        if self.cr.fetchall():
            msg.showwarning("Warning", "Email already exists.", parent=self.root)
            return

        q = f"select * from center where mobile='{self.mobile}'"
        self.cr.execute(q)
        if self.cr.fetchall():
            msg.showwarning("Warning", "Mobile already exists.", parent=self.root)
            return

        q = f"insert into center (name, email, mobile, password, state, city) values ('{self.name}', '{self.email}', '{self.mobile}', '{self.password}', '{self.state}', '{self.city}')"
        try:
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo('Success', 'Record inserted successfully!', parent=self.root)
            self.resetcenter()
        except Exception as e:
            msg.showerror('Error', f'Error inserting record: {str(e)}', parent=self.root)
            parent = self.root

    def resetcenter(self):
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, tk.END)
        self.txt3.delete(0, tk.END)
        self.txt4.delete(0, tk.END)
        self.txt5.set('')
        self.txt6.set('')


if __name__ == "__main__":
    obj = Main()