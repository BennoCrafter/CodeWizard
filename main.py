import find_closest_element

data = open('example.txt').read().split("\n")
questions = []
answers = []
for element in data:
    question, answer = element.split('|')
    questions.append(question)
    answers.append(answer)

input = input("Input:")
question = find_closest_element.find_closest_element(input, questions)
answer = answers[(questions.index(question))]
answer = answer.replace("$n", "\n").replace("$t", "\t")
print(answer)