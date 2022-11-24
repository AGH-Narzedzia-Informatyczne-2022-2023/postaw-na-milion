from tkinter import *


class QuestionPage(Frame):
    def __init__(self, parent, controller, number):
        Frame.__init__(self, parent)

        questionNumber = Label(self, text=f"Question {number}")
        questionNumber.grid(row=0, column=4, padx=10, pady=10)

        nextQuestion = Button(self, text="Next Question", command=controller.next_question)
        nextQuestion.grid(row=6, column=1, padx=10, pady=10)

        questionTitle = Label(self, text=f"title of question {number}")
        questionTitle.grid(row=1, column=2, padx=10, pady=10)

        self.answer = IntVar()
        self.show_answer("answer 1", 2)
        self.show_answer("answer 2", 3)
        self.show_answer("answer 3", 4)
        self.show_answer("answer 4", 5)

    def show_answer(self, text, number):
        r = Radiobutton(self, text=text, variable=self.answer, value=number)
        r.grid(row=number, column=1, padx=10, pady=10)

