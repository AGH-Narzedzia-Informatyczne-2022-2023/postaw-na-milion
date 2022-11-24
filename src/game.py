from .question_handler import QuestionHandler
from .ui import UI


class Game:
    UI

    def __init__(self):
        print("Game stworzony")
        self.question_handler = QuestionHandler()
        self.UI = UI()
