class FindOutput:
    def __init__(self):
        self.user_input = ""
        self.remain_words = []

    def get_input(self):
        self.user_input = input("Your Input:")

    def read_important_words(self, filename):
        self.important_words = open(filename).read().split("\n")

    def split_input(self):
        self.user_input_splitted = self.user_input.split(" ")
        print(self.user_input_splitted)
        for element in self.user_input_splitted:
            if element in self.important_words or element.isdigit():
                self.remain_words.append(element)
        print(self.remain_words)

    def find_code_snippet(self):
        code_snippet = ""
        parameters = ""
        # FOR LOOP
        if "for" in self.remain_words and "loop" in self.remain_words:
            for_loop_decision = self.remain_words.index('loop') + 1
            if self.remain_words[for_loop_decision] == "range":
                code_snippet = "for i in range(" + self.remain_words[for_loop_decision + 1] + "):\n\t print(i)"
        # FUNNCTION
        elif "function" in self.remain_words:
            if "name" in self.remain_words:
                name_of_function = self.user_input_splitted[self.user_input_splitted.index('name') + 1]
            elif "named" in self.remain_words:
                name_of_function = self.user_input_splitted[self.user_input_splitted.index('named') + 1]
            print(name_of_function)
            if "parameter" in self.remain_words:
                parameters = self.user_input_splitted[self.user_input_splitted.index('parameter') + 1]
            elif "parameters" in self.remain_words and "and" in self.remain_words:
                parameters = self.user_input_splitted[self.user_input_splitted.index('parameters') + 1]
                parameters = parameters + self.user_input_splitted[self.user_input_splitted.index('and') + 1]
            print(parameters)
        print(code_snippet)


# if __name__ == "__main__":
#     predictor = FindOutput()
#     predictor.get_input()
#     predictor.read_important_words(filename="important_words.txt")
#     predictor.split_input()
#     predictor.find_code_snippet()
