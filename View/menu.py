import tkinter as tk
from tkinter import filedialog


class Menu():
    """
    the 'row' class. creates a View that arranges children horizontally within
    it's bounds. can auto wrap or truncate if needed. scrolling is also an
    option.
    """

    def __init__(self, master=None, window=None):
        """
        init(name: str, children[]: List<varies>): void
        calls super(). needs to populate the horizontal View. also needs to bind either
        truncate or wrap data when the contents of the horizontal View exceed the
        bounds.
        """


        self.master = master
        self.window = window

        self.menu = tk.Menu(self.master)

        self.menu_file = tk.Menu(self.menu, tearoff=0)
        self.menu_file.add_command(label="Import...", command=self.import_file)
        self.menu_file.add_separator()

        self.menu_file.add_command(label="Logout", command=self.logout)
        self.menu_file.add_command(label="Exit", command=self.master.quit)

        self.menu.add_cascade(label="File", menu=self.menu_file)

        self.master.configure(menu=self.menu)

    def import_file(self):
        file_name = filedialog.askopenfilename(initialdir="/",
                                               title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*"))
                                               )
        print(file_name)

    def logout(self):
        self.window.login()

