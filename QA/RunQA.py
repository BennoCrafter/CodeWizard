import json
import QA.find_nearest


class GetAnswer:
    def __init__(self):
        self.question_answer_dict = {}
        self.questions = []

    def read_and_split_data(self, filename):
        # Open the .json file
        with open(filename, 'r') as f:
            data = json.load(f)

        # Iterate through the data array and read data
        for item in data['data']:
            question = item['question']
            question.lower()
            answer = item['answer']
            self.question_answer_dict[question] = answer

        self.questions = [v for v in self.question_answer_dict.keys()]

    def get_input(self, ask):
        output = QA.find_nearest.find_nearest(self.questions, ask)
        answer = self.question_answer_dict.get(output)
        print(answer)


# if __name__ == "__main__":
#     qa = GetAnswer()
#     qa.read_and_split_data(filename="/Users/benno/PythonProjects/CodeWizard/QA/DataCodeExamples.json")
#     qa.get_input(ask=input("Input:"))
