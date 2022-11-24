import random
from tkinter import *


class QuestionPage(Frame):
    def __init__(self, parent, controller, number):
        Frame.__init__(self, parent)

        question = controller.question_handler.questions[number-1]
        print(question)

        questionNumber = Label(self, text=f"Question {number}")
        questionNumber.grid(row=0, column=4, padx=10, pady=10)

        nextQuestion = Button(self, text="Next Question", command=controller.next_question)
        nextQuestion.grid(row=6, column=1, padx=10, pady=10)

        questionTitle = Label(self, text=question['question'])
        questionTitle.grid(row=1, column=2, padx=10, pady=10)

        answers = [
            question['correct_answer'],
            question['incorrect_answers'][0],
            question['incorrect_answers'][1],
            question['incorrect_answers'][2],
        ]
        random.shuffle(answers)

        self.answer = IntVar()
        self.show_answer(answers[0], 2)
        self.show_answer(answers[1], 3)
        self.show_answer(answers[2], 4)
        self.show_answer(answers[3], 5)

    def show_answer(self, text, number):
        r = Radiobutton(self, text=text, variable=self.answer, value=number)
        r.grid(row=number, column=1, padx=10, pady=10)

