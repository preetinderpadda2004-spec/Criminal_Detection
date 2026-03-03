import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
from connection import Connect

class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('700x600')
        self.root.title('Location Form')
        self.primarycolor = "#E3D3E4"
        self.secondaycolor = "#946E83"
        self.txtcolor = 'black'

        self.title = tk.Label(self.root, text='Add new Location', font=("Arial", '20', 'bold'),bg=self.secondaycolor,fg=self.txtcolor,width=15)
        self.title.pack(pady=20)
        self.root.configure(bg=self.secondaycolor)

        self.formFont = ("Arial", 14)

        self.formFrame = tk.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.formFrame.pack()

        self.lb1 = tk.Label(self.formFrame, text='Select State', font=self.formFont,bg=self.primarycolor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)

        self.states = {
            'Andhra Pradesh': ['Visakhapatnam', 'Vijayawada', 'Guntur', 'Nellore'],
            'Arunachal Pradesh': ['Itanagar', 'Tawang', 'Pasighat', 'Ziro'],
            'Assam': ['Guwahati', 'Dibrugarh', 'Silchar', 'Jorhat'],
            'Bihar': ['Patna', 'Gaya', 'Bhagalpur', 'Muzaffarpur'],
            'Chhattisgarh': ['Raipur', 'Bhilai', 'Bilaspur', 'Durg'],
            'Goa': ['Panaji', 'Margao', 'Vasco da Gama', 'Mapusa'],
            'Gujarat': ['Ahmedabad', 'Surat', 'Vadodara', 'Rajkot'],
            'Haryana': ['Chandigarh', 'Gurgaon', 'Faridabad', 'Panipat'],
            'Himachal Pradesh': ['Shimla', 'Manali', 'Dharamshala', 'Solan'],
            'Jharkhand': ['Ranchi', 'Jamshedpur', 'Dhanbad', 'Bokaro'],
            'Karnataka': ['Bengaluru', 'Mysuru', 'Mangalore', 'Hubballi'],
            'Kerala': ['Thiruvananthapuram', 'Kochi', 'Kozhikode', 'Thrissur'],
            'Madhya Pradesh': ['Bhopal', 'Indore', 'Gwalior', 'Jabalpur'],
            'Maharashtra': ['Mumbai', 'Pune', 'Nagpur', 'Nashik'],
            'Manipur': ['Imphal', 'Churachandpur', 'Thoubal', 'Bishnupur'],
            'Meghalaya': ['Shillong', 'Tura', 'Nongstoin', 'Jowai'],
            'Mizoram': ['Aizawl', 'Lunglei', 'Saiha', 'Champhai'],
            'Nagaland': ['Kohima', 'Dimapur', 'Mokokchung', 'Tuensang'],
            'Odisha': ['Bhubaneswar', 'Cuttack', 'Rourkela', 'Puri'],
            'Punjab': ['Chandigarh', 'Ludhiana', 'Amritsar', 'Jalandhar'],
            'Rajasthan': ['Jaipur', 'Jodhpur', 'Udaipur', 'Kota'],
            'Sikkim': ['Gangtok', 'Namchi', 'Gyalshing', 'Mangan'],
            'Tamil Nadu': ['Chennai', 'Coimbatore', 'Madurai', 'Tiruchirappalli'],
            'Telangana': ['Hyderabad', 'Warangal', 'Nizamabad', 'Karimnagar'],
            'Tripura': ['Agartala', 'Udaipur', 'Kailashahar', 'Dharmanagar'],
            'Uttar Pradesh': ['Lucknow', 'Kanpur', 'Varanasi', 'Agra'],
            'Uttarakhand': ['Dehradun', 'Haridwar', 'Roorkee', 'Haldwani'],
            'West Bengal': ['Kolkata', 'Darjeeling', 'Siliguri', 'Durgapur']
        }

        self.state_combobox = ttk.Combobox(self.formFrame, values=list(self.states.keys()), font=self.formFont)
        self.state_combobox.grid(row=0, column=1, padx=10, pady=10)
        self.state_combobox.set("Select state")
        self.state_combobox.bind("<<ComboboxSelected>>", self.update_cities)

        self.lb2 = tk.Label(self.formFrame, text='Select City', font=self.formFont,bg=self.primarycolor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)

        self.city_combobox = ttk.Combobox(self.formFrame, font=self.formFont)
        self.city_combobox.grid(row=1, column=1, padx=10, pady=10)
        self.city_combobox.set("Select city")

        self.btnFrame = tk.Frame(self.root,bg=self.primarycolor,highlightthickness=2,highlightbackground="black")
        self.btnFrame.pack(pady=10)

        self.submitBtn = tk.Button(self.btnFrame, text="Submit", font=self.formFont, command=self.getFormValues,width=12,bg=self.primarycolor,fg=self.txtcolor,relief="raised")
        self.submitBtn.grid(row=0, column=0, padx=10, pady=10)

        self.resetBtn = tk.Button(self.btnFrame, text="Reset", font=self.formFont, command=self.resetForm,width=12,bg=self.primarycolor,fg=self.txtcolor,relief="raised")
        self.resetBtn.grid(row=0, column=1, padx=10, pady=10)

        self.root.mainloop()

    def update_cities(self, event):
        selected_state = self.state_combobox.get()
        cities = self.states.get(selected_state, [])
        self.city_combobox['values'] = cities
        self.city_combobox.set("Select city")

    def resetForm(self):
        self.state_combobox.set("Select state")
        self.city_combobox.set("Select city")

    def getFormValues(self):
        self.state = self.state_combobox.get()
        self.city = self.city_combobox.get()

        if self.state == 'Select state' or self.city == 'Select city':
            msg.showwarning("Warning", "Please Enter Values.", parent=self.root)
        else:
            self.conn = Connect()
            self.cr = self.conn.cursor()
            q = f"insert into location (state, city) values ('{self.state}', '{self.city}')"
            self.cr.execute(q)
            self.conn.commit()
            self.conn.close()
            msg.showinfo('Success', 'location has been Added', parent=self.root)
            self.resetForm()


if __name__ == "__main__":
    obj = Main()