from tkinter import *
from tkinter import messagebox
import database
import showemployee


class Employee:
    def __init__(self):
        self.t = Toplevel()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 500) / 2) - 20

        center_window_geometry = "1000x500+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)

        self.t.geometry(center_window_geometry)

    def mainframe(self, data=''):

        self.f = Frame(self.t, bg="#0b343e", width="500", height="600")
        self.f.place(x=0, y=0)

        self.f1 = Frame(self.t, bg="#0b343e", width="500", height="600")
        self.f1.place(x=500, y=0)

        self.img = PhotoImage(file="images/picture.png")
        self.label_image = Label(self.f1, image=self.img, width=500, height=500)
        self.label_image.place(x=0, y=0)

        self.l = Label(self.f, text="ADD EMPLOYEE", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l.place(x=125, y=30)

        self.l = Label(self.f, text="EMPLOYEE NAME", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l.place(x=10, y=80)

        self.employee_name_entry_box = Entry(self.f)
        self.employee_name_entry_box.place(x=250, y=80, width="150", height="25")

        self.l1 = Label(self.f, text="PHONE NUMBER", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l1.place(x=10, y=120)

        self.phone_entry_box = Entry(self.f)
        self.phone_entry_box.place(x=250, y=120, width="150", height="25")

        self.l2 = Label(self.f, text="ADDRESS", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l2.place(x=10, y=160)

        self.address_entry_box = Entry(self.f)
        self.address_entry_box.place(x=250, y=160, width="150", height="25")

        self.l3 = Label(self.f, text="EMAIL", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l3.place(x=10, y=200)

        self.email_entry_box = Entry(self.f)
        self.email_entry_box.place(x=250, y=200, width="150", height="25")

        self.l4 = Label(self.f, text="DESIGNATION", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l4.place(x=10, y=240)

        self.designation_entry_box = Entry(self.f)
        self.designation_entry_box.place(x=250, y=240, width="150", height="25")

        if data == "":
            self.l4 = Label(self.f, text="PASSWORD", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
            self.l4.place(x=10, y=280)

            self.password_entry_box = Entry(self.f)
            self.password_entry_box.place(x=250, y=280, width="150", height="25")

        self.l5 = Label(self.f, text="GENDER", font=("Calibri", 18, "bold"), bg="#0b343e", fg="white")
        self.l5.place(x=10, y=320)

        self.radioData = StringVar()
        self.male_radio = Radiobutton(self.f, text="Male", variable=self.radioData, value="Male")
        self.male_radio.place(x=250, y=320)

        self.female_radio = Radiobutton(self.f, text="Female", variable=self.radioData, value="Female")
        self.female_radio.place(x=330, y=320)

        if data == '':
            self.b = Button(self.f, text="Submit", bg="#ed5344", fg="White", command=self.addemployee)
            self.b.place(x=130, y=380, width="200", height="25")
        else:
            self.l = Label(self.f, text="Employee Id", font=("Calibri", 18, "bold"), bg="#535c68", fg="white")
            self.l.place(x=10, y=360)

            self.employee_id_entry_box = Entry(self.f)
            self.employee_id_entry_box.place(x=200, y=320, width="150", height="25")

            print(data.get('values'))
            result = data.get('values')
            sid = data.get('text')
            print(sid)
            self.employee_name_entry_box.insert(0, result[0])
            self.phone_entry_box.insert(1, result[1])
            self.address_entry_box.insert(2, result[2])
            self.email_entry_box.insert(3, result[3])
            self.designation_entry_box.insert(4, result[4])
            self.employee_id_entry_box.insert(0, sid)
            self.b = Button(self.f, text="Update", bg="Brown", fg="White", command=self.updateemployee)
            self.b.place(x=100, y=420, width="200", height="25")

        self.t.mainloop()

    def addemployee(self):
        name = self.employee_name_entry_box.get()
        phone_number = self.phone_entry_box.get()
        address = self.address_entry_box.get()
        email = self.email_entry_box.get()
        designation = self.designation_entry_box.get()
        gender = self.radioData.get()
        password = self.password_entry_box.get()

        data = (name, phone_number, address, email, designation, gender, password)
        print("Employee data - ", data)

        result = database.insertemployee(data)
        if result:
            messagebox.showinfo("Message", "Employee Data Update Successfully")
            self.t.destroy()
            s = showemployee.ShowEmployee()
            s.mainframe()
        else:
            messagebox.showwarning("Alert", "Error")

    def updateemployee(self):
        name = self.employee_name_entry_box.get()
        phone_number = self.phone_entry_box.get()
        address = self.address_entry_box.get()
        email = self.email_entry_box.get()
        designation = self.designation_entry_box.get()
        gender = self.radioData.get()
        eid = self.employee_id_entry_box.get()

        data = (name, phone_number, address, email, designation, gender, eid)
        print("Update employee data - ", data)

        result = database.updateemployee(data)
        if result:
            messagebox.showinfo("Message", "Employee Data Update Successfully")
            self.t.destroy()
            s = showemployee.ShowEmployee()
            s.mainframe()
        else:
            messagebox.showwarning("Alert", "Error")


if __name__ == '__main__':
    e = Employee()
    e.mainframe()
