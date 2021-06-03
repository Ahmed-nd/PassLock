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
        self.master.geometry("1500x700")
        self.master.resizable(1, 1)
        # self.master.state('zoomed')
        # -------------------------------
        self.close_button = tk.Button()
        self.expand_button = tk.Button()
        self.minimize_button = tk.Button()
        self.title_bar_title = tk.Label()
        self.window = tk.Canvas(self.master)

        self.menu_bar()
        # colors
        """
        # 1
        
        # 2
        "#00dee1"
        "pale turquoise"
        "floral white"
        'white'
        
        """
        self.frame_left_color = "gray12"
        self.frame_right_color = "gray12"
        self.canvas_right_table_color = "gray70"
        self.font_color = 'thistle1'
        self.master.configure(bg=self.canvas_right_table_color)

        # self.master.state('zoomed')
        # ------------------------Application private variable

        # ---------------------------frame left
        self.frame_left = tk.Frame(self.window)
        # ---------------------------frame right
        self.frame_right = tk.Frame(self.window)
        # ---------------------------Canvas right table
        self.canvas_right_table = tk.Canvas(self.frame_right)
        self.frame_left.pack(side="left", fill='both', anchor='c')
        self.frame_right.pack(side="left", expand='true', fill='both', anchor='c')
        self.canvas_right_table.pack(side="top", fill='both', anchor='c', padx=30, expand='true')

        # database 1
        self.lst = []
        self.lst_tk = []
        self.wid = []
        self.folder_name = tk.StringVar()
        self.bg_color = []
        # database 2
        self.folder_lst = []
        self.folder_lst_wid = []
        self.account_web = tk.StringVar()
        self.account_username = tk.StringVar()
        self.account_password = tk.StringVar()
        self.folder_bg_color = []
        # ---------------------------Table
        self.tab1 = tk.Frame(self.canvas_right_table)
        self.btn_add = tk.Button(self.tab1)
        self.show_app()

    # GUI folder table
    def show_table(self):
        """
        show all the Folders in database
        """

        def command(find):
            print('search:' + find)

        # floral white
        filename = tk.Label(self.tab1, text="Folders:", width=10, bg=self.canvas_right_table_color,
                            font="Times 26 bold", )
        filename.grid(row=0, column=0, pady=25)
        # Search box
        search.SearchBox(self.tab1, command=command, placeholder="Type and press enter",
                         button_foreground=self.font_color,
                         entry_highlightthickness=0, entry_width=40).grid(row=0, column=3, columnspan=3)
        # menu
        lst_menu = ['Name', 'tools']
        lst_menu_wid = [30, 33]
        for i in range(2, len(lst_menu) + 2):
            e = tk.Label(self.tab1, text=lst_menu[i - 2], width=lst_menu_wid[i - 2], fg=self.font_color,
                         font="Arial 12 bold", relief='groove', bg=self.frame_left_color, )
            e.grid(row=1, column=i, pady=2)
            if i == 3:
                e.grid(columnspan=3)
        del self.lst_tk
        self.lst_tk = []
        total_rows = len(self.lst)
        total_columns = len(self.lst[0])
        for i in range(2, total_rows + 2):
            temp_tk = []
            e = tk.Label(self.tab1, text=(i - 1), width=5, bg=self.frame_left_color, fg=self.font_color,
                         font="Arial 12 bold", relief='groove', )
            e.grid(row=i, column=1, padx=2, pady=2, sticky='e')
            temp_tk.append(e)
            for j in range(2, total_columns + 2):
                if j == 2:
                    e = tk.Label(self.tab1, text=self.lst[i - 2][j - 2], width=self.wid[j - 2], bg=self.bg_color[j - 2],
                                 font="Arial 12 bold", relief='groove', )
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
                                 command=self.add_new_folder, )
        # User can't add more that 12 folder
        if total_rows == 12:
            self.btn_add['state'] = 'disable'
        self.btn_add.grid(row=total_rows + 1, column=total_columns + 3)

    def refresh_folder_table(self):
        """
        refresh the folders with new frame (new data)
        """
        self.tab1.destroy()
        self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg=self.canvas_right_table_color)
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
                                     command=add, )
            self.btn_add.grid(row=row + 2, column=6)
            folder_name_entry = tk.Entry(self.tab1, width=self.wid[0] + 3,
                                         font="Arial 12 bold", relief='groove',
                                         textvariable=self.folder_name, )
            self.folder_name.set(self.lst[row][0])
            folder_name_entry.grid(row=row + 2, column=2, padx=2, pady=2)

        elif column == 1:
            print("View")
            """
            get the folder's accounts database
            """
            self.tab1.destroy()
            self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg=self.canvas_right_table_color)
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
                                     width=5, bg=self.canvas_right_table_color, border=0)
        folder_name_label.grid(row=total_rows + 2, column=1, padx=2, pady=2, sticky='e')
        folder_name_entry = tk.Entry(self.tab1, width=self.wid[0] + 3, font="Arial 12 bold", relief='groove',
                                     textvariable=self.folder_name)
        folder_name_entry.grid(row=total_rows + 2, column=2, padx=2, pady=2)
        # ------------------------------Add folder btn
        self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=self.wid[1] + self.wid[2],
                                 relief='groove', bg="lawn green", activebackground='green2',
                                 command=add, )
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
        filename = tk.Label(self.tab1, text=account_fold_name + ":", width=40, bg=self.canvas_right_table_color,
                            font="Times 26 bold", anchor='w')
        filename.grid(row=0, column=0, pady=25, columnspan=10, sticky='w')
        search.SearchBox(self.tab1, command=command, placeholder="Type and press enter",
                         entry_highlightthickness=0, button_foreground=self.font_color
                         , entry_width=40).grid(row=0, column=5, columnspan=3)
        lst_menu = ['Website', 'Username', 'Password', 'tools']
        lst_menu_wid = [20, 30, 25, 33]
        for i in range(2, len(lst_menu) + 2):
            e = tk.Label(self.tab1, text=lst_menu[i - 2], width=lst_menu_wid[i - 2],
                         font="Arial 12 bold", relief='groove', fg=self.font_color, bg=self.frame_left_color)
            e.grid(row=1, column=i, pady=2)
            if i == 5:
                e.grid(columnspan=3)
        del self.lst_tk
        self.lst_tk = []
        total_rows = len(self.folder_lst)
        total_columns = len(self.folder_lst[0])
        for i in range(2, total_rows + 2):
            temp_tk = []
            e = tk.Label(self.tab1, text=(i - 1), width=5,
                         font="Arial 12 bold", relief='groove', fg=self.font_color, bg=self.frame_left_color)
            e.grid(row=i, column=1, padx=2, pady=2)
            temp_tk.append(e)
            for j in range(2, total_columns + 2):
                if j < 5:
                    e = tk.Label(self.tab1, text=self.folder_lst[i - 2][j - 2], width=self.folder_lst_wid[j - 2],
                                 bg=self.folder_bg_color[j - 2], font="Arial 12 bold", relief='groove', )
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
            self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg=self.canvas_right_table_color)
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
                    self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg=self.canvas_right_table_color)
                    self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
                    self.show_account(account_fold_name)
                else:
                    messagebox.showerror("PassLock", "Please Enter the data")

            total_columns = len(self.folder_lst[0])
            self.btn_add.destroy()
            self.btn_add = tk.Button(self.tab1, text="+", font="Arial 12 bold", border=2, width=2,
                                     relief='groove', bg="lawn green", activebackground='green2',
                                     command=add, )
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
                temp_lst = [web, username, password, self.folder_lst[0][3], self.folder_lst[0][4],
                            self.folder_lst[0][5]]
                temp_lst = tuple(temp_lst)
                self.folder_lst.append(temp_lst)
                self.tab1.destroy()
                self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg=self.canvas_right_table_color)
                self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
                self.show_account(account_fold_name)
            else:
                messagebox.showerror("PassLock", "Please Enter the data")

        def back():
            print("remove folder")
            self.tab1.destroy()
            self.tab1 = tk.Frame(self.canvas_right_table, padx=20, pady=20, bg=self.canvas_right_table_color)
            self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
            self.show_account(account_fold_name)

        self.btn_add.destroy()
        # ------------------------web name
        web_name_label = tk.Label(self.tab1, text="Web Name :", font="Arial 12 bold",
                                  width=15, bg=self.canvas_right_table_color, border=0)
        web_name_label.grid(row=total_rows + 2, column=2, padx=2, pady=2, sticky='e')
        web_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[1], font="Arial 12 bold", relief='groove',
                                  textvariable=self.account_web)
        web_name_entry.grid(row=total_rows + 2, column=3, padx=2, pady=2, columnspan=2, sticky='w')
        # -------------------------user name
        web_name_label = tk.Label(self.tab1, text="Username :", font="Arial 12 bold",
                                  width=15, bg=self.canvas_right_table_color, border=0)
        web_name_label.grid(row=total_rows + 3, column=2, padx=2, pady=2, sticky='e')
        web_name_entry = tk.Entry(self.tab1, width=self.folder_lst_wid[1], font="Arial 12 bold", relief='groove',
                                  textvariable=self.account_username, )
        web_name_entry.grid(row=total_rows + 3, column=3, padx=2, pady=2, columnspan=2, sticky='w')
        # -------------------------password
        web_name_label = tk.Label(self.tab1, text="Password :", font="Arial 12 bold",
                                  width=15, bg=self.canvas_right_table_color, border=0)
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
        self.tab1 = tk.Frame(self.canvas_right_table, padx=100, pady=100, bg=self.canvas_right_table_color)
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
                                 relief='groove', bg="lawn green", activebackground='green2', fg=self.font_color,
                                 command=lambda: generate_password(int(current_value.get())))
        btn_generate.pack(side='left')
        btn_copy = tk.Button(generate_frame, text="Copy", font="Arial 12 bold", border=2, fg=self.font_color,
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

    # setting
    def setting(self):

        self.tab1.destroy()
        self.tab1 = tk.Frame(self.canvas_right_table, padx=100, pady=100, bg=self.canvas_right_table_color)
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
        dark_mode_frame = tk.Frame(self.tab1, bg=self.canvas_right_table_color)
        dark_mode_frame.grid(row=1, column=1)

        # self.frame_left_color = "purple1"
        # self.frame_right_color = "purple1"
        # self.canvas_right_table_color = "DarkOrchid1"
        # self.font_color = 'white'
        # def mode():
        #     if selected.get() == '1':
        #         print(1)
        #         self.frame_left_color = "gray12"
        #         self.frame_right_color = "gray12"
        #         self.canvas_right_table_color = "gray70"
        #         self.font_color = 'thistle1'
        #         self.frame_left.destroy()
        #         self.frame_right.destroy()
        #         self.show_app()
        #     else:
        #         print(0)
        #         self.frame_left_color = "#00dee1"
        #         self.frame_right_color = "#00dee1"
        #         self.canvas_right_table_color = "floral white"
        #         self.font_color = 'black'
        #         self.frame_left.destroy()
        #         self.frame_right.destroy()
        #         self.show_app()

        # selected = tk.StringVar()
        # label = tk.Label(dark_mode_frame, text="Dark Mode", bg=self.canvas_right_table_color,
        #                  font="Times 16 bold", anchor='w')
        # label.pack(padx=5, pady=5)
        #
        # # Style class to add style to Radiobutton
        # # it can be used to style any ttk widget
        # style = ttk.Style(self.tab1)
        # style.configure("TRadiobutton", background=self.canvas_right_table_color,
        #                 fg=self.font_color, font=("arial", 10, "bold"))
        # r1 = ttk.Radiobutton(dark_mode_frame, text='On', value='1', variable=selected, command=mode)
        # r2 = ttk.Radiobutton(dark_mode_frame, text='Off', value='0', variable=selected, command=mode)
        # r1.pack(padx=5, pady=5)
        # r2.pack(padx=5, pady=5)

    def auto_fill(self):
        self.tab1.destroy()
        self.tab1 = tk.Frame(self.canvas_right_table, padx=100, pady=100, bg=self.canvas_right_table_color)
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')
        dark_mode_frame = tk.Frame(self.tab1, bg=self.canvas_right_table_color)
        dark_mode_frame.grid(row=1, column=1)

    def show_app(self):
        # ------------------------------Menu
        # menu_bar = tk.Menu()
        #
        # file_menu_items = tk.Menu(menu_bar, tearoff=0)
        #
        # file_menu_items.add_command(label="All Folders", command=self.refresh_folder_table)
        # file_menu_items.add_command(label="Settings...")
        # file_menu_items.add_separator()
        #
        # file_menu_items.add_command(label="Exit", command=self.master.destroy)
        #
        # tools_menu_items = tk.Menu(menu_bar, tearoff=0)
        #
        # tools_menu_items.add_command(label="Auto Fill")
        # tools_menu_items.add_command(label="Generate Password", command=self.generate_pass)
        #
        # help_menu_items = tk.Menu(menu_bar, tearoff=0)
        #
        # intro_url = "https://github.com/Ahmed-nd/PassLock#introduction"
        # help_menu_items.add_command(label="Introduction", command=lambda link=intro_url: open_url(link))
        # help_menu_items.add_separator()
        # updates_url = "https://github.com/Ahmed-nd/PassLock#download"
        # help_menu_items.add_command(label="Check for Updates...",
        #                             command=lambda link=updates_url: open_url(link))
        # license_url = "https://github.com/Ahmed-nd/PassLock#license"
        # help_menu_items.add_command(label="License", command=lambda link=license_url: open_url(link))
        # help_menu_items.add_separator()
        #
        about_url = "https://github.com/Ahmed-nd/PassLock#developers"
        # help_menu_items.add_command(label="About", command=lambda link=about_url: open_url(link))
        #
        # menu_bar.add_cascade(label="File", menu=file_menu_items)
        # menu_bar.add_cascade(label="Tools", menu=tools_menu_items)
        # menu_bar.add_cascade(label="Help", menu=help_menu_items)
        # self.master.config(menu=menu_bar)

        # ---------------------------frame refresh

        self.tab1 = tk.Frame(self.canvas_right_table)

        self.frame_left.config(bg=self.frame_left_color, relief="groove", borderwidth=3, padx=30,
                               pady=30)
        self.frame_left.pack(side="left", fill='both', anchor='c')
        # ---------------------------frame right
        self.frame_right.config(bg=self.frame_right_color, relief="groove", borderwidth=0, pady=30)
        self.frame_right.pack(side="left", expand='true', fill='both', anchor='c')
        # ---------------------------Canvas right table
        self.canvas_right_table.config(bg=self.canvas_right_table_color, relief="ridge",
                                       borderwidth=4)
        self.canvas_right_table.pack(side="top", fill='both', anchor='c', padx=30, expand='true')
        # ---------------------------Table
        self.tab1.config(padx=20, pady=20, bg=self.canvas_right_table_color)
        self.tab1.pack(side="left", fill="both", padx=10, pady=10, expand='true')

        # ------------------------------left
        btn_enter = tk.Button(self.frame_left, text="All Folders", font="Arial 10 bold", border=0,
                              bg=self.frame_left_color, activebackground=self.frame_left_color,
                              command=self.refresh_folder_table, fg=self.font_color)
        btn_enter.pack(pady=10)
        btn_enter = tk.Button(self.frame_left, text="Auto Fill", font="Arial 10 bold", border=0, command=self.auto_fill,
                              bg=self.frame_left_color, activebackground=self.frame_left_color, fg=self.font_color)
        btn_enter.pack(pady=10)
        btn_enter = tk.Button(self.frame_left, text="Generate\nPassword", font="Arial 10 bold", border=0,
                              bg=self.frame_left_color, activebackground=self.frame_left_color,
                              command=self.generate_pass, fg=self.font_color)
        btn_enter.pack(pady=10)
        btn_enter = tk.Button(self.frame_left, text="Setting", font="Arial 10 bold", border=0, command=self.setting,
                              bg=self.frame_left_color, activebackground=self.frame_left_color, fg=self.font_color)
        btn_enter.pack(pady=10)
        btn_enter = tk.Button(self.frame_left, text="About", command=lambda link=about_url: open_url(link)
                              , font="Arial 10 bold", border=0, fg=self.font_color,
                              bg=self.frame_left_color, activebackground=self.frame_left_color)
        btn_enter.pack(pady=10)
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
                                 command=self.add_new_folder, fg=self.font_color)
        self.show_table()

    def menu_bar(self):
        lgray = '#545454'
        dgray = '#242424'
        rgray = '#2e2e2e'
        self.master.overrideredirect(True)
        self.master.attributes('-topmost', True)
        title_bar = tk.Frame(self.master, bg='#2e2e2e', relief='raised', bd=0, highlightthickness=0, pady=4, padx=4)

        def get_pos(event):
            xwin = app.winfo_x()
            ywin = app.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx

            def move_window(e):
                self.master.geometry("1500x700" + '+{0}+{1}'.format(e.x_root + xwin, e.y_root + ywin + 110))

            title_bar.bind('<B1-Motion>', move_window)

        title_bar.bind('<Button-1>', get_pos)

        def changex_on_hovering(event):
            self.close_button['bg'] = 'red'

        def returnx_to_normalstate(event):
            self.close_button['bg'] = rgray

        def change_size_on_hovering(event):
            self.expand_button['bg'] = lgray

        def return_size_on_hovering(event):
            self.expand_button['bg'] = rgray

        def changem_size_on_hovering(event):
            self.minimize_button['bg'] = lgray

        def returnm_size_on_hovering(event):
            self.minimize_button['bg'] = rgray

        def minimizeWindow():
            self.master.withdraw()
            self.master.overrideredirect(False)
            self.master.iconify()

        def check_map(event):  # apply override on deiconify.
            if str(event) == "<Map event>":
                self.master.overrideredirect(1)
                print('Deiconified', event)
            else:
                print('Iconified', event)

        def restore_down():
            if self.master.state() == 'normal':
                self.master.state('zoomed')
            else:
                self.master.state('normal')

        def hide_screen(e):
            # root.overrideredirect(False)
            self.master.withdraw()
            self.master.overrideredirect(0)
            # self.master.update_idletasks()
            # self.master.state('withdrawn')
            self.master.state("iconic")

        def screen_appear(e):
            print(e)
            self.master.overrideredirect(1)
            # self.master.update_idletasks()
            # self.master.state("normal")
            # self.master.state('zoomed')

        # put a close button on the title bar
        self.close_button = tk.Button(title_bar, text='  X  ', command=self.master.destroy, bg=rgray, padx=2, pady=2,
                                      font=("calibri", 10), bd=0, fg='white', highlightthickness=0)
        self.expand_button = tk.Button(title_bar, text=' ■ ', bg=rgray, padx=2, pady=2, bd=0, fg='white',
                                       font=("calibri", 10), command=restore_down,
                                       highlightthickness=0)
        self.minimize_button = tk.Button(title_bar, text=' ─ ', bg=rgray, padx=2, pady=2, bd=0, fg='white',
                                         font=("calibri", 10), highlightthickness=0, command=minimizeWindow)
        self.title_bar_title = tk.Label(title_bar, text='PassLock', bg=rgray, bd=0, fg='white',
                                        font=("helvetica", 10), padx=21, pady=2,
                                        highlightthickness=0)
        # a canvas for the main area of the window
        self.window.config(bg='black', highlightthickness=0)
        # pack the widgets
        title_bar.pack(fill='x')
        self.close_button.pack(side='right')
        self.expand_button.pack(side='right')
        self.minimize_button.pack(side='right')
        self.title_bar_title.pack(side='left', padx=20)
        self.window.pack(expand=1, fill='both')

        # Animation
        self.close_button.bind('<Enter>', changex_on_hovering)
        self.close_button.bind('<Leave>', returnx_to_normalstate)
        self.expand_button.bind('<Enter>', change_size_on_hovering)
        self.expand_button.bind('<Leave>', return_size_on_hovering)
        self.minimize_button.bind('<Enter>', changem_size_on_hovering)
        self.minimize_button.bind('<Leave>', returnm_size_on_hovering)
        # check_map
        self.master.bind('<Map>', check_map)  # added bindings to pass windows status to function
        self.master.bind('<Unmap>', check_map)

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
