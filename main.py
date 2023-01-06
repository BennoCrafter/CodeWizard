from CodeDetection.predict import Predict
from GenerateCode.search_right_CodeSnippet import FindOutput
from QA.RunQA import GetAnswer


class GetUserInput:
    def __init__(self):
        # objects
        self.code_detection = Predict()
        self.code_generation = FindOutput()
        self.q_and_a = GetAnswer()

    def get_user_input(self, user_input):
        if user_input == 1:
            self.code_detection.do_math()
            if self.code_detection.from_txt_file:
                self.code_detection.get_output(user_input=input("Whats the file path?:"), txt=True)
            else:
                self.code_detection.get_output(user_input=input("What do you want to check?:"), txt=False)

        elif user_input == 2:
            self.code_generation.read_important_words(filename="GenerateCode/important_words.txt")
            self.code_generation.get_input()
            self.code_generation.split_input()
            self.code_generation.find_code_snippet()

        elif user_input == 3:
            self.q_and_a.read_and_split_data(filename="/Users/benno/PythonProjects/CodeWizard/QA/DataCodeExamples.json")
            self.q_and_a.read_and_split_data(filename="/Users/benno/PythonProjects/CodeWizard/QA/DataCodeExamples.json")
            self.q_and_a.get_input(ask=input("Input:"))

        else:
            print("There is something wrong!")


if __name__ == "__main__":
    start = GetUserInput()
    start.get_user_input(user_input=int(input("What dou you want to do?: [1: Detect Code | 2: Generate Code | 3: Ask coding Questions]")))