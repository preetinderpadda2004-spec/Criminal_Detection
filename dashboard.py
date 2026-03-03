import tkinter
import admin
import center
import changePassword
import criminal
import category
import location
import viewAdmin
import viewcenter
import viewcriminal
import viewCategory
import viewLocation
from tkinter import NW
from PIL import Image, ImageTk

import tkinter.messagebox as msg
from connection import Connect


class Main:
    def __init__(self,adminDetails):
        self.detail=adminDetails
        self.root = tkinter.Toplevel()
        self.root.state("zoomed")
        self.root.title('Welcome to Admin Dashboard')

        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtColor = '#FEFBD8'

        self.mainMenu = tkinter.Menu(self.root)
        self.root.configure(menu=self.mainMenu)

        if self.detail[0][-1]=="Super Admin":
            self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
            self.mainMenu.add_cascade(label='Manage Admin', menu=self.fileMenu)
            self.fileMenu.add_command(label='Add Admin', command=admin.Main)
            self.fileMenu.add_command(label='View Admin',command=viewAdmin.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Category', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Category', command=category.Main)
        self.fileMenu.add_command(label='View Category',command=viewCategory.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Location', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Location', command=location.Main)
        self.fileMenu.add_command(label='View Location',command=viewLocation.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Center', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Center', command=center.Main)
        self.fileMenu.add_command(label='View Center',command=viewcenter.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Criminal', menu=self.fileMenu)
        self.fileMenu.add_command(label='Add Criminal', command=criminal.Main)
        self.fileMenu.add_command(label='View Criminal',command=viewcriminal.Main)

        self.fileMenu = tkinter.Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label='Manage Profile', menu=self.fileMenu)
        self.fileMenu.add_command(label='Change Password',command=lambda:changePassword.Main(self.detail[0][2]))
        self.fileMenu.add_command(label='Exit', command=self.exitWindow)

        self.root.configure(bg=self.primarycolor)

        self.image = Image.open('detective2.jpg')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.img = self.image.resize((self.width, self.height // 1))
        bg = ImageTk.PhotoImage(self.img)

        c = tkinter.Canvas(self.root, width=self.width, height=self.height // 1, highlightthickness=2,
                           highlightbackground='black')
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor=NW)
        c.create_text(800, 67, font=('Arial', 30, 'bold', 'underline'), text="Dashboard",fill="black")

        self.root.mainloop()

    def exitWindow(self):
        self.root.destroy()


# obj = Main()

if __name__ == "__main__":
    obj = Main("Krrish")