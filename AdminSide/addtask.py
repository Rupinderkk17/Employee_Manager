from tkinter import *
from tkinter import messagebox
import database
import showtask


class AddTask:
    def __init__(self):
        self.t = Toplevel()



        # Centralize the Window
        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 500) / 2) - 20

        center_window_geometry = "1000x500+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)

        self.t.geometry(center_window_geometry)
        self.t.title("Task Management | Add Task Here")

    def mainframe(self, data=""):
        self.f = Frame(self.t, bg="#3d4787", width="500", height="600")
        self.f.place(x=0, y=0)

        self.f1 = Frame(self.t, bg="White", width="500", height="600")
        self.f1.place(x=500, y=0)

        self.img = PhotoImage(file="images/task.png")
        self.label_image = Label(self.f1, image=self.img, width=500 ,height=500)
        self.label_image.place(x=0, y=0)

        self.l = Label(self.f, text="Task Name", bg="white", fg="black")
        self.l.place(x=100, y=120, width="100", height="30")

        self.e = Entry(self.f)
        self.e.place(x=210, y=120, width="250", height="30")

        self.l1 = Label(self.f, text="Task Description")
        self.l1.place(x=100, y=180, width="100", height="30")

        self.e1 = Entry(self.f)
        self.e1.place(x=210, y=180, width="250", height="30")

        if data == '':
            self.b = Button(self.f, text="SUBMIT", command=self.addtask)
            self.b.place(x=160, y=270, width="200", height="25")
        else:
            self.l3 = Label(self.f, text="User Id")
            self.l3.place(x=250, y=290, width="100", height="30")
            self.e4 = Entry(self.f)
            self.e4.place(x=550, y=300, width="250")

            print(data.get('values'))
            result = data.get('values')
            sid = data.get('text')

            self.e.insert(0, result[0])
            self.e1.insert(1, result[1])
            self.e4.insert(0, sid)
            self.b = Button(self.f, text="Update", command=self.updatetask)
            self.b.place(x=400, y=350, width="200", height="25")

        self.t.mainloop()

    def addtask(self):
        task_name = self.e.get()
        task_description = self.e1.get()
        print("task_name-", task_name, "task_description-", task_description)
        data = (task_name, task_description)

        result = database.inserttask(task_name, task_description)
        print(result)
        if result:
            messagebox.showinfo("Message", "Task added successfully")
            self.t.destroy()
            s = showtask.ShowTask()
            s.mainframe()
        else:
            messagebox.showwarning("Alert", "Please try again")

    def updatetask(self):
        task_name = self.e.get()
        task_description = self.e1.get()
        userid = self.e4.get()
        print("task_name-", task_name, "task_description-", task_description)

        data = (task_name, task_description, userid)

        result = database.update_task(data)
        if result:
            messagebox.showinfo("Message", "Task update successfully")
            self.t.destroy()
            s = showtask.ShowTask()
            s.mainframe()
        else:
            messagebox.showwarning("Alert", "Please try again")
            self.t.destroy()
            s = showtask.ShowTask()
            s.mainframe()


if __name__ == '__main__':
    s = AddTask()
    s.mainframe()
