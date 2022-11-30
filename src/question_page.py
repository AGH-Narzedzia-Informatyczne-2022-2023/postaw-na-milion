import random
from tkinter import *


class QuestionPage(Frame):
    def __init__(self, parent, controller, number):
        Frame.__init__(self, parent)
        self.controller = controller

        self.question = controller.question_handler.questions[number-1]
        print(self.question)

        questionNumber = Label(self, text=f"Pytanie {number}")
        questionNumber.grid(row=0, column=4, padx=10, pady=10)

        nextQuestion = Button(self, text="Next Question", command=self.check_answer)
        nextQuestion.grid(row=6, column=1, padx=10, pady=10)

        questionTitle = Label(self, text=self.question['question'])
        questionTitle.grid(row=1, column=2, padx=10, pady=10)

        self.answers = [
            self.question['correct_answer'],
            self.question['incorrect_answers'][0],
            self.question['incorrect_answers'][1],
            self.question['incorrect_answers'][2],
        ]
        random.shuffle(self.answers)

        self.answer = IntVar()
        self.show_answer(0, 2)
        self.show_answer(1, 3)
        self.show_answer(2, 4)
        self.show_answer(3, 5)

    def show_answer(self, id, row):
        r = Radiobutton(self, text=self.answers[id], variable=self.answer, value=id)
        r.grid(row=row, column=1, padx=10, pady=10)

    def check_answer(self):
        self.controller.next_question(self.is_correct())

    def is_correct(self):
        for id, answer in enumerate(self.answers):
            if id == self.answer.get() and answer == self.question['correct_answer']:
                return True
        return False


