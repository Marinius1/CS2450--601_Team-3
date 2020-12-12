from pynput.mouse import Listener

class ResizeUtility:

    def __init__(self, master):

        self.master = master

        self.element_callbacks = []
        self.style_callbacks = []

        self.can_listen = False
        self.is_first_draw = True

        self.master.bind('<Configure>', lambda event: self.resize(event=event))

    def body_text(self):
        width = self.master.winfo_width()
        height = self.master.winfo_height()
        return int((height/9 + width/32) * 0.07)

    def register_element(self, callback, mode):
        self.element_callbacks.append([callback, mode])

    def register_style(self, style, tag, mode):
        self.style_callbacks.append([style, tag, mode])

    def on_click(self, x, y, button, pressed):
        # print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
        if not pressed:
            # Stop listener


            # size_ratio = ((width + height) / 2) * .01

            # print(size_ratio)
            # for i in self.canvas_columns:
            #     i.configure(font=('Roboto', int(size_ratio)), width=int(size_ratio))

            for i in self.element_callbacks:
                if i[1] == "body":
                    # print(i[0])
                    print(self.body_text())
                    i[0].configure(font=('Roboto', self.body_text()))

            for i in self.style_callbacks:
                if i[2] == "body":
                    # print(i[0])
                    print(self.body_text())
                    i[0].configure(style=i[1], font=('Roboto', self.body_text()))

            self.can_listen = False
            self.listener.stop()
            self.listener = None

            return False

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