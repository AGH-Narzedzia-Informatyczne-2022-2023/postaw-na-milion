from tkinter import *


class EndPage(Frame):
    def __init__(self, parent, controller, message):
        Frame.__init__(self, parent)

        message = Label(self, text=message)
        message.pack()

        correct_answers = Label(self, text=f'{controller.question_number - 1}/{controller.question_max_number} correct answers')
        correct_answers.pack()

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
            text='Try again',
            bd='3',
            command=controller.restart_quiz,
            width=10,
            height=3,
        )
        restart_button.pack()
