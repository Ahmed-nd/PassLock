# tkinter/ ttk/ webbrowser
import tkinter as tk
import webbrowser
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


class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("800x600")
        self.master.destroy()
        os.system('python signup.py')
        # signup(self)

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
    app = Window(form)
    # Adjust size
    form.mainloop()
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
