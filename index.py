# tkinter/ ttk/ webbrowser
import tkinter as tk
import os


class Index(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.iconbitmap('images/icon.ico')
        self.master.title("PassLock")
        self.master.geometry("800x600")
        self.master.destroy()
        os.system('python signup.py')
        # signup(self)


if __name__ == "__main__":
    # Create object
    form = tk.Tk()
    app = Index(form)
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
Button(command,state="active, disabled, or normal")
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
