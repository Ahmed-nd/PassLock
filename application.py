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

        self.file_menu_items.add_command(label="All Items", command=self.open_tools)
        self.file_menu_items.add_command(label="Settings...", command=self.open_tools)
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

        # ---------------------------frame left
        self.frame_left = tk.Frame(self.master, bg="antique white", relief="groove", borderwidth=5, padx=30, pady=30)
        self.frame_left.pack(side="left", fill='both', anchor='c')
        # ---------------------------frame right
        self.frame_right = tk.Frame(self.master, bg="floral white", relief="groove", borderwidth=5)
        self.frame_right.pack(side="left", expand='true', fill='both', anchor='c')
        # ---------------------------frame1 space-----------------------------
        self.frame_right_inner0 = tk.Frame(self.frame_right, bg="floral white", borderwidth=0)
        self.frame_right_inner0.pack(side="top", expand='true')
        # ---------------------------frame1
        self.frame_right_inner1 = tk.Frame(self.frame_right, bg="floral white", borderwidth=0, padx=22)
        self.frame_right_inner1.pack(side="top", fill='both', anchor='c')
        # ---------------------------frame2
        self.frame_right_inner2 = tk.Frame(self.frame_right, bg="lemon chiffon", relief="ridge", borderwidth=4,
                                           padx=30, pady=30)
        self.frame_right_inner2.pack(side="top", expand='true')
        # ------------------------------Scroll bar
        self.scrollbar = tk.Scrollbar(self.frame_right_inner2, orient="vertical")
        self.scrollbar.pack(side="right", fill='y')
        self.frame_right_inner2.pack(side="top", expand='true', fill='both', anchor='c', padx=20)
        # ---------------------------frame2 space-------------------------------
        self.frame_right_inner3 = tk.Frame(self.frame_right, bg="floral white", borderwidth=0)
        self.frame_right_inner3.pack(side="bottom", expand='true')

        # ------------------------------left
        btn_enter = tk.Button(self.frame_left, text="All items", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Auto Fill", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=1, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Generate\nPassword", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=2, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Setting", font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=3, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="About", command=lambda link=about_url: self.open_url(link)
                              , font="Arial 10 bold", border=0,
                              bg="antique white", activebackground='antique white')
        btn_enter.grid(row=4, column=0, columnspan=2, sticky='n', pady=10)
        # ------------------------------right
        # ------------------------------Add folder btn
        btn_enter = tk.Button(self.frame_right_inner1, text="+", font="Arial 12 bold", border=2, width=2,
                              relief='groove', bg="lawn green", activebackground='green2',
                              command=self.add_folder)
        btn_enter.grid(row=0, column=0)
        btn_enter = tk.Button(self.frame_right_inner1, text="-", font="Arial 12 bold", relief='groove',
                              border=2, width=2, fg='white', bg="red", activebackground='red2',
                              activeforeground='white', state='normal', command=self.remove_folder)
        btn_enter.grid(row=0, column=1)

        # self.frame_right_inner2['yscrollcommand'] = scrollbar.set

    # Function Backend
    def open_tools(self):
        print("Tools Open")

    def add_folder(self):
        print("Add folder")
        tmp_frame = tk.Frame(self.frame_right_inner2, bg="lemon chiffon", relief="ridge", border=2,
                             padx=30, pady=10, height=10)
        tmp_frame.pack(side="top", fill='both', anchor='c')
        number = tk.Label(tmp_frame, text='0', border=2, width=5, font="Arial 12 bold", relief='groove')
        number.grid(row=0, column=0)
        btn_enter = tk.Button(tmp_frame, text="Ahmed Nasser", font="Arial 12 bold", relief='groove',
                              border=2, width=30, bg="antique white", activebackground='antique white', anchor='w',
                              activeforeground='black', state='normal')
        btn_enter.grid(row=0, column=1)

    def remove_folder(self):
        print("remove folder")

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
