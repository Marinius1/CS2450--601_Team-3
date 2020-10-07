"""
Root window creation logic. this can effectively be a singleton unless we
want to have multiple windows open, though that is not likely. Call once
On application init
"""
# TODO: implement singleton logic

import tkinter as tk


class Window(tk.Frame):
    """
    Window class: responsible for being the 'root' component of all other
    widgets, layout, etc.. has properties like height, width, etc. will most
    likely handle resize events as well.
    """

    def __init__(self, master=None, title: str = "Test Window",
                 width: int = 800, height: int = 600):
        """
        window class init function. Needs to create the window of course,
        and set up any window-level logic data pertinent to the view.
        """

        super().__init__(master)
        self.pack()

        self.width = width
        self.height = height
        self.set_size()

        self.master.title(title)

        self.nodes = []

    def add_node(self, node):
        self.nodes.append(node)

    def get_nodes(self):
        return self.nodes

    @property
    def size(self):
        return [self.width, self.height]

    @size.setter
    def size(self, value: list):
        """manually resize window within setter"""
        self.width = value[0]
        self.height = value[1]
        self.set_size()

    def set_size(self):
        self.master.geometry(str(self.width) + "x" + str(self.height))
