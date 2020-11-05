from tkinter import *


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
        photo = PhotoImage(file="logo.gif")
        label = Label(toolbar, image=photo, background="red")
        label.image = photo
        label.pack(side=LEFT, padx=2, pady=2)
        exitButton = Button(toolbar, relief=FLAT,
                            command=self.quit)
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    def onExit(self):
        self.quit()

def main():

    root = Tk()
    root.geometry("250x150+300+300")
    app = Example()
    root.mainloop()

if __name__ == '__main__':
    main()