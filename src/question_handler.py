from src.api_question_getter import ApiQuestionGetter


class QuestionHandler:
    question_count = 10
    questions = []

    def __init__(self):
        self.api = ApiQuestionGetter()

    def load_questions(self):
        self.questions = self.api.get_questions(self.question_count)
