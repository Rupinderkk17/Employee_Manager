import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import emp_pendingtask, emp_completedtask, emp_loginpage

class Dashboard:
    def __init__(self):
        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 550) / 2) - 32

        center_window_geometry = "1000x550+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)
        self.t.geometry(center_window_geometry)

        self.t.title("Task Management | Dashboard Page")

    def mainframe(self, email):

        self.email = email
        print("value of email is ", self.email)

        self.f = Frame(self.t, bg="#2cac95", width="500", height="550")
        self.f.place(x=0, y=0)

        self.f1 = Frame(self.t, bg="White", width="1000", height="550")
        self.f1.place(x=500, y=0)

        self.img = PhotoImage(file="images/image (6).png")
        self.label_image = Label(self.f1, image=self.img)
        self.label_image.place(x=0, y=0)

        self.b = Button(self.f, text="PENDING TASK", command=self.pending_task_emp, bg="#2d2d60", fg="White")
        self.b.place(x=20, y=150, width="250", height="50")

        self.b = Button(self.f, text="COMPLETED TASKS", command=self.completed_task_emp , bg="#2d2d60", fg="White")
        self.b.place(x=360, y=150, width="250", height="50")

        self.b = Button(self.f, text="LOG OUT", command=self.open_show_login_page, bg="#2d2d60", fg="White")
        self.b.place(x=360, y=450, width="250", height="50")

        self.t.mainloop()

    def pending_task_emp(self):
        obj = emp_pendingtask.PendingTask()
        obj.mainframe(self.email)
        obj.getData()

    def completed_task_emp(self):
        obj = emp_completedtask.CompletedTask()
        obj.mainframe(self.email)
        obj.getData()

    def open_show_login_page(self):
        self.t.destroy()
        obj = emp_loginpage.emp_loginpage()
        obj.mainframe()


if __name__ == "__main__":
    s = Dashboard()
    s.mainframe(email="")
