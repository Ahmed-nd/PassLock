import os
import tkinter as tk
from tkinter import messagebox


class Signup(tk.Frame):
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
        self.new_password_label = tk.Label(text="     New password", font="Sans 13", bg="#0001e6")
        self.new_password_entry = tk.Entry(width=25, show="*")

        self.confirm_label = tk.Label(text="Confirm password", font="Sans 13", bg="#0001e6")
        self.confirm_entry = tk.Entry(width=25, show="*")

        self.new_password_label.place(x=180, y=350, width=130, height=21)
        self.new_password_entry.place(x=320, y=350, width=200, height=21)

        self.confirm_label.place(x=180, y=380, width=130, height=21)
        self.confirm_entry.place(x=320, y=380, width=200, height=21)

        self.btn_enter = tk.Button(text="Enter", font="Sans 10 bold", width=10,
                                   command=self.change, bg="#0001a7", fg="white")
        self.btn_enter.place(x=350, y=430, height=25)

    def change(self):
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
