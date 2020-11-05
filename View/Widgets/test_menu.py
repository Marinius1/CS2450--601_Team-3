from tkinter import *
from button import Button as Btn

class Example(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.master.title("Toolbar")

        menubar = Menu(self.master)
        self.fileMenu = Menu(self.master, tearoff=0)
        self.fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=self.fileMenu)

        toolbar = Frame(self.master, bd=1, relief=RAISED)

        btn_0 = Btn(toolbar, text="Test", theme="Ubuntu", side=LEFT)
        btn_1 = Btn(toolbar, text="Test", theme="Ubuntu", side=LEFT)
        btn_2 = Btn(toolbar, text="Test", theme="Ubuntu", side=LEFT)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()

def main():

    root = Tk()
    root.geometry("800x600+300+300")
    root.configure(background="purple")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()