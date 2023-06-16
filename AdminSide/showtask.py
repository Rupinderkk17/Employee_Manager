from tkinter import *
from tkinter.ttk import Treeview
import database
import addtask
from tkinter import messagebox


class ShowTask:
    def __init__(self):
        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 500) / 2) - 32

        center_window_geometry = "1000x500+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)
        self.t.geometry(center_window_geometry)

        self.t.title("Task Details | Task Management")

    def mainframe(self):
        self.f = Frame(self.t,bg="#5472a4", width="1000", height="500")
        self.f.place(x=0, y=0)

        self.tr = Treeview(self.f, columns=('A', 'B', 'C', 'D', 'E', 'F', 'G'))

        self.tr.heading('#0', text="Id")
        self.tr.column("#0", width=50, anchor=CENTER)

        self.tr.heading('#1', text="Task Name")
        self.tr.column("#1", width=200, anchor=CENTER)

        self.tr.heading('#2', text='Task description')
        self.tr.column("#2", width=200, anchor=CENTER)

        self.tr.heading('#3', text='Start Date')
        self.tr.column("#3", width=100, anchor=CENTER)

        self.tr.heading('#4', text='End date')
        self.tr.column("#4", width=100, anchor=CENTER)

        self.tr.heading('#5', text='Delete')
        self.tr.column("#5", width=100, anchor=CENTER)

        self.tr.heading('#6', text='Update')
        self.tr.column("#6", width=100, anchor=CENTER)

        for i in database.showtasks():
            print(i)
            self.tr.insert('', 'end', text=i[0], values=(i[1], i[2], i[3], i[4], 'Delete', 'Update'))

        self.tr.place(x=70, y=75, width="850", height="350")
        # Add the functionality of Double Click

        self.tr.bind('<Double-Button-1>', self.getData)

        self.t.mainloop()

    def getData(self, e):
        tt = self.tr.focus()
        print('Focused Row ', tt)

        col = self.tr.identify_column(e.x)
        print('Column Number ', col)
        print(self.tr.item(tt))
        gup = (
            self.tr.item(tt).get('text'),
        )
        print(' Id ', gup)

        if col == '#5':
            a = messagebox.askyesno('alert', 'Do you want to delete this data?')
            if a:
                result = database.deletetask(gup)
                if result:
                    messagebox.showinfo('Message', 'Student Deleted')
                    self.t.destroy()
                    s = ShowTask()
                    s.mainframe()
                else:
                    messagebox.showwarning('Alert', 'Please try again.')

        elif col == '#6':
            a = addtask.AddTask()
            a.mainframe(self.tr.item(tt))
            self.t.destroy()


if __name__ == '__main__':
    s = ShowTask()
    s.mainframe()
