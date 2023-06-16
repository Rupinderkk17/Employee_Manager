from tkinter import *
from tkinter.ttk import Treeview
import database, addemployee
from tkinter import messagebox
from tkinter.ttk import Combobox


class CompletedTask:
    def __init__(self):
        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 500) / 2) - 32

        center_window_geometry = "1000x500+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)
        self.t.geometry(center_window_geometry)

        self.t.title("Completed Task Details")

    def mainframe(self):
        self.f = Frame(self.t, bg="#5472a4", width="1000", height="500")
        self.f.place(x=0, y=0)

        employees_list = []

        data = database.showemployee()
        print("Data - ", data)
        for i in data:
            print("Employee Data - ", i[4])
            employees_list.append(i[4])

        self.l1 = Label(self.t, text="EMPLOYEES LIST", bg="white", fg="black")
        self.l1.place(x=300, y=50, width="100", height="30")

        self.c = Combobox(self.t, values=employees_list, state="readonly")
        self.c.place(x=500, y=50, height="30")
        self.c.bind("<<ComboboxSelected>>", self.getData)

        self.tr = Treeview(self.f, columns=('A', 'B', 'C', 'D', 'E', 'F'))
        self.tr.heading('#0', text="Id")
        self.tr.column('#0', width="50")
        self.tr.heading('#1', text="TASK NAME")
        self.tr.column('#1', width="150")
        self.tr.heading('#2', text='TASK DESCRIPTION')
        self.tr.column('#2', width="150")
        self.tr.heading('#3', text='START DATE')
        self.tr.column('#3', width="150")
        self.tr.heading('#4', text='LAST DATE')
        self.tr.column('#4', width="100")
        self.tr.heading('#5', text='STATUS')
        self.tr.column('#5', width="100")

        self.tr.place(x=50, y=100)

    def getData(self, e):
        for t in self.tr.get_children():
            self.tr.delete(t)

        # Get the selected email from the combobox widget with the help of event
        print("Employee Email ", e.widget.get())
        employee_email = e.widget.get()

        for i in database.showpendingtask(employee_email, "COMPLETED"):
            print(i)
            self.tr.insert('', 'end', text=i[0], values=(i[1], i[2], i[3], i[4], 'COMPLETED'))


if __name__ == '__main__':
    c = CompletedTask()
    c.mainframe()
    c.t.mainloop()
