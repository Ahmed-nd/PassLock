import tkinter as tk
import webbrowser
from tkinter import filedialog, Menu
from tkinter import messagebox
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("1000x700")
        self.master.resizable(1, 1)
        # self.master.state('zoomed')
        # background
        # Add image file
        # self.bg = tk.PhotoImage(file="images/app.png")
        # bg_label2 = tk.Label(image=self.bg)
        # bg_label2.place(x=-2, y=-2)
        self.menu_bar = tk.Menu()

        self.file_menu_items = tk.Menu(self.menu_bar, tearoff=0)

        self.file_menu_items.add_command(label="All Items", command=self.open_file)
        self.file_menu_items.add_command(label="Settings...", command=self.open_file)
        self.file_menu_items.add_separator()

        self.file_menu_items.add_command(label="Exit", command=self.master.destroy)

        self.tools_menu_items = tk.Menu(self.menu_bar, tearoff=0)

        self.tools_menu_items.add_command(label="Auto Fill", command=self.open_tools)
        self.tools_menu_items.add_command(label="Generate Password", command=self.open_tools)

        self.help_menu_items = tk.Menu(self.menu_bar, tearoff=0)

        intro_url = "https://github.com/Ahmed-nd/PassLock#introduction"
        self.help_menu_items.add_command(label="Introduction", command=lambda link=intro_url: self.open_url(link))
        self.help_menu_items.add_separator()
        updates_url = "https://github.com/Ahmed-nd/PassLock#download"
        self.help_menu_items.add_command(label="Check for Updates...",
                                         command=lambda link=updates_url: self.open_url(link))
        license_url = "https://github.com/Ahmed-nd/PassLock#license"
        self.help_menu_items.add_command(label="License", command=lambda link=license_url: self.open_url(link))
        self.help_menu_items.add_separator()

        about_url = "https://github.com/Ahmed-nd/PassLock#developers"
        self.help_menu_items.add_command(label="About", command=lambda link=about_url: self.open_url(link))

        self.menu_bar.add_cascade(label="File", menu=self.file_menu_items)
        self.menu_bar.add_cascade(label="Tools", menu=self.tools_menu_items)
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu_items)

        self.master.config(menu=self.menu_bar)

        self.img = tk.PhotoImage(file="images/btn add folder hover.png")
        self.btn_add_folder = tk.Button(image=self.img, width=279, command=self.add_folder,
                                        height=40, border="0")
        self.btn_add_folder.pack(side="bottom", pady=100)

        self.btn_add_folder.bind("<ButtonPress>", self.btn_add_folder_press)
        self.btn_add_folder.bind("<ButtonRelease>", self.btn_add_folder_release)

    # Function Backend

    # Program UI
    def open_file(self):
        filename = filedialog.askopenfilename(initialdir="C:/Users/ahmed/OneDrive/Desktop/", title="Open File",
                                              filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        print("File Open" + filename)

    def open_tools(self):
        print("Tools Open")

    def add_folder(self):
        print("Add folder")

    def btn_add_folder_press(self, _):
        self.img = tk.PhotoImage(file="images/btn add folder.png")
        self.btn_add_folder.config(image=self.img)

    def btn_add_folder_release(self, _):
        self.img = tk.PhotoImage(file="images/btn add folder hover.png")
        self.btn_add_folder.config(image=self.img)

    @staticmethod
    def exit_program(self):
        self.exit()

    @staticmethod
    def open_url(self):
        print("Open Url : " + self)
        webbrowser.open_new(self)


if __name__ == "__main__":
    # Create object
    form = tk.Tk()
    app = Application(form)
    # Adjust size
    form.mainloop()
