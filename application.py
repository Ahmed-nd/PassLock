import tkinter as tk
import webbrowser
from tkinter import scrolledtext, END
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

        self.file_menu_items.add_command(label="All Items")
        self.file_menu_items.add_command(label="Settings...")
        self.file_menu_items.add_separator()

        self.file_menu_items.add_command(label="Exit", command=self.master.destroy)

        self.tools_menu_items = tk.Menu(self.menu_bar, tearoff=0)

        self.tools_menu_items.add_command(label="Auto Fill")
        self.tools_menu_items.add_command(label="Generate Password")

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
        self.frame_left = tk.Frame(self.master, bg="#00dee1", relief="groove", borderwidth=5, padx=30, pady=30)
        self.frame_left.pack(side="left", fill='both', anchor='c')
        # ---------------------------frame right
        self.frame_right = tk.Frame(self.master, bg="pale turquoise", relief="groove", borderwidth=5, pady=30)
        self.frame_right.pack(side="left", expand='true', fill='both', anchor='c')
        # ---------------------------Canvas right table
        self.canvas_right_table = tk.Canvas(self.frame_right, bg="floral white", relief="ridge",
                                            borderwidth=4)
        self.canvas_right_table.pack(side="top", fill='both', anchor='c', padx=30, expand='true')
        # ---------------------------Table
        self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')

        # ------------------------------left
        btn_enter = tk.Button(self.frame_left, text="All items", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Auto Fill", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=1, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Generate\nPassword", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=2, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Setting", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=3, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="About", command=lambda link=about_url: self.open_url(link)
                              , font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=4, column=0, columnspan=2, sticky='n', pady=10)
        # ------------------------------right

        # ---------------------------Table
        # take the data
        self.lst = [('Raj', 'View', 'Edit', 'Del'),
                    ('Aaryan', 'View', 'Edit', 'Del'),
                    ('Vaishnavi', 'View', 'Edit', 'Del'),
                    ('Rachna', 'View', 'Edit', 'Del'),
                    ('Shubham', 'View', 'Edit', 'Del')]
        self.lst_tk = []
        self.wid = [30, 10, 10, 10]
        self.folder_name = tk.StringVar()
        self.bg_color = ['light cyan', 'gold', 'royal blue', 'firebrick1']
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=self.add_new_folder)
        self.show_table()

    # Function Backend
    def show_table(self):
        del self.lst_tk
        self.lst_tk = []
        total_rows = len(self.lst)
        total_columns = len(self.lst[0])
        for i in range(total_rows):
            temp_tk = []
            e = tk.Label(self.tab1, text=(i + 1), width=5, bg='cyan',
                         font="Arial 12 bold", relief='groove')
            e.grid(row=i, column=0, padx=2, pady=2)
            temp_tk.append(e)
            for j in range(0, total_columns):
                if j == 0:
                    e = tk.Label(self.tab1, text=self.lst[i][j], width=self.wid[j], bg=self.bg_color[j],
                                 font="Arial 12 bold", relief='groove')
                else:
                    e = tk.Button(self.tab1, text=self.lst[i][j], width=self.wid[j], bg=self.bg_color[j],
                                  font="Arial 12 bold", activebackground='antique white',
                                  command=lambda row=i, column=j: self.table_tools(row, column))
                temp_tk.append(e)
                e.grid(row=i, column=j + 1, padx=2, pady=2)

            temp_tk = tuple(temp_tk)
            if total_rows == 1:
                temp_tk[4]['state'] = 'disable'
            self.lst_tk.append(temp_tk)

            # self.e.insert(END, lst[i][j])
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=self.add_new_folder)
        if total_rows == 12:
            self.btn_add['state'] = 'disable'
        self.btn_add.grid(row=total_rows - 1, column=total_columns + 1)

    def destroy_table(self):
        self.tab1.destroy()
        self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
        self.show_table()

    def table_tools(self, row, column):
        print(row, column)
        if column == 3:
            del self.lst[row]
            self.destroy_table()
        elif column == 2:
            del self.folder_name
            self.folder_name = tk.StringVar()

            def add():
                print("add")
                name = self.folder_name.get()
                if name != '':
                    t = list(self.lst[row])
                    t[0] = name
                    self.lst[row] = tuple(t)
                    self.destroy_table()
                else:
                    messagebox.showerror("Error", "Enter folder name")

            self.btn_add.destroy()
            self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                     relief='groove', bg="lawn green", activebackground='green2',
                                     command=add)
            self.btn_add.grid(row=row, column=5)
            folder_name_entry = tk.Entry(self.tab1, width=self.wid[0] + 3,
                                         font="Arial 12 bold", relief='groove',
                                         textvariable=self.folder_name)
            folder_name_entry.insert(0, self.lst[row][0])
            folder_name_entry.grid(row=row, column=1, padx=2, pady=2)

        elif column == 1:
            pass

    def add_new_folder(self):
        print("Add folder")
        total_rows = len(self.lst)
        del self.folder_name
        self.folder_name = tk.StringVar()

        def add():
            print("add")
            name = self.folder_name.get()
            if name != '':
                temp_lst = [name, self.lst[0][1], self.lst[0][2], self.lst[0][3]]
                temp_lst = tuple(temp_lst)
                self.lst.append(temp_lst)
                self.destroy_table()
            else:
                messagebox.showerror("PassLock", "Enter folder name")

        def back():
            print("remove folder")
            folder_name_label.destroy()
            folder_name_entry.destroy()
            self.btn_add.destroy()
            btn_remove.destroy()
            self.show_table()

        self.btn_add.destroy()

        folder_name_label = tk.Label(self.tab1, text="Name :", font="Arial 12 bold", relief='groove',
                                     width=5, bg='floral white', border=0)
        folder_name_label.grid(row=total_rows, column=0, padx=2, pady=2)
        folder_name_entry = tk.Entry(self.tab1, width=self.wid[0] + 3, font="Arial 12 bold", relief='groove',
                                     textvariable=self.folder_name)
        folder_name_entry.grid(row=total_rows, column=1, padx=2, pady=2)
        # ------------------------------Add folder btn
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=self.wid[1],
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=add)
        self.btn_add.grid(row=total_rows, column=2)
        btn_remove = tk.Button(self.tab1, text="-", font="Arial 12 bold", relief='groove',
                               border=2, width=self.wid[2], fg='white', bg="red", activebackground='red2',
                               activeforeground='white', state='normal', command=back)
        btn_remove.grid(row=total_rows, column=3)

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
