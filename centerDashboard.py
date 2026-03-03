import tkinter
from tkinter import NW

import admin
import center
import changePassword
import criminal
import category
import location
import viewAdmin
import viewcenter
import viewcriminal
import remarks
import viewCategory
import viewLocation
from PIL import Image, ImageTk
import report
import viewremarks
import viewreport

import tkinter.messagebox as msg
from connection import Connect
import centerLogin


class Main:
    def __init__(self,centerDetails):
        self.detail=centerDetails
        self.root = tkinter.Toplevel()
        self.root.state("zoomed")
        self.root.title('Welcome to Center Dashboard')

        self.primaryColor = '#987D9A'
        self.secondaryColor = '#BB9AB1'
        self.txtColor = '#FEFBD8'

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())

        self.mainMenu = tkinter.Menu(self.root)
        self.root.configure(menu=self.mainMenu)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Criminals', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Criminals', command=criminal.Main)
        self.fileMenu.add_command(label='View Criminals',command=viewcriminal.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Reports', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Reports',command=report.Main)
        self.fileMenu.add_command(label='View Reports',command=viewreport.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Remarks', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Remarks',command=lambda:remarks.addRemarks(self.detail[0][0]))
        self.fileMenu.add_command(label='View Remarks',command=viewremarks.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Profile', menu=self.fileMenu)
        self.fileMenu.add_command(label='Change Password',command=lambda:changePassword.Main(self.detail[0][2]))
        self.fileMenu.add_command(label='Log Out', command=self.exitWindow)

        self.image = Image.open('download.jpeg')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.img = self.image.resize((self.width, self.height // 1))
        bg = ImageTk.PhotoImage(self.img)

        c = tkinter.Canvas(self.root, width=self.width, height=self.height // 1, highlightthickness=2,
                           highlightbackground='black')
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor=NW)

        c.create_text(800, 67, font=('Arial', 30, 'bold','underline'), text="Welcome To Center Dashboard", fill="white")

        self.root.configure(bg=self.primaryColor)

        self.root.mainloop()

    def exitWindow(self):
        self.root.destroy()


# obj = Main()

if __name__ == "__main__":
    obj = Main("krrish2@gmail.com")