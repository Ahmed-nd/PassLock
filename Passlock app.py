# Import module 
import tkinter as tk
import webbrowser
from tkinter import filedialog, Menu
from tkinter import messagebox
from tkinter import ttk


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/btn exit.png')
        self.master.title("PassLock")
        self.master.geometry("800x600")

        def signup(self_signup):

            self_signup.master.resizable(0, 0)
            # background
            # Add image file
            self_signup.master.bg = tk.PhotoImage(file="images/login-page.png")
            bg_label2 = tk.Label(image=self_signup.master.bg)
            bg_label2.place(x=-2, y=-2)

            # Function Backend
            def change():
                new_password = new_password_entry.get()
                confirm = confirm_entry.get()
                if len(new_password) == 0:
                    messagebox.showerror("Error", "Enter your password")
                elif new_password == confirm and len(new_password) >= 8:
                    # store the new password in Database

                    btn_enter.destroy()
                    confirm_entry.destroy()
                    confirm_label.destroy()
                    new_password_entry.destroy()
                    new_password_label.destroy()
                    # bgLabel.destroy()
                    return login(self_signup)
                elif new_password == confirm and len(new_password) < 8:
                    messagebox.showerror("Error", "Your password is less than 8 characters")
                else:
                    messagebox.showerror("Error", "Your password and confirmation password do not match")

            # Program UI
            new_password_label = tk.Label(text="New password", font="Sans 13", bg="#0001e6")
            new_password_entry = tk.Entry(width=25, show="*")

            confirm_label = tk.Label(text="Confirm password", font="Sans 13", bg="#0001e6")
            confirm_entry = tk.Entry(width=25, show="*")

            new_password_label.place(x=180, y=350, width=130, height=21)
            new_password_entry.place(x=320, y=350, width=200, height=21)

            confirm_label.place(x=180, y=380, width=130, height=21)
            confirm_entry.place(x=320, y=380, width=200, height=21)

            btn_enter = tk.Button(text="Enter", font="Sans 10 bold", width=10,
                                  command=change, bg="#0001a7", fg="white")
            btn_enter.place(x=350, y=430, height=25)

        def login(self_login):

            self_login.master.resizable(0, 0)
            # background
            # Add image file
            self_login.master.bg = tk.PhotoImage(file="images/login-page.png")
            bg_label2 = tk.Label(image=self_login.master.bg)
            bg_label2.place(x=-2, y=-2)

            # Function Backend
            def change_app():
                password_label.destroy()
                password_entry.destroy()
                btn_enter.destroy()
                btn_reset_pass.destroy()
                return application(self_login)

            def change_reset():
                print("Reset password")
                password_label.destroy()
                password_entry.destroy()
                btn_enter.destroy()
                btn_reset_pass.destroy()
                return reset_pass(self_login)

            # Program UI
            password_label = tk.Label(text="Password", font="Sans 13", bg="#0001e6")
            password_entry = tk.Entry(width=25, show="*")

            password_label.place(x=180, y=350, width=180, height=21)
            password_entry.place(x=320, y=350, width=200, height=21)

            btn_reset_pass = tk.Button(text="Reset Password", font="Sans 12 bold", bg='#0001e6', fg="white",
                                       command=change_reset, activebackground='#0001e6', activeforeground="white",
                                       border="0")
            btn_reset_pass.place(x=500, y=400)

            btn_enter = tk.Button(text="Enter", font="Sans 10 bold", width=10,
                                  command=change_app, fg="white", bg="#0001a7")
            btn_enter.place(x=350, y=400, height=25)

        def reset_pass(self_reset):

            self_reset.master.resizable(0, 0)
            # background
            # Add image file
            self_reset.master.bg = tk.PhotoImage(file="images/reset password page.png")
            bg_label3 = tk.Label(image=self_reset.master.bg)
            bg_label3.place(x=-2, y=-2)

            # Function Backend
            def change():
                new_password = new_password_entry.get()
                confirm = confirm_entry.get()
                if len(new_password) == 0:
                    messagebox.showerror("Error", "Enter your password")
                elif new_password == confirm and len(new_password) >= 8:
                    # store the new password in Database

                    btn_enter.destroy()
                    confirm_entry.destroy()
                    confirm_label.destroy()
                    new_password_entry.destroy()
                    new_password_label.destroy()
                    key_label.destroy()
                    key_entry.destroy()
                    # bgLabel.destroy()
                    return login(self_reset)
                elif new_password == confirm and len(new_password) < 8:
                    messagebox.showerror("Error", "Your password is less than 8 characters")
                else:
                    messagebox.showerror("Error", "Your password and confirmation password do not match")

            # Program UI

            key_label = tk.Label(text="Key", font="Sans 13", bg="#0001e6")
            key_entry = tk.Entry(width=30)

            new_password_label = tk.Label(text="New password", font="Sans 13", bg="#0001e6")
            new_password_entry = tk.Entry(width=25, show="*")

            confirm_label = tk.Label(text="Confirm password", font="Sans 13", bg="#0001e6")
            confirm_entry = tk.Entry(width=25, show="*")

            # n, e, s, w, ne, se, sw, nw
            key_label.place(x=180, y=320, width=130, height=21)
            key_entry.place(x=320, y=320, width=200, height=21)

            new_password_label.place(x=180, y=350, width=130, height=21)
            new_password_entry.place(x=320, y=350, width=200, height=21)

            confirm_label.place(x=180, y=380, width=130, height=21)
            confirm_entry.place(x=320, y=380, width=200, height=21)

            btn_enter = tk.Button(text="Enter", font="Sans 10 bold", width=10,
                                  command=change, bg="#0001a7", fg="white")
            btn_enter.place(x=350, y=430, height=25)

        def application(self_app):

            self_app.master.resizable(1, 1)
            self_app.master.geometry("800x600")
            # self_app.master.state('zoomed')
            # background
            # Add image file
            self_app.master.bg = tk.PhotoImage(file="images/app.png")
            bg_label2 = tk.Label(image=self_app.master.bg)
            bg_label2.place(x=-2, y=-2)

            # Function Backend

            # Program UI
            def open_file():
                filename = filedialog.askopenfilename(initialdir="C:/Users/ahmed/OneDrive/Desktop/", title="Open File",
                                                      filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
                print("File Open" + filename)

            def open_tools():
                print("Tools Open")

            def add_folder():
                print("Add folder")

            def btn_add_folder_press(_):
                self_app.master.img = tk.PhotoImage(file="images/btn add folder.png")
                btn_add_folder.config(image=self_app.master.img)

            def btn_add_folder_release(_):
                self_app.master.img = tk.PhotoImage(file="images/btn add folder hover.png")
                btn_add_folder.config(image=self_app.master.img)

            menu_bar: Menu = tk.Menu()

            file_menu_items = tk.Menu(menu_bar, tearoff=0)

            file_menu_items.add_command(label="All Items", command=open_file)
            file_menu_items.add_command(label="Settings...", command=open_file)
            file_menu_items.add_separator()

            file_menu_items.add_command(label="Exit", command=self_app.master.destroy)

            tools_menu_items = tk.Menu(menu_bar, tearoff=0)

            tools_menu_items.add_command(label="Auto Fill", command=open_tools)
            tools_menu_items.add_command(label="Generate Password", command=open_tools)

            help_menu_items = tk.Menu(menu_bar, tearoff=0)

            intro_url = "https://github.com/Ahmed-nd/PassLock#introduction"
            help_menu_items.add_command(label="Introduction", command=lambda link=intro_url: self.open_url(link))
            help_menu_items.add_separator()
            updates_url = "https://github.com/Ahmed-nd/PassLock#download"
            help_menu_items.add_command(label="Check for Updates...",
                                        command=lambda link=updates_url: self.open_url(link))
            license_url = "https://github.com/Ahmed-nd/PassLock#license"
            help_menu_items.add_command(label="License", command=lambda link=license_url: self.open_url(link))
            help_menu_items.add_separator()

            about_url = "https://github.com/Ahmed-nd/PassLock#developers"
            help_menu_items.add_command(label="About", command=lambda link=about_url: self.open_url(link))

            menu_bar.add_cascade(label="File", menu=file_menu_items)
            menu_bar.add_cascade(label="Tools", menu=tools_menu_items)
            menu_bar.add_cascade(label="Help", menu=help_menu_items)

            self_app.master.config(menu=menu_bar)

            self_app.master.img = tk.PhotoImage(file="images/btn add folder hover.png")
            btn_add_folder = tk.Button(image=self_app.master.img, width=279, command=add_folder,
                                       height=40, border="0")
            btn_add_folder.pack(side="bottom", pady=100)

            btn_add_folder.bind("<ButtonPress>", btn_add_folder_press)
            btn_add_folder.bind("<ButtonRelease>", btn_add_folder_release)

        login(self)
        # signup(self)

    @staticmethod
    def exit_program(self):
        self.exit()

    @staticmethod
    def open_url(self):
        print("Open Url : " + self)
        webbrowser.open_new(self)


if __name__ == "__main__":
    # Create object
    app = Window(tk.Tk())

    # Adjust size
    app.mainloop()
"""
Label(anchor="n, e, s, w, ne, se, sw, nw", bg="color", bitmap,
bd, cursor, font, fg="color", height, image, justify="left, right, center",
padx, pady, text, textvariable, underline, width, wraplength)
"""
"""
Entry(relief="raised, flat, groove, ridge, sunken")."get, insert(0, String)"
"""
"""
Button(command)
"""
"""
grid(row, column, columnspan)
"""
"""
pack(side = "top, bottom, left, or right")
"""
"""
        # Menu
        menuBar = tk.Menu(self.master)
        
        fileMenuItems = tk.Menu(menuBar, tearoff=0)
        
        fileMenuItems.add_command(label="Open", command=self.openfile)
        fileMenuItems.add_command(label="Save", command=self.openfile)
        fileMenuItems.add_separator()
        fileMenuItems.add_command(label="Quit", command=self.exitProgram)
        
        editMenuItems = tk.Menu(menuBar, tearoff=0)
        editMenuItems.add_command(label="Cut", command=self.openedit)
        editMenuItems.add_command(label="Copy", command=self.openedit)
        editMenuItems.add_command(label="Paste", command=self.openedit)
        
        
        menuBar.add_cascade(label="File", menu=fileMenuItems)
        menuBar.add_cascade(label="Edit", menu=editMenuItems)
        
        
        
        self.master.config(menu=menuBar)
"""
"""
        textArea = tk.Text(self.master, height=7, width=55, wrap=tk.WORD)
        textArea.configure(font=("Arial", 14))
        textArea.insert('1.0', 'Some default text here')
        textArea.place(x=75,y=350)
"""
