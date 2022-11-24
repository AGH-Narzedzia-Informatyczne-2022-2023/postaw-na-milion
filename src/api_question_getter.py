import requests


class ApiQuestionGetter:
    url = "https://opentdb.com/api.php?"

    def get_n_questions(self, amount):
        return self.get_questions({'amount': amount})

    def get_questions(self, dict):
        parameters = []
        for parameter, value in dict.items():
            parameters.append(f'{parameter}={value}')

        url = self.url + '&'.join(parameters)
        response = requests.get(url)
        questions = response.json()["results"]
        return questions
