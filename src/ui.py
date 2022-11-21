from tkinter import *


class UI:
    window = Tk()
    title = "Tytuł"
    width = 1600
    height = 900
    bg = "#74b9ff"

    def __init__(self):
        print("UI stworzony")
        self.window_setup()
        self.create_button()

        self.window.mainloop()  # tworzy okno

    def window_setup(self):
        self.window.title(self.title)
        #self.window.configure(width=self.width, height=self.height)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.configure(bg=self.bg)

    def create_button(self):
        btn = Button(
            self.window,
            text='Zacznij grę !',
            bd='3',
            command=self.window.destroy,
            width=10,
            height=3,
        )
        #btn.pack(side="top")
        btn.place(x=700, y=450)

