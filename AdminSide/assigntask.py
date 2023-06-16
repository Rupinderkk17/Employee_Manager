from tkinter import *
from tkinter.ttk import Combobox
import database
from tkinter import messagebox


class AssignTask:
    def __init__(self):

        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 550) / 2) - 32

        center_window_geometry = "1000x550+" + str(self.width) + "+" + str(self.height)

        self.t.geometry(center_window_geometry)

        self.t.title("Task Management | Assigned Task")

    def mainframe(self):
        self.f = Frame(self.t, bg="sky blue", width="1000", height="550")
        self.f.place(x=0, y=0)

        self.imgpath = PhotoImage(file="images/addtask.png")
        self.limg = Label(self.f, image=self.imgpath, width=1000, height=550)
        self.limg.place(x=0, y=0)

        self.l = Label(self.f, text="SELECT TASK", bg="#e36d13", fg="black")
        self.l.place(x=120, y=170, width="150", height="30")

        self.l = Label(self.f, text="SELECT EMPLOYEE", bg="#e36d13", fg="black")
        self.l.place(x=120, y=220, width="150", height="30")

        self.l1 = Label(self.f, text="START DATE", bg="#e36d13", fg="black")
        self.l1.place(x=120, y=270, width="150", height="30")

        self.e1 = Entry(self.f)
        self.e1.place(x=340, y=270, width="150", height="30")

        self.l = Label(self.f, text="END DATE", bg="#e36d13", fg="black")
        self.l.place(x=120, y=320, width="150", height="30")

        self.e2 = Entry(self.f)
        self.e2.place(x=340, y=320, width="150", height="30")

        self.b = Button(self.f, text="ASSIGN TASK", bg="#3a3c58", fg="White", command=self.assigntask)
        self.b.place(x=230, y=390, width="150", height="30")

        self.data = []
        for i in database.showtasks():
            self.data.append(i[0])

        self.ctask = Combobox(self.t, values=self.data, state="readonly")
        self.ctask.place(x=340, y=170, width="150", height="30")

        self.edata = []
        for i in database.showemployee():
            self.edata.append(i[4])

        self.cemployee = Combobox(self.t, values=self.edata, state="readonly")
        self.cemployee.place(x=340, y=220, width="150", height="30")

        self.t.mainloop()

    def assigntask(self):
        taskId = self.ctask.get()
        employeeName = self.cemployee.get()
        start = self.e1.get()
        end = self.e2.get()

        result = database.assign_task("PENDING", employeeName, start, end, taskId)
        if result:
            messagebox.showinfo("Message", "Task Assign to the employee Successfully")
        else:
            messagebox.showwarning("Alert", "Please try again")


if __name__ == "__main__":
    a = AssignTask()
    a.mainframe()
