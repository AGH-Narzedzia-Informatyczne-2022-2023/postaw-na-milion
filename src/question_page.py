from tkinter import *


class QuestionPage(Frame):

    def __init__(self, parent, controller, number):
        Frame.__init__(self, parent)
        label = Label(self, text=f"Question {number}")
        label.grid(row=0, column=4, padx=10, pady=10)

        button2 = Button(self, text="Next Question", command=controller.next_question)

        button2.grid(row=2, column=1, padx=10, pady=10)
