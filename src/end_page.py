from tkinter import *


class EndPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        close_button = Button(
            self,
            text='End game',
            bd='3',
            command=controller.close_application,
            width=10,
            height=3,
        )
        close_button.pack(side="top")

        restart_button = Button(
            self,
            text='Play again',
            bd='3',
            command=controller.restart_quiz,
            width=10,
            height=3,
        )
        restart_button.pack()
