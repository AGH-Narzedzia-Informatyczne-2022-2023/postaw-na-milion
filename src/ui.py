from tkinter import *

from src.question_page import QuestionPage
from src.title_page import TitlePage


class UI():
    window = Tk()
    title = "Tytuł"
    width = 1600
    height = 900
    bg = "#74b9ff"
    question_number = 1

    def __init__(self):
        frame = TitlePage(self.window, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
        self.window_setup()

        self.window.mainloop()


    def window_setup(self):
        self.window.title(self.title)
        #self.window.configure(width=self.width, height=self.height)
        self.window.geometry(f"{self.width}x{self.height}")
        self.window.configure(bg=self.bg)


    def start_quiz(self):
        frame = QuestionPage(self.window, self, self.question_number)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def next_question(self):
        self.question_number += 1
        frame = QuestionPage(self.window, self, self.question_number)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()




