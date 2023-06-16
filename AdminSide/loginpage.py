from tkinter import *
import dashboard
import database
from tkinter import messagebox


class LoginPage:
    def __init__(self):
        self.t = Tk()

        self.fwidth = self.t.winfo_screenwidth()
        self.fheight = self.t.winfo_screenheight()

        self.width = int((self.fwidth - 1000) / 2)
        self.height = int((self.fheight - 600) / 2) - 32

        center_window_geometry = "1000x600+" + str(self.width) + "+" + str(self.height)
        print(center_window_geometry)

        self.t.geometry(center_window_geometry)
        self.t.title("Login Page")

    def mainframe(self, data=''):
        self.f = Frame(self.t, bg="#f03b4f", width="500", height="600")
        self.f.place(x=0, y=0)

        self.f1 = Frame(self.t, bg="White", width="500", height="600")
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

            result = database.loginuser(data)
            if result:
                messagebox.showinfo("Message", "Login Successfully")
                self.t.destroy()
                a = dashboard.DashBoard()
                a.mainframe()
            else:
                messagebox.showwarning("Alert", "Wrong Email or Password")


if __name__ == '__main__':
    l = LoginPage()
    l.mainframe()
    l.t.mainloop()
