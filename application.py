import tkinter as tk
import webbrowser
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter import ttk
# AES 256 encryption/decryption using pycryptodome library
from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
import search


# pip install pycryptodomex
# pip install pycryptodome
def open_url(self):
    print("Open Url : " + self)
    webbrowser.open_new(self)


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

        self.file_menu_items.add_command(label="All Folders", command=self.refresh_folder_table)
        self.file_menu_items.add_command(label="Settings...")
        self.file_menu_items.add_separator()

        self.file_menu_items.add_command(label="Exit", command=self.master.destroy)

        self.tools_menu_items = tk.Menu(self.menu_bar, tearoff=0)

        self.tools_menu_items.add_command(label="Auto Fill")
        self.tools_menu_items.add_command(label="Generate Password", command=self.generate_pass)

        self.help_menu_items = tk.Menu(self.menu_bar, tearoff=0)

        intro_url = "https://github.com/Ahmed-nd/PassLock#introduction"
        self.help_menu_items.add_command(label="Introduction", command=lambda link=intro_url: open_url(link))
        self.help_menu_items.add_separator()
        updates_url = "https://github.com/Ahmed-nd/PassLock#download"
        self.help_menu_items.add_command(label="Check for Updates...",
                                         command=lambda link=updates_url: open_url(link))
        license_url = "https://github.com/Ahmed-nd/PassLock#license"
        self.help_menu_items.add_command(label="License", command=lambda link=license_url: open_url(link))
        self.help_menu_items.add_separator()

        about_url = "https://github.com/Ahmed-nd/PassLock#developers"
        self.help_menu_items.add_command(label="About", command=lambda link=about_url: open_url(link))

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
        btn_enter = tk.Button(self.frame_left, text="All Folders", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1', command=self.refresh_folder_table)
        btn_enter.grid(row=0, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Auto Fill", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=1, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Generate\nPassword", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1', command=self.generate_pass)
        btn_enter.grid(row=2, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="Setting", font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=3, column=0, columnspan=2, sticky='n', pady=10)
        btn_enter = tk.Button(self.frame_left, text="About", command=lambda link=about_url: open_url(link)
                              , font="Arial 10 bold", border=0,
                              bg="#00dee1", activebackground='#00dee1')
        btn_enter.grid(row=4, column=0, columnspan=2, sticky='n', pady=10)
        # ------------------------------right

        # ---------------------------Table
        self.master.state('zoomed')
        # database 1
        self.lst = [('Raj', 'View', 'Edit', 'Del'),
                    ('Aaryan', 'View', 'Edit', 'Del'),
                    ('Vaishnavi', 'View', 'Edit', 'Del'),
                    ('Rachna', 'View', 'Edit', 'Del'),
                    ('Shubham', 'View', 'Edit', 'Del')]
        self.lst_tk = []
        self.wid = [30, 10, 10, 10]
        self.folder_name = tk.StringVar()
        self.bg_color = ['light cyan', 'gold', 'royal blue', 'firebrick1']
        # database 2
        self.folder_lst = []
        self.folder_lst_wid = [20, 30, 25, 10, 10, 10]
        self.account_web = tk.StringVar()
        self.account_username = tk.StringVar()
        self.account_password = tk.StringVar()
        self.folder_bg_color = ['light cyan', 'light cyan', 'light cyan', 'gold', 'royal blue', 'firebrick1']
        # add btn
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=self.add_new_folder)
        self.show_table()

    # GUI folder table
    def show_table(self):
        """
        show all the Folders in database
        """

        def command(find):
            print('search:' + find)

        # floral white
        filename = tk.Label(self.tab1, text="Folders:", width=10, bg='floral white',
                            font="Times 26 bold", fg='gray20')
        filename.grid(row=0, column=0, pady=25)
        # Search box
        search.SearchBox(self.tab1, command=command, placeholder="Type and press enter",
                         entry_highlightthickness=0).grid(row=0, column=3, columnspan=3)
        # menu
        lst_menu = ['Name', 'tools']
        lst_menu_wid = [30, 33]
        for i in range(2, len(lst_menu) + 2):
            e = tk.Label(self.tab1, text=lst_menu[i - 2], width=lst_menu_wid[i - 2], bg='cyan',
                         font="Arial 12 bold", relief='groove')
            e.grid(row=1, column=i, pady=2)
            if i == 3:
                e.grid(columnspan=3)
        del self.lst_tk
        self.lst_tk = []
        total_rows = len(self.lst)
        total_columns = len(self.lst[0])
        for i in range(2, total_rows + 2):
            temp_tk = []
            e = tk.Label(self.tab1, text=(i - 1), width=5, bg='cyan',
                         font="Arial 12 bold", relief='groove')
            e.grid(row=i, column=1, padx=2, pady=2, sticky='e')
            temp_tk.append(e)
            for j in range(2, total_columns + 2):
                if j == 2:
                    e = tk.Label(self.tab1, text=self.lst[i - 2][j - 2], width=self.wid[j - 2], bg=self.bg_color[j - 2],
                                 font="Arial 12 bold", relief='groove')
                else:
                    e = tk.Button(self.tab1, text=self.lst[i - 2][j - 2], width=self.wid[j - 2],
                                  bg=self.bg_color[j - 2],
                                  font="Arial 12 bold", activebackground='antique white',
                                  command=lambda row=i - 2, column=j - 2: self.folder_table_tools(row, column))
                temp_tk.append(e)
                e.grid(row=i, column=j, padx=2, pady=2)

            temp_tk = tuple(temp_tk)
            # User can't delete folder if it's the only folder
            if total_rows == 1:
                temp_tk[4]['state'] = 'disable'
            self.lst_tk.append(temp_tk)

        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=self.add_new_folder)
        # User can't add more that 12 folder
        if total_rows == 12:
            self.btn_add['state'] = 'disable'
        self.btn_add.grid(row=total_rows + 1, column=total_columns + 3)

    def refresh_folder_table(self):
        """
        refresh the folders with new frame (new data)
        """
        self.tab1.destroy()
        self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
        self.show_table()

    def folder_table_tools(self, row, column):
        """
                View folder content and Edit folder name and Delete Folder from database
                this function take the button that have been clicked (row, column) and
                from that it know witch folder and witch code that need to run.
        """
        print(row, column)
        if column == 3:
            del self.lst[row]
            self.refresh_folder_table()
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
                    self.refresh_folder_table()
                else:
                    messagebox.showerror("PassLock", "Enter folder name")

            self.btn_add.destroy()
            self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                     relief='groove', bg="lawn green", activebackground='green2',
                                     command=add)
            self.btn_add.grid(row=row + 2, column=6)
            folder_name_entry = tk.Entry(self.tab1, width=self.wid[0] + 3,
                                         font="Arial 12 bold", relief='groove',
                                         textvariable=self.folder_name)
            self.folder_name.set(self.lst[row][0])
            folder_name_entry.grid(row=row + 2, column=2, padx=2, pady=2)

        elif column == 1:
            print("View")
            """
            get the folder's accounts database
            """
            self.tab1.destroy()
            self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
            self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
            self.folder_lst = [('www.Google.com', 'go354', '123', 'Visit', 'Edit', 'Del'),
                               ('www.Google.com', 'go121', '321', 'Visit', 'Edit', 'Del'),
                               ('www.Facebook.com', 'face12354', '231', 'Visit', 'Edit', 'Del'),
                               ('www.youtube.com', 'yo4453', '132', 'Visit', 'Edit', 'Del'),
                               ('www.Coursera.com', 'Cour1234', '312', 'Visit', 'Edit', 'Del')]
            self.show_account(self.lst[row][0])

    def add_new_folder(self):
        """
                add new folder to database
                take from the user the folder name and the user can't add more than 12 folder
                """
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
                self.refresh_folder_table()
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
        folder_name_label.grid(row=total_rows + 2, column=1, padx=2, pady=2, sticky='e')
        folder_name_entry = tk.Entry(self.tab1, width=self.wid[0] + 3, font="Arial 12 bold", relief='groove',
                                     textvariable=self.folder_name)
        folder_name_entry.grid(row=total_rows + 2, column=2, padx=2, pady=2)
        # ------------------------------Add folder btn
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=self.wid[1] + self.wid[2],
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=add)
        self.btn_add.grid(row=total_rows + 3, column=4, columnspan=3)
        btn_remove = tk.Button(self.tab1, text="-", font="Arial 12 bold", relief='groove',
                               border=2, width=self.wid[1] + self.wid[2], fg='white', bg="red", activebackground='red2',
                               activeforeground='white', state='normal', command=back)
        btn_remove.grid(row=total_rows + 2, column=4, columnspan=3, pady=10)

    # GUI account table
    def show_account(self, account_fold_name):
        """
                show all the accounts in database folder
                """

        def command(find):
            print('search :' + find)

        # floral white
        filename = tk.Label(self.tab1, text=account_fold_name + ":", width=40, bg='floral white',
                            font="Times 26 bold", fg='gray20', anchor='w')
        filename.grid(row=0, column=0, pady=25, columnspan=10, sticky='w')
        search.SearchBox(self.tab1, command=command, placeholder="Type and press enter",
                         entry_highlightthickness=0).grid(row=0, column=5, columnspan=3)
        lst_menu = ['Website', 'Username', 'Password', 'tools']
        lst_menu_wid = [20, 30, 25, 33]
        for i in range(2, len(lst_menu) + 2):
            e = tk.Label(self.tab1, text=lst_menu[i - 2], width=lst_menu_wid[i - 2], bg='cyan',
                         font="Arial 12 bold", relief='groove')
            e.grid(row=1, column=i, pady=2)
            if i == 5:
                e.grid(columnspan=3)
        del self.lst_tk
        self.lst_tk = []
        total_rows = len(self.folder_lst)
        total_columns = len(self.folder_lst[0])
        for i in range(2, total_rows + 2):
            temp_tk = []
            e = tk.Label(self.tab1, text=(i - 1), width=5, bg='cyan',
                         font="Arial 12 bold", relief='groove')
            e.grid(row=i, column=1, padx=20, pady=2)
            temp_tk.append(e)
            for j in range(2, total_columns + 2):
                if j < 5:
                    e = tk.Label(self.tab1, text=self.folder_lst[i - 2][j - 2], width=self.folder_lst_wid[j - 2],
                                 bg=self.folder_bg_color[j - 2], font="Arial 12 bold", relief='groove')
                else:
                    e = tk.Button(self.tab1, text=self.folder_lst[i - 2][j - 2], width=self.folder_lst_wid[j - 2],
                                  bg=self.folder_bg_color[j - 2], font="Arial 12 bold",
                                  activebackground='antique white',
                                  command=lambda row=i - 2, column=j - 2:
                                  self.accounts_table_tools(account_fold_name, row, column))
                temp_tk.append(e)
                e.grid(row=i, column=j, padx=2, pady=2)

            temp_tk = tuple(temp_tk)
            if total_rows == 1:
                temp_tk[5]['state'] = 'disable'
            self.lst_tk.append(temp_tk)

            # self.e.insert(END, lst[i][j])
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=lambda: self.add_new_account(account_fold_name))
        if total_rows == 12:
            self.btn_add['state'] = 'disable'
        self.btn_add.grid(row=total_rows + 1, column=total_columns + 3)

    def accounts_table_tools(self, account_fold_name, row, column):
        """
                        View folder content and Edit folder name and Delete Folder from database
                        this function take the button that have been clicked (row, column) and
                        from that it know witch folder and witch code that need to run.
                """
        print(row, column)
        if column == 5:
            # delete record
            del self.folder_lst[row]
            self.tab1.destroy()
            self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
            self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
            self.show_account(account_fold_name)
        elif column == 4:
            # Edit record
            del self.account_web
            del self.account_username
            del self.account_password
            self.account_web = tk.StringVar()
            self.account_username = tk.StringVar()
            self.account_password = tk.StringVar()

            def add():
                print("add")
                web = self.account_web.get()
                username = self.account_username.get()
                password = self.account_password.get()
                if web != '' and username != '' and password != '':
                    t = list(self.folder_lst[row])
                    t[0] = web
                    t[1] = username
                    t[2] = password
                    self.folder_lst[row] = tuple(t)
                    self.tab1.destroy()
                    self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
                    self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
                    self.show_account(account_fold_name)
                else:
                    messagebox.showerror("PassLock", "Please Enter the data")

            total_columns = len(self.folder_lst[0])
            self.btn_add.destroy()
            self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                     relief='groove', bg="lawn green", activebackground='green2',
                                     command=add)
            self.btn_add.grid(row=row + 2, column=total_columns + 3)

            folder_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[0] + 3,
                                         font="Arial 12 bold", relief='groove',
                                         textvariable=self.account_web)
            self.account_web.set(self.folder_lst[row][0])
            folder_name_entry.grid(row=row + 2, column=2, padx=2, pady=2)

            folder_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[1] + 4,
                                         font="Arial 12 bold", relief='groove',
                                         textvariable=self.account_username)
            self.account_username.set(self.folder_lst[row][1])
            folder_name_entry.grid(row=row + 2, column=3, padx=2, pady=2)

            folder_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[2] + 3,
                                         font="Arial 12 bold", relief='groove',
                                         textvariable=self.account_password)
            self.account_password.set(self.folder_lst[row][2])
            folder_name_entry.grid(row=row + 2, column=4, padx=2, pady=2)
        elif column == 3:
            # visit record link
            open_url(self.folder_lst[row][0])

    def add_new_account(self, account_fold_name):
        print("Add folder")
        total_rows = len(self.folder_lst)
        total_columns = len(self.folder_lst[0])
        del self.account_web
        del self.account_username
        del self.account_password
        self.account_web = tk.StringVar()
        self.account_username = tk.StringVar()
        self.account_password = tk.StringVar()

        def add():
            print("add")
            web = self.account_web.get()
            username = self.account_username.get()
            password = self.account_password.get()
            if web != '' and username != '' and password != '':
                temp_lst = [web, username, password, self.folder_lst[0][3], self.folder_lst[0][4]]
                temp_lst = tuple(temp_lst)
                self.folder_lst.append(temp_lst)
                self.tab1.destroy()
                self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
                self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
                self.show_account(account_fold_name)
            else:
                messagebox.showerror("PassLock", "Please Enter the data")

        def back():
            print("remove folder")
            self.tab1.destroy()
            self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg='floral white')
            self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
            self.show_account(account_fold_name)

        self.btn_add.destroy()
        # ------------------------web name
        web_name_label = tk.Label(self.tab1, text="Web Name :", font="Arial 12 bold",
                                  width=15, bg='floral white', border=0)
        web_name_label.grid(row=total_rows + 2, column=2, padx=2, pady=2, sticky='e')
        web_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[1], font="Arial 12 bold", relief='groove',
                                  textvariable=self.account_web)
        web_name_entry.grid(row=total_rows + 2, column=3, padx=2, pady=2, columnspan=2, sticky='w')
        # -------------------------user name
        web_name_label = tk.Label(self.tab1, text="Username :", font="Arial 12 bold",
                                  width=15, bg='floral white', border=0)
        web_name_label.grid(row=total_rows + 3, column=2, padx=2, pady=2, sticky='e')
        web_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[1], font="Arial 12 bold", relief='groove',
                                  textvariable=self.account_username)
        web_name_entry.grid(row=total_rows + 3, column=3, padx=2, pady=2, columnspan=2, sticky='w')
        # -------------------------password
        web_name_label = tk.Label(self.tab1, text="Password :", font="Arial 12 bold",
                                  width=15, bg='floral white', border=0)
        web_name_label.grid(row=total_rows + 4, column=2, padx=2, pady=2, sticky='e')
        folder_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[1],
                                     font="Arial 12 bold", relief='groove',
                                     textvariable=self.account_password)
        folder_name_entry.grid(row=total_rows + 4, column=3, padx=2, pady=17, columnspan=2, sticky='w')
        # ------------------------------Add folder btn
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2,
                                 width=self.folder_lst_wid[3] + self.folder_lst_wid[4] + 1,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=add)
        self.btn_add.grid(row=total_rows + 3, column=5, columnspan=4)
        btn_remove = tk.Button(self.tab1, text="-", font="Arial 12 bold", relief='groove',
                               border=2, width=self.folder_lst_wid[3] + self.folder_lst_wid[4] + 1,
                               fg='white', bg="red", activebackground='red2',
                               activeforeground='white', state='normal', command=back)
        btn_remove.grid(row=total_rows + 2, column=5, columnspan=4, pady=10)

    # GUI generate password
    def generate_pass(self):

        import random
        import array
        self.tab1.destroy()
        self.tab1 = tk.Frame(self.canvas_right_table, padx=100, pady=100, bg='floral white')
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
        strong_pass = tk.StringVar()
        current_value = tk.DoubleVar()

        def generate_password(max_len):
            # MAX_LEN
            # maximum length of password needed
            # this can be changed to suit your password length

            # declare arrays of the character that we need in out password
            # Represented as chars to enable easy string concatenation
            digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            lowercase_characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                    'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                    'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                    'z']

            uppercase_characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                    'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                    'Z']

            symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '+', '-', "'",
                       ".", ","]

            # combines all the character arrays above to form one array
            combined_list = digits + uppercase_characters + lowercase_characters + symbols

            # randomly select one character from each character set above
            rand_digit = random.choice(digits)
            rand_upper = random.choice(uppercase_characters)
            rand_lower = random.choice(lowercase_characters)
            rand_symbol = random.choice(symbols)

            # combine the character randomly selected above
            # at this stage, the password contains only 4 characters but
            # we want a 12-character password
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

            # now that we are sure we have at least one character from each
            # set of characters, we fill the rest of
            # the password length by selecting randomly from the combined
            # list of character above.
            for x in range(max_len - 4):
                temp_pass = temp_pass + random.choice(combined_list)

                # convert temporary password into array and shuffle to
                # prevent it from having a consistent pattern
                # where the beginning of the password is predictable
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)

            # traverse the temporary password array and append the chars
            # to form the password
            password = ""
            for x in temp_pass_list:
                password = password + x
            strong_pass.set(password)

        def slider_changed(_):
            slider_num_label.config(text=str(int(current_value.get())))

            # triggered off left button click on text_field

        def copy_text_to_clipboard():
            field_value = strong_pass.get()
            self.master.clipboard_clear()  # clear clipboard contents
            self.master.clipboard_append(field_value)  # append new value to clipbaord

        # Frame 1 generate_frame
        generate_frame = tk.Frame(self.tab1)
        generate_frame.pack(pady=10)
        strong_pass_entry = tk.Entry(generate_frame, width=50,
                                     font="Arial 12 bold", relief='groove',
                                     textvariable=strong_pass)

        strong_pass_entry.pack(side='left')
        btn_generate = tk.Button(generate_frame, text="Generate", font="Arial 12 bold", border=2,
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=lambda: generate_password(int(current_value.get())))
        btn_generate.pack(side='left')
        btn_copy = tk.Button(generate_frame, text="Copy", font="Arial 12 bold", border=2,
                             relief='groove', bg="light goldenrod", activebackground='gold',
                             command=copy_text_to_clipboard)
        btn_copy.pack(side='left')
        # Frame 2 pass_len_frame
        pass_len_frame = tk.Frame(self.tab1)
        pass_len_frame.pack()
        # scale Value
        current_value.set(5)
        scroll_num = ttk.Scale(pass_len_frame, from_=5, to=45, orient='horizontal', length=300,
                               variable=current_value, command=slider_changed)
        scroll_num.pack(side='left')
        slider_num_label = tk.Label(pass_len_frame, text=str(int(current_value.get())),
                                    font="Arial 12 bold", relief='groove')
        slider_num_label.pack(side='left')

    # Backend
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
