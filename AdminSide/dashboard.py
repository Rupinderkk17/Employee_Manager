from tkinter import *
import addemployee
import database
import showemployee
import pendingtask
import completedtask, loginpage
import addtask, showtask
import assigntask


class DashBoard:
    def __init__(self):
        self.t = Tk()

        # Centralize the Window
        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1200) / 2)
        self.height = int((self.fheight - 650) / 2) - 32

        center_window_geometry = "1200x650+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)
        self.t.geometry(center_window_geometry)

        self.t.title("Task Management : DashBoard")

    def mainframe(self, data=''):
        self.f = Frame(self.t, bg="#535c68", width="1200", height="650")
        self.f.place(x=0, y=0)

        self.back_image = PhotoImage(file="images/admin.png")
        self.limg = Label(self.f, image=self.back_image, height=1200, width=1200)
        self.limg.place(x=0, y=0)

        self.b = Button(self.f, text="ADD TASK", bg="#2b468b", fg="White", command=self.openaddtask)
        self.b.place(x=270, y=160, width="300", height="75")

        self.b = Button(self.f, text="ADD EMPLOYEE", bg="#2b468b", fg="White", command=self.openaddemployee)
        self.b.place(x=270, y=240, width="300", height="75")

        self.b = Button(self.f, text="PENDING TASK", bg="#2b468b", fg="White", command=self.openpendingtask)
        self.b.place(x=270, y=320, width="300", height="75")

        self.b = Button(self.f, text="ASSIGN TASK", bg="#2b468b", fg="White", command=self.openassigntask)
        self.b.place(x=270, y=400, width="300", height="75")

        self.b = Button(self.f, text="SHOW TASK", bg="#2b468b", fg="White", command=self.openshowtask)
        self.b.place(x=660, y=160, width="300", height="75")

        self.b = Button(self.f, text="SHOW EMPLOYEE", bg="#2b468b", fg="White", command=self.openshowemployee)
        self.b.place(x=660, y=240, width="300", height="75")

        self.b = Button(self.f, text="COMPLETED TASK", bg="#2b468b", fg="White", command=self.opencompletedtask)
        self.b.place(x=660, y=320, width="300", height="75")

        self.b = Button(self.f, text="LOGOUT ", bg="#2b468b", fg="White", command=self.openloginscreen)
        self.b.place(x=660, y=400, width="300", height="75")

    def openaddemployee(self):
        a = addemployee.Employee()
        a.mainframe()

    def openshowemployee(self):
        b = showemployee.ShowEmployee()
        b.mainframe()

    def openpendingtask(self):
        c = pendingtask.PendingTask()
        c.mainframe()

    def opencompletedtask(self):
        d = completedtask.CompletedTask()
        d.mainframe()

    def openaddtask(self):
        e = addtask.AddTask()
        e.mainframe()

    def openshowtask(self):
        f = showtask.ShowTask()
        f.mainframe()

    def openassigntask(self):
        f = assigntask.AssignTask()
        f.mainframe()

    def openloginscreen(self):
        self.t.destroy()
        g = loginpage.LoginPage()
        g.mainframe()


if __name__ == '__main__':
    d = DashBoard()
    d.mainframe()
    d.t.mainloop()
