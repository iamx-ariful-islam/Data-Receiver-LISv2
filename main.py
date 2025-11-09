from tkinter import *


# root class
class App(Frame):
    def __init__(self, win):
        super().__init__(win)
        self.win   = win
        self.text  = "Not Free — This is a paid project, available after purchase!"
        self.icon_visible = False

        self.lb_icon = Label(self.win, text="⚠️", font=("Cambria", 37, "bold"), fg="red", justify="center")
        self.lb_icon.place(relx=0.5, rely=0.35, anchor="center")
        
        self.lb_text = Label(self.win, text=self.text, font=("Cambria", 19, "bold"), wraplength=700, justify="center")
        self.lb_text.place(relx=0.5, rely=0.46, anchor="center")

        self.blink_icon()


    def blink_icon(self):
        if self.icon_visible:
            self.lb_icon.config(fg="#F0F0ED")
            self.icon_visible = False
        else:
            self.lb_icon.config(fg="red")
            self.icon_visible = True
        self.win.after(600, self.blink_icon)


# root
if __name__ == '__main__':
    win = Tk()
    win.title('Example App')

    w, h = 850, 500
    sw = win.winfo_screenwidth()
    sh = win.winfo_screenheight()
    x, y = (sw - w) // 2, (sh - h) // 2
    win.geometry(f'{w}x{h}+{x}+{y-40}')
    win.resizable(0, 0)

    app = App(win)
    win.mainloop()
