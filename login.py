import os
import tkinter as tk
from tkinter import messagebox


class Login(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("800x600")
        self.master.resizable(0, 0)
        # background
        # Add image file
        self.bg = tk.PhotoImage(file="images/login-page.png")
        bg_label2 = tk.Label(image=self.bg)
        bg_label2.place(x=-2, y=-2)

        # Program UI
        self.password_label = tk.Label(text="Password", font="Sans 13", bg="#0001e6")
        self.password_entry = tk.Entry(width=25, show="*")

        self.password_label.place(x=180, y=350, width=180, height=21)
        self.password_entry.place(x=320, y=350, width=200, height=21)

        self.btn_reset_pass = tk.Button(text="Reset Password", font="Sans 12 bold", bg='#0001e6',
                                        fg="white",
                                        command=self.change_reset, activebackground='#0001e6', activeforeground="white",
                                        border="0")
        self.btn_reset_pass.place(x=500, y=400)

        self.btn_enter = tk.Button(text="Enter", font="Sans 10 bold", width=10, fg="white",
                                   bg="#0001a7",
                                   command=self.change_app, activebackground='#0001c6', activeforeground="white")
        self.btn_enter.place(x=350, y=400, height=30)

    def change_app(self):
        self.master.destroy()
        os.system('python application.py')

    def change_reset(self):
        self.master.destroy()
        os.system('python reset_password.py')


if __name__ == "__main__":
    form = tk.Tk()
    app = Login(form)
    # Adjust size
    form.mainloop()
