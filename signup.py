import os
import tkinter as tk
from tkinter import messagebox


class Signup(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("500x500")
        self.master.resizable(0, 0)
        # ---------------------------frame1
        self.frame1 = tk.Frame(self.master, bg="pale turquoise", relief="ridge")
        self.frame1.pack(side="top", expand='true', fill='both', anchor='c')
        # ---------------------------title label
        self.title_label = tk.Label(self.frame1, text="Sign up", font="Arial 18 bold", bg="pale turquoise")
        self.title_label.grid(row=1, column=0, columnspan=2, sticky='n', pady=40)
        # ---------------------------image
        # Add image file
        self.img = tk.PhotoImage(file="images/logo.png")
        # ---------------------------canvas
        self.canvas = tk.Canvas(self.frame1, height=110, bg="white", width=500)
        self.canvas.grid(row=0, column=0, columnspan=2)
        self.canvas.create_image(250, 60, image=self.img)
        # ---------------------------Program UI
        self.new_password_label = tk.Label(self.frame1, text="                             New password:",
                                           font="Arial 10 bold", bg="pale turquoise")
        self.new_password_entry = tk.Entry(self.frame1, width=25, show="*")

        self.confirm_label = tk.Label(self.frame1, text="                        Confirm password:",
                                      font="Arial 10 bold", bg="pale turquoise")
        self.confirm_entry = tk.Entry(self.frame1, width=25, show="*")

        self.new_password_label.grid(row=2, column=0, columnspan=2, sticky='w', pady=10)
        self.new_password_entry.grid(row=2, column=1, columnspan=2, sticky='e', pady=10, padx=130)

        self.confirm_label.grid(row=3, column=0, columnspan=2, sticky='w', pady=10)
        self.confirm_entry.grid(row=3, column=1, columnspan=2, sticky='e', pady=10, padx=130)

        self.btn_enter = tk.Button(self.frame1, text="Enter", font="Arial 10 bold", width=7,
                                   bg="#0001a7", fg='white', command=self.change,
                                   activeforeground='white', activebackground='#00dee1')
        self.btn_enter.grid(row=4, column=0, columnspan=2, pady=20)
        # -------------------------------Events
        self.master.bind('<Return>', self.change)

    def change(self, *_):
        new_password = self.new_password_entry.get()
        confirm = self.confirm_entry.get()
        if len(new_password) == 0:
            messagebox.showerror("Error", "Enter your password")
        elif new_password == confirm and len(new_password) >= 8:
            # store the new password in Database
            self.master.destroy()
            os.system('python login.py')
            # bgLabel.destroy()
            # return Login(self)
        elif new_password == confirm and len(new_password) < 8:
            messagebox.showerror("Error", "Your password is less than 8 characters")
        else:
            messagebox.showerror("Error", "Your password and confirmation password do not match")


if __name__ == "__main__":
    # Create object
    form = tk.Tk()
    app = Signup(form)
    # Adjust size
    form.mainloop()
