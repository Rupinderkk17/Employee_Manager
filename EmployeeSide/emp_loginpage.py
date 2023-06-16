from tkinter import *
#import task_database
from tkinter import messagebox
import emp_database, emp_dashboard

class emp_loginpage:
    def __init__(self):
        self.t = Tk()
        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 550) / 2) - 32

        center_window_geometry = "1000x550+" + str(self.width) + "+" + str(self.height)

        self.t.geometry(center_window_geometry)

        self.t.title("Emoplyee Login Page")

    def mainframe(self):

        self.f = Frame(self.t, bg="#f03b4f", width="500", height="550")
        self.f.place(x=0, y=0)

        self.f1 = Frame(self.t, bg="White", width="1100", height="550")
        self.f1.place(x=500, y=0)

        self.img = PhotoImage(file="images/login_background.png")
        self.label_image = Label(self.f1, image=self.img)
        self.label_image.place(x=0, y=0)

        self.l = Label(self.f, text="EMAIL", font=("Calibri", 18, "bold"), bg="#f03b4f", fg="white")
        self.l.place(x=50, y=180)

        self.e = Entry(self.f)
        self.e.place(x=50, y=230, width="390", height="25")

        self.l1 = Label(self.f, text="PASSWORD", font=("Calibri", 18, "bold"), bg="#f03b4f", fg="white")
        self.l1.place(x=50, y=270)

        self.e1 = Entry(self.f, show="*")
        self.e1.place(x=50, y=320, width="390", height="25")

        self.b = Button(self.f, text="LOGIN", bg="#132330", fg="White", command=self.opendashboard)
        self.b.place(x=50, y=380, width="390", height="25")

        self.l.mainloop()

    def opendashboard(self):
        if self.e.get() == "":
            messagebox.showinfo("Alert", "Please enter email first.")
        elif self.e1.get() == "":
            messagebox.showinfo("Alert", "Please enter password first.")
        else:
            email = self.e.get()
            password = self.e1.get()
            print("EMAIL - ", email, "PASSWORD", password)

            data = (email, password)
            print(data)

            result = emp_database.loginuser(data)
            if result:
                messagebox.showinfo("Message", "Login Successfully")
                self.t.destroy()
                a = emp_dashboard.Dashboard()
                a.mainframe(email)
            else:
                messagebox.showwarning("Alert", "Wrong Email or Password")


if __name__ == "__main__":
    s = emp_loginpage()
    s.mainframe()
