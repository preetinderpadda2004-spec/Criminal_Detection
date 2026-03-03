import os
import cv2
import numpy as np
import datetime
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg
from connection import Connect  # Ensure your 'connect' module is correctly imported
import email_verification
# import face_recognition


class addRemarks:
    def __init__(self, center_name):
        self.center_name = center_name
        print(self.center_name)
        self.root = Toplevel()
        self.root.title("Criminal Detection || Add Remark")
        self.root.state("zoomed")

        self.font = ('Times New Roman', 14)
        self.font1 = ('Times New Roman', 16, 'bold')

        self.mainBackground = "#E3D3E4"
        self.frameBackground = "#946E83"

        self.root.configure(bg=self.mainBackground)
        self.conn = Connect()
        self.cr = self.conn.cursor()

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)

        self.root.columnconfigure(1, weight=1)  # Expand the right column

        self.frame = Frame(self.root, pady=10, padx=10, bg=self.mainBackground, width=int(width), height=int(height))
        self.frame.pack(expand=True, fill='both')
        self.frame.pack_propagate(0)

        width_1 = int(self.frame.winfo_screenwidth() / 2)
        height_2 = int(self.frame.winfo_screenheight() - 200)

        self.frame1 = Frame(self.frame, highlightthickness=4, highlightbackground='black', width=int(width_1),
                            height=int(height_2), bg=self.frameBackground, padx=10, pady=10)
        self.frame1.grid(row=0, column=0, padx=12, pady=35)
        self.frame1.grid_propagate(0)

        self.frame2 = Frame(self.frame, highlightthickness=4, bg=self.frameBackground, highlightbackground='black',
                            width=width_1, height=height_2)
        self.frame2.grid(row=0, column=1, pady=35)
        self.frame2.grid_propagate(0)

        self.mainLabel1 = Label(self.frame1, text="CRIMINAL DETECTION SYSTEM", font=("Times New Roman", 20, 'bold'),
                                fg='black', bg=self.frameBackground)
        self.mainLabel1.pack(padx=30, pady=10)
        self.frm = Frame(self.frame1, bg=self.mainBackground)
        self.frm.pack(pady=10, padx=30)
        self.lb1 = Label(self.frm, text='Criminal ID:', font=self.font, bg=self.mainBackground)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = Entry(self.frm, font=self.font, width=30, highlightthickness=4, highlightbackground='black')
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.frm, text='Criminal Name:', font=self.font, bg=self.mainBackground)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = Entry(self.frm, font=self.font, width=30, highlightbackground='black', highlightthickness=4)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.frm, text='Date:', font=self.font, bg=self.mainBackground)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.frm, font=self.font, width=30, highlightthickness=4, highlightbackground='black')
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = Label(self.frm, text='Timing:', font=self.font, bg=self.mainBackground)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = Entry(self.frm, font=self.font, width=30, highlightthickness=4, highlightbackground='black')
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = Label(self.frm, text='Center Id :', font=self.font, bg=self.mainBackground)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = Entry(self.frm, font=self.font, width=30, highlightbackground='black', highlightthickness=4)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = Label(self.frm, text="Enter Remarks:", font=self.font, bg=self.mainBackground)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = Text(self.frm, font=self.font, width=30, height=4, highlightbackground='black',
                         highlightthickness=4)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.btn = Button(self.frame1, text='Submit', font=self.font, width=35, relief=tk.SOLID,
                          borderwidth=2, command=self.getSubmit)
        self.btn.pack(pady=42, padx=25)
        self.btn.bind("<Enter>", self.on_enter_btn)
        self.btn.bind("<Leave>", self.on_leave_btn)

        self.displayFrame = Frame(self.frame2, width=self.frame2.winfo_width(), padx=40, pady=40,
                                  height=int(self.frame2.winfo_screenheight()) - 350)
        self.displayFrame.pack(pady=10, expand=True, fill='both', padx=10)
        self.displayFrame.pack_propagate(0)

        self.camLabel = Label(self.displayFrame)
        self.camLabel.pack(anchor=NW)

        self.btnFrame = Frame(self.frame2, width=int(self.frame2.winfo_width() * 2 / 3), bg=self.frameBackground)
        self.btnFrame.pack(pady=20, padx=20)
        self.btnFrame.pack_propagate(0)

        self.cameraButton = Button(self.btnFrame, text='Open Camera', font=self.font, width=18, relief=tk.SOLID,
                                   command=self.openCamera, anchor='center', bg=self.mainBackground)
        self.cameraButton.grid(row=0, column=0, pady=20, padx=15)

        self.cameraClose = Button(self.btnFrame, text="Capture", font=self.font, width=18, relief=tk.SOLID,
                                  bg=self.mainBackground, command=self.captureImage)
        self.cameraClose.grid(row=0, column=1, pady=20, padx=15)

        self.imageButton = Button(self.btnFrame, text="Close Camera", font=self.font, width=18, relief=tk.SOLID,
                                  bg=self.mainBackground, command=self.closeCamera)
        self.imageButton.grid(row=0, column=2, pady=20, padx=15)

        self.cameraButton.bind("<Enter>", self.on_enter_btn)
        self.cameraButton.bind("<Leave>", self.on_leave_btn)

        self.cameraClose.bind("<Enter>", self.on_enter_btn)
        self.cameraClose.bind("<Leave>", self.on_leave_btn)

        self.imageButton.bind("<Enter>", self.on_enter_btn)
        self.imageButton.bind("<Leave>", self.on_leave_btn)

        # Load the trained model and label dictionary
        self.label_dict = self.train_model()
        self.root.mainloop()

    def train_model(self):
        # Initialize the LBPH face recognizer
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        # Load the face detector
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Create lists to store face images and labels
        faces = []
        labels = []
        label_dict = {}

        # Assign a unique label to each user
        label_id = 0
        dataset_dir = "dataset"

        for user_name in os.listdir(dataset_dir):
            user_dir = os.path.join(dataset_dir, user_name)

            if not os.path.isdir(user_dir):
                continue

            # Assign a label to the user
            label_dict[label_id] = user_name

            for image_name in os.listdir(user_dir):
                image_path = os.path.join(user_dir, image_name)
                img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

                if img is None:
                    continue

                # Detect faces in the image
                detected_faces = face_cascade.detectMultiScale(img, 1.1, 4)

                for (x, y, w, h) in detected_faces:
                    # Add face and label to the lists
                    faces.append(img[y:y + h, x:x + w])
                    labels.append(label_id)

            label_id += 1

        # Train the recognizer
        recognizer.train(faces, np.array(labels))
        recognizer.write("face_trainer.yml")

        return label_dict

    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.recognizer.read("face_trainer.yml")
        self.show_frames()

    def closeCamera(self):
        if hasattr(self, 'cap'):
            self.cap.release()
            cv2.destroyAllWindows()
            self.camLabel.configure(image='')
            self.cameraButton.configure(command=self.openCamera, text='Open Camera')

    def captureImage(self):
        if hasattr(self, 'cap'):
            ret, frame = self.cap.read()
            if ret:
                img_name = "captured_image.png"
                cv2.imwrite(img_name, frame)
                msg.showinfo("Image Capture", f"Image saved as {img_name}", parent=self.root)

    def show_frames(self):
        if not hasattr(self, 'cap'):
            return

        ret, frame = self.cap.read()
        if not ret:
            return

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            id_, confidence = self.recognizer.predict(roi_gray)

            if confidence < 100:
                name = self.label_dict.get(id_, "Unknown")
                confidence_text = f"{round(100 - confidence)}%"
                if round(100 - confidence) >= 30:
                    self.getCriminalData(name)
            else:
                name = "Unknown"
                confidence_text = "N/A"

            cv2.putText(frame, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            cv2.putText(frame, confidence_text, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2_image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.camLabel.imgtk = imgtk
        self.camLabel.configure(image=imgtk)

        self.camLabel.after(10, self.show_frames)

    def getCriminalData(self, id):
        print(id)
        self.cr.execute(f"SELECT * FROM criminal WHERE id='{id}'")
        data = self.cr.fetchall()
        print(data)
        self.txt1.delete(0, END)
        self.txt1.insert(0, id)
        self.txt2.delete(0, END)
        self.txt2.insert(0, data[0][1])
        self.txt3.delete(0, END)
        self.txt3.insert(0, str(datetime.date.today()))
        self.txt4.delete(0, END)
        self.txt4.insert(0, str(datetime.datetime.now().time()))
        self.txt5.delete(0, END)
        self.txt5.insert(0, self.center_name)

    def sendRemarks(self, criminal_id):
        q = f"select Name from criminal where id='{criminal_id}'"
        self.cr.execute(q)
        criminals_data = self.cr.fetchone()
        center_id = self.txt5.get()

        q1 = f"select name, email, mobile, state, city from center where id='{center_id}'"
        self.cr.execute(q1)
        center_data = self.cr.fetchone()
        date = self.txt3.get()
        time = self.txt4.get()
        description = self.txt6.get('1.0', 'end-1c')

        message = f'''
               Criminal Name - {criminals_data[0]} has been identified at {time} on {date}.

               Here are Center Details - 
               Center Name - {center_data[0]}
               Center Mobile - {center_data[2]}
               Center Email - {center_data[1]}
               Location - {center_data[4]}
               Area - {center_data[3]}

               Here are Center Remarks - 
               {description}
           '''
        subject = "Criminal Report"

        x = email_verification.sendEmail(to=center_data[1], message=message, subject=subject)
        if x:
            msg.showinfo("Sent", "Mail has been sent", parent=self.root)
        else:
            msg.showwarning('Warn', 'Mail not sent', parent=self.root)

    def getSubmit(self):
        if not (
                self.txt1.get() and self.txt2.get() and self.txt3.get() and self.txt4.get() and self.txt5.get() and self.txt6.get(
                "1.0", END)):
            msg.showinfo("Error", "Please fill all fields", parent=self.root)
            return
        criminal_id = self.txt1.get()
        name = self.txt2.get()
        date = self.txt3.get()
        timing = self.txt4.get()
        center_name = self.txt5.get()
        remarks = self.txt6.get("1.0", END)
        self.cr.execute(
            f"INSERT INTO remarks  VALUES (null,'{criminal_id}', '{center_name}', '{date}', '{timing}', '{remarks}', '{name}')")
        print("Data submitted")
        self.conn.commit()
        self.sendRemarks(criminal_id)
        msg.showinfo("Success", "Data submitted successfully",parent=self.root)
        self.txt1.delete(0,"end")
        self.txt2.delete(0,"end")
        self.txt3.delete(0,"end")
        self.txt4.delete(0,"end")
        self.txt5.delete(0,"end")
        self.txt6.delete("1.0","end")

    def on_enter_btn(self, e):
        e.widget['background'] = '#ABABAB'

    def on_leave_btn(self, e):
        e.widget['background'] = self.mainBackground


if __name__ == "__main__":
    root = Tk()  # Create the root window
    root.withdraw()  # Hide the root window
    addRemarks(3)