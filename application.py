import tkinter as tk
import webbrowser
from tkinter import scrolledtext
import os
from tkinter import filedialog, Menu
from tkinter import messagebox
from tkinter import ttk
# AES 256 encryption/decryption using pycryptodome library
from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
# pip install pycryptodomex
# pip install pycryptodome


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("1000x700")
        self.master.resizable(1, 1)
        self.master.configure(bg='floral white')
        # self.master.state('zoomed')
        # ------------------------------Menu
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
        # ---------------------------frame1
        # self.frame1 = tk.Frame(self.master, bg="lemon chiffon", relief="ridge", height=40, borderwidth=5)
        # self.frame1.pack(side="left", fill='both', anchor='c')
        # ---------------------------frame2
        self.frame1 = tk.Frame(self.master, bg="antique white", relief="ridge", borderwidth=5, padx=30, pady=30)
        self.frame1.pack(side="left", fill='both', anchor='c')
        # ---------------------------frame3
        self.frame2 = tk.Frame(self.master, bg="floral white", relief="ridge", borderwidth=5)
        self.frame2.pack(side="left", expand='true', fill='both', anchor='c')
        # ---------------------------Notebook

        # ---------------------------label
        # self.title_label = tk.Label(self.frame1, text="Sign up", font="Arial 18 bold", bg="pale turquoise")
        # self.title_label.grid(row=0, column=0, columnspan=2, sticky='n', pady=40)
        self.title_label = tk.Label(self.frame2, text="Sign up", font="Arial 18 bold", bg="pale turquoise")
        self.title_label.grid(row=0, column=0, columnspan=2, sticky='n', pady=40)
        self.title_label = tk.Label(self.frame2, text="Sign up", font="Arial 18 bold", bg="pale turquoise")
        self.title_label.grid(row=1, column=0, columnspan=2, sticky='n', pady=40)

        # ------------------------------left
        btn_enter = tk.Button(self.frame1, text="All items", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame1, text="Auto Fill", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=1, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame1, text="Generate\nPassword", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=2, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame1, text="Auto Fill", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=3, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame1, text="About", command=lambda link=about_url: self.open_url(link)
                              , font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=4, column=0, columnspan=2, sticky='n', pady=10)
        # ------------------------------right
        # ------------------------------Add folder btn
        self.img = tk.PhotoImage(file="images/btn add folder hover.png")
        self.btn_add_folder = tk.Button(self.frame2, image=self.img, width=279, command=self.add_folder,
                                        height=40, border="0", bg="floral white", activebackground='floral white')
        self.btn_add_folder.grid(row=2, column=1, columnspan=2, sticky='s', pady=10, padx=50)

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

    def encrypt(self, password):
        # generate a random salt
        salt = get_random_bytes(AES.block_size)

        # use the Scrypt KDF to get a private key from the password
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # create cipher config
        cipher_config = AES.new(private_key, AES.MODE_GCM)

        # return a dictionary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(str(self), 'utf-8'))
        return {
            'cipher_text': b64encode(cipher_text).decode('utf-8'),
            'salt': b64encode(salt).decode('utf-8'),
            'nonce': b64encode(cipher_config.nonce).decode('utf-8'),
            'tag': b64encode(tag).decode('utf-8')
        }

    def decrypt(self, password):
        # decode the dictionary entries from base64
        salt = b64decode(self['salt'])
        cipher_text = b64decode(self['cipher_text'])
        nonce = b64decode(self['nonce'])
        tag = b64decode(self['tag'])

        # generate the private key from the password and salt
        private_key = hashlib.scrypt(
            password.encode(), salt=salt, n=2 ** 14, r=8, p=1, dklen=32)

        # create the cipher config
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

        # decrypt the cipher text
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)

        return decrypted


if __name__ == "__main__":
    # Create object
    form = tk.Tk()
    app = Application(form)
    # Adjust size
    form.mainloop()
