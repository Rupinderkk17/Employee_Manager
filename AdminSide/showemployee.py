from tkinter import *
from tkinter.ttk import Treeview
import database, addemployee
from tkinter import messagebox


class ShowEmployee:
    def __init__(self):
        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1100) / 2)
        self.height = int((self.fheight - 500) / 2) - 32

        center_window_geometry = "1100x500+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)
        self.t.geometry(center_window_geometry)

        self.t.title("Employee Details")

    def mainframe(self):
        self.f = Frame(self.t, bg="#5472a4", width="1100", height="500")
        self.f.place(x=0, y=0)

        self.tr = Treeview(self.f, columns=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'))
        self.tr.heading('#0', text="Id")
        self.tr.column('#0', width="50",anchor=CENTER)
        self.tr.heading('#1', text="Employee Name")
        self.tr.column('#1', width="150")
        self.tr.heading('#2', text='P.No')
        self.tr.column('#2', width="150")
        self.tr.heading('#3', text='ADDRESS')
        self.tr.column('#3', width="150")
        self.tr.heading('#4', text='EMAIL')
        self.tr.column('#4', width="100")
        self.tr.heading('#5', text='DESIGNATION')
        self.tr.column('#5', width="100")
        self.tr.heading('#6', text='GENDER')
        self.tr.column('#6', width="100")
        self.tr.heading('#7', text='DELETE')
        self.tr.column('#7', width="100")
        self.tr.heading('#8', text='UPDATE')
        self.tr.column('#8', width="100")

        for i in database.showemployee():
            print(i)
            self.tr.insert('', 'end', text=i[0], values=(i[1], i[2], i[3], i[4], i[5], i[6], 'DELETE', 'UPDATE'))

        self.tr.place(x=60, y=100, width="1000")
        self.tr.bind('<Double-Button-1>', self.getData)

    def getData(self, e):
        fr = self.tr.focus()
        print('Focused Row ', fr)

        col = self.tr.identify_column(e.x)
        print('Column Number ', col)
        print(self.tr.item(fr))

        foc = (
            self.tr.item(fr).get('text'),
        )
        print('Employee Id ', foc)

        if col == '#7':
            a = messagebox.askyesno('Alert', 'Do you realy want to delete this data?')
            if a:
                result = database.deleteemployee(foc)
                if result:
                    messagebox.showinfo('Message', 'Employee data Deleted')
                    self.t.destroy()
                    s = ShowEmployee()
                    s.mainframe()
                else:
                    messagebox.showwarning('Alert', 'Error')

        elif col == '#8':
            a = addemployee.Employee()
            a.mainframe(self.tr.item(fr))
            self.t.destroy()


if __name__ == '__main__':
    s = ShowEmployee()
    s.mainframe()
    s.t.mainloop()
