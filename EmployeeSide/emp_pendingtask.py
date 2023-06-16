from tkinter import *
from tkinter.ttk import Treeview

from tkinter.ttk import Combobox
import emp_database

class PendingTask:
    def __init__(self):
        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 500) / 2) - 32

        center_window_geometry = "1000x500+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)
        self.t.geometry(center_window_geometry)

        self.t.title("Pending Task Details Of Employee")
    def mainframe(self, email):

        self.email = email
        self.f = Frame(self.t,bg="#5472a4", width="1000", height="500")
        self.f.place(x=0, y=0)

        self.tr = Treeview(self.f, columns=('A', 'B', 'C', 'D', 'E', 'F'))
        self.tr.heading('#0', text="Id")
        self.tr.column('#0', width=50)
        self.tr.heading('#1', text="TASK NAME")
        self.tr.column('#1', width=150)
        self.tr.heading('#2', text='TASK DESCRIPTION')
        self.tr.column('#2', width=150)
        self.tr.heading('#3', text='START DATE')
        self.tr.column('#3', width=150)
        self.tr.heading('#4', text='LAST DATE')
        self.tr.column('#4', width=100)
        self.tr.heading('#5', text='STATUS')
        self.tr.column('#5', width=100)

        self.tr.place(x=50, y=150)

    def getData(self):
            for i in emp_database.showpendingtask(self.email, "PENDING"):
                print(i)
                self.tr.insert('', 'end', text=i[0], values=(i[1], i[2], i[3], i[4], 'PENDING'))


if __name__ == '__main__':
    p = PendingTask()
    p. mainframe(email="")
    p.t.mainloop()
