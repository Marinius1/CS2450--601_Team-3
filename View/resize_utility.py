from pynput.mouse import Listener

class ResizeUtility:

    def __init__(self, master, scrollbar=None, yView=None):

        self.master = master

        self.scrollbar = scrollbar
        self.yview = yView

        self.element_callbacks = []
        self.style_callbacks = []
        self.canvas_callbacks = []
        self.frame_callbacks = []
        self.canvas_window_callbacks = []

        self.can_listen = False
        self.is_first_draw = True

        self.master.bind('<Configure>', lambda event: self.resize(event=event))

    def title_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.2)

    def heading_one_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.15)

    def heading_two_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.1)

    def heading_three_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.09)

    def heading_four_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.085)

    def body_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.08)

    def register_element(self, callback, mode):
        self.element_callbacks.append([callback, mode])

    def register_style(self, style, tag, mode):
        self.style_callbacks.append([style, tag, mode])

    def register_canvas(self, canvas, length):
        self.canvas_callbacks.append([canvas, length])

    def register_frame(self, frame):
        self.frame_callbacks.append(frame)

    def register_canvas_window(self, window):
        self.canvas_window_callbacks.append(window)

    def on_click(self, x, y, button, pressed):
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        if not pressed:

            self.morph()

            self.can_listen = False
            self.listener.stop()
            self.listener = None

            return False

    def morph(self):
        for i in self.element_callbacks:
            if i[1] == "title":
                i[0].configure(font=('Roboto', self.title_text()))
            if i[1] == "h1":
                i[0].configure(font=('Roboto', self.heading_one_text()))
            if i[1] == "h2":
                i[0].configure(font=('Roboto', self.heading_two_text()))
            if i[1] == "h3":
                i[0].configure(font=('Roboto', self.heading_three_text()))
            if i[1] == "h4":
                i[0].configure(font=('Roboto', self.heading_four_text()))
            if i[1] == "body":
                i[0].configure(font=('Roboto', self.body_text()))

        for i in self.style_callbacks:
            if i[2] == "title":
                i[0].configure(style=i[1], font=('Roboto', self.title_text()))
            if i[2] == "h1":
                i[0].configure(style=i[1], font=('Roboto', self.heading_one_text()))
            if i[2] == "h2":
                i[0].configure(style=i[1], font=('Roboto', self.heading_two_text()))
            if i[2] == "h3":
                i[0].configure(style=i[1], font=('Roboto', self.heading_three_text()))
            if i[2] == "h4":
                i[0].configure(style=i[1], font=('Roboto', self.heading_four_text()))
            if i[2] == "body":
                i[0].configure(style=i[1], font=('Roboto', self.body_text()))

        width = self.master.winfo_width()
        height = self.master.winfo_height()
        ratio = 7.0/8.0


        if len(self.canvas_callbacks) > 0:
            new_width = (width * ratio) / len(self.canvas_callbacks)
            for i in self.canvas_callbacks:
                i[0].configure(scrollregion=i[0].bbox("all"), width=new_width, height=height)
                if self.scrollbar is not None:
                    self.scrollbar.configure(command=self.yview)
                for j in i[0].find_all():
                    i[0].itemconfig(j, width=new_width)

        if len(self.frame_callbacks) > 0:
            new_width = (width * ratio) / len(self.canvas_callbacks)
            for i in self.frame_callbacks:
                i.configure(width = int(new_width))

    def resize(self, event):

        if not self.can_listen and not self.can_listen and not self.is_first_draw:
            self.can_listen = True

            # print('resize')
            # Collect events until released
            self.listener = Listener(on_click=self.on_click)
            self.listener.start()

        if self.is_first_draw:
            # print('first event')
            self.is_first_draw = False