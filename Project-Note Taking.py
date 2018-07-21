__Author__ = 'Akshay_kumar'

# import sqlite3
from tkinter import filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *

Akshay = Tk()

c = filedialog.asksaveasfilename(defaultextension='.db', filetypes=[('database files', '.db')],
                                 initialfile='Acadview_project',
                                 title="Choose your databasefile", initialdir=".", parent=Akshay)


class Notepad:
    Akshay = Tk()

    # default window width and height
    thisWidth = 300
    thisHeight = 300
    thisTextArea = Text(Akshay)
    thisMenuBar = Menu(Akshay)
    thisFileMenu = Menu(thisMenuBar, tearoff=0)
    thisEditMenu = Menu(thisMenuBar, tearoff=0)
    thisHelpMenu = Menu(thisMenuBar, tearoff=0)

    # To add scrollbar
    thisScrollBar = Scrollbar(thisTextArea)
    file = None

    def __init__(self, **kwargs):

        # Set icon
        try:
            self.Akshay.wm_iconbitmap("D:/hello-git/notepad.ico")
        except():
            pass

        # Set window size (the default is 300x300)

        try:
            self.thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.Akshay.title("Notepad_Plus+")

        # Center the window
        screenwidth = self.Akshay.winfo_screenwidth()
        screenheight = self.Akshay.winfo_screenheight()

        # For left-align
        left = (screenwidth / 2) - (self.thisWidth / 2)

        # For right-align
        top = (screenheight / 2) - (self.thisHeight / 2)

        # For top and bottom
        self.Akshay.geometry('%dx%d+%d+%d' % (self.thisWidth,
                                              self.thisHeight,
                                              left, top))

        # To make the text area auto resizable
        self.Akshay.grid_rowconfigure(0, weight=1)
        self.Akshay.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.thisFileMenu.add_command(label="Create_New",
                                      command=self.__newfile)

        # To open a already existing file
        self.thisFileMenu.add_command(label="Search|Files",
                                      command=self.__searchfile)

        # To save current file
        self.thisFileMenu.add_command(label="Save|File",
                                      command=self.__savefile)

        # To create a line in the dialog
        self.thisFileMenu.add_separator()
        self.thisFileMenu.add_command(label="Exit!",
                                      command=self.__quit_application)
        self.thisMenuBar.add_cascade(label="File",
                                     menu=self.thisFileMenu)

        # To give a feature of cut
        self.thisEditMenu.add_command(label="Cut",
                                      command=self.__cut)

        # to give a feature of copy
        self.thisEditMenu.add_command(label="Copy",
                                      command=self.__copy)

        # To give a feature of paste
        self.thisEditMenu.add_command(label="Paste",
                                      command=self.__paste)

        # To give a feature of editing
        self.thisMenuBar.add_cascade(label="Edit",
                                     menu=self.thisEditMenu)

        # To create a feature of description of the notepad
        self.thisHelpMenu.add_command(label="About Notepad_Plus+",
                                      command=self.__showabout)
        self.thisMenuBar.add_cascade(label="Help",
                                     menu=self.thisHelpMenu)

        self.Akshay.config(menu=self.thisMenuBar)

        self.thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.thisScrollBar.config(command=self.thisTextArea.yview)
        self.thisTextArea.config(yscrollcommand=self.thisScrollBar.set)

    def __quit_application(self):
        self.Akshay.destroy()
        # exit()

    def __showabout(self):
        showinfo("Notepad_Plus+", "AkshayK_Copyright © 2018\n"
                                  "FrAmed using Python 3.7 # Pycharm\n"
                                  "company @Acadview 2018")

    def __searchfile(self):

        self.file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                        ("Text Documents", "*.txt")])

        if self.file == "":

            # no file to open
            self.file = None
        else:

            # Try to open the file
            # set the window title
            self.Akshay.title(os.path.basename(self.file) + " - Notepad")
            self.thisTextArea.delete(1.0, END)

            file = open(self.file, "r")

            self.thisTextArea.insert(1.0, file.read())

            file.close()

    def __newfile(self):
        self.Akshay.title("Untitled - Notepad")
        self.file = None
        self.thisTextArea.delete(1.0, END)

    def __savefile(self):

        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt",
                                          filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])

            if self.file == "":
                self.file = None
            else:

                # Try to save the file
                file = open(self.file, "w")
                file.write(self.thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.Akshay.title(os.path.basename(self.file) + " - Notepad")
        else:
            file = open(self.file, "w")
            file.write(self.thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.Akshay.mainloop()


# Run main application
notepad = Notepad(width=720, height=400)
notepad.run()
