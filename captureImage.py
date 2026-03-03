from tkinter import *
import cv2
import os

class CaptureImage:
    def __init__(self,id):
        self.id=id
        self.root = Tk()
        self.root.geometry('500x500')
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = "black"
        self.root.title('Face Recognition')
        self.root.resizable(False, False)
        self.root.configure(bg=self.secondaycolor)

        self.lb = Label(self.root, text='Enter Id', font=('Arial', 15),fg=self.txtcolor,bg=self.secondaycolor)
        self.lb.pack(pady=20)
        self.txt = Entry(self.root, font=('Arial', 15),relief="raised")
        self.txt.pack(pady=20)
        self.txt.insert(0,self.id)
        self.txt.configure(state="readonly")
        self.btn = Button(self.root, text='Capture', font=('Arial', 15),command=self.capture,fg=self.txtcolor,bg=self.primarycolor)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def capture(self):
        id = self.txt.get()
        user_dir = f'dataset/{id}'
        os.makedirs(user_dir, exist_ok=True)
        cap = cv2.VideoCapture(0)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        count = 1

        while count <= 100:
            ret, frame = cap.read()
            print(frame)
            if not ret:
                break
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)
            for (x, y, w, h) in faces:
                # print(faces)
                face_img = frame[y:y + h, x:x + w]
                img_name = f"{user_dir}/{id}__{count}.jpg"
                cv2.imwrite(img_name, face_img)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                count += 1
        cap.release()
        cv2.destroyAllWindows()


if __name__ == '__main__':
    CaptureImage(109)