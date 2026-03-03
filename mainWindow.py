import tkinter
from tkinter import messagebox as msg
from connection import *
import adminLogin
import centerLogin
from tkinter import NW
from PIL import Image, ImageTk


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.state("zoomed")
        self.root.title("Main Window")
        self.primarycolor = "#8EA8C3"
        self.secondaycolor = "#CBF7ED"
        self.txtcolor = "black"
        # self.title = tkinter.Label(self.root, text="Criminal Detection System", font=("Arial", "20", "bold"), bg=self.secondaycolor,
        #                            fg=self.txtcolor)
        # self.title.pack(pady=20)


        self.formFont = ("Arial", 14)

        self.root.configure(bg=self.secondaycolor)

        self.conn = Connect()
        self.cur = self.conn.cursor()

        self.image = Image.open('detective.jpg')
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.img = self.image.resize((self.width, self.height // 1))
        bg = ImageTk.PhotoImage(self.img)

        c = tkinter.Canvas(self.root, width=self.width, height=self.height // 1, highlightthickness=2,
                           highlightbackground='black')
        c.pack(fill='both', expand=True)
        c.create_image(0, 0, image=bg, anchor=NW)

        c.create_text(800,67,font=('Arial',40,'bold'),text="Criminal Detection System",fill="black")

        c.create_text(1200,280, font=('castellar', 38, 'bold'), text="Let's Investigate", fill="black")

        btn=tkinter.Button(self.root,text="Admin Login",width=20,font=('Arial',13,'bold'),command=adminLogin.Main)
        c.create_window(1300,400,window=btn,anchor="ne")

        btn2= tkinter.Button(self.root, text="Center Login", width=20, font=('Arial', 13, 'bold'),command=centerLogin.Main)
        c.create_window(1300, 500, window=btn2, anchor="ne")

        btn3 = tkinter.Button(self.root, text="Leave", width=20, font=('Arial', 13, 'bold'),command=self.exitWindow)
        c.create_window(1300, 600, window=btn3, anchor="ne")

        self.root.mainloop()

    def exitWindow(self):
            self.root.destroy()


obj=Main()