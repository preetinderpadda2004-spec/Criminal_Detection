import tkinter as tk
from tkinter.filedialog import askopenfilename
import tkinter.messagebox as msg
from tkinter import ttk
from connection import *
import cv2
import random


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

        self.title = tk.Label(self.root, text='Add Criminal', font=("Arial", '20', 'bold'),bg=self.secondaycolor)
        self.title.pack(pady=20)

        self.formFont = ("Arial", 14)

        self.formFrame = tk.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tk.Label(self.formFrame, text='Enter Name', font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tk.Label(self.formFrame, text='Enter Gender', font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tk.Label(self.formFrame, text='Enter DOB', font=self.formFont,bg=self.primarycolor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tk.Label(self.formFrame, text='Enter Mobile', font=self.formFont,bg=self.primarycolor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tk.Label(self.formFrame, text='Enter Address', font=self.formFont,bg=self.primarycolor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tk.Entry(self.formFrame, font=self.formFont)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = tk.Label(self.formFrame, text='Enter Family_Member', font=self.formFont,bg=self.primarycolor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = ttk.Entry(self.formFrame, font=self.formFont)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.lb7 = tk.Label(self.formFrame, text='Enter Member_contact', font=self.formFont,bg=self.primarycolor)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7 = ttk.Entry(self.formFrame, font=self.formFont)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)

        self.lb8 = tk.Label(self.formFrame, text='Select Image', font=self.formFont,bg=self.primarycolor)
        self.lb8.grid(row=7, column=0, padx=10, pady=10)
        self.txt8 = ttk.Entry(self.formFrame, font=self.formFont)
        self.txt8.grid(row=7, column=1, padx=10, pady=10)
        self.btn8 = tk.Button(self.formFrame, text="select", font=self.formFont, command=self.selectImage,bg=self.secondaycolor)
        self.btn8.grid(row=7, column=2, pady=10, padx=10)

        self.lb9 = tk.Label(self.formFrame, text='Select category', font=self.formFont,bg=self.primarycolor)
        self.lb9.grid(row=8, column=0, padx=10, pady=10)
        self.txt9 = ttk.Combobox(self.formFrame, font=self.formFont, state='readonly',values=['murder','thief','kidnapper'])
        self.txt9.grid(row=8, column=1, padx=10, pady=10)
        self.txt9 = ttk.Combobox(self.formFrame, values=self.getcategory(), font=self.formFont, state='readonly')
        self.txt9.grid(row=8, column=1, padx=10, pady=10)
        # self.txt9.bind("<<ComboboxSelected>>", self.getcategory)

        self.btn = tk.Button(self.root, text="Submit", font=self.formFont, command=self.getFormValues,bg=self.secondaycolor)
        self.btn.pack(pady=10)
        self.resetCriminal()

        self.btnFrame = tk.Frame(self.root)
        self.btnFrame.pack(pady=10)

        self.root.mainloop()

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
            msg.showwarning("Warning", "Please Enter Values.", parent=self.root)

        else:
            q = f"insert into criminal values(null,'{self.name}', '{self.gender}', '{self.dob}','{self.mobile}','{self.address}','{self.family_member}','{self.member_contact}','{self.image}','{self.category}')"
            self.cr.execute(q)
            self.conn.commit()
            msg.showwarning("Success", "Criminal has been added", parent=self.root)

    def resetCriminal(self):
        self.txt1.delete(0, tk.END)
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')
        self.txt5.delete(0, 'end')
        self.txt6.delete(0, 'end')

    def selectImage(self):
        name = self.txt1.get()
        if len(name) != 0:
            path = askopenfilename(parent=self.root)
            print(path)
            img = cv2.imread(path)
            # print(cv2.data.haarcascades)
            cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            # cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            face = cascade.detectMultiScale(img, 1.1, 4)
            if len(face) == 0:
                msg.showwarning("Warning", 'Image is not Valid', parent=self.root)
            else:
                msg.showinfo("Success", 'Image is Valid', parent=self.root)
                img_name = f"{name}_{random.randint(10000, 99999)}.jpeg"
                cv2.imwrite(f"../criminal_image/{img_name}", img)
                # cv2.imwrite(f"criminals_dir/{img_name}", img)
                self.txt8.insert(0, img_name)
        else:
            msg.showwarning("Warning", "Please Enter your Name", parent=self.root)

    def getcategory(self):
        q = f"select distinct name from category"
        self.cr.execute(q)
        rows = self.cr.fetchall()
        return [row[0] for row in rows]


if __name__ == "__main__":
    obj = Main()