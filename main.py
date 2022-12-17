import find_closest_element
import difflib

own_method = True
data = open('data.txt').read().split("\n")
questions = []
answers = []
for element in data:
    question, answer = element.split(';')
    questions.append(question)
    answers.append(answer)

input = input("Input:")
# us difflib
if not own_method:
    question = difflib.get_close_matches(input, questions, n=5, cutoff=0.7)
    question = question[0]
# use own variant
if own_method:
    question = find_closest_element.find_closest_element(input, questions)

answer = answers[(questions.index(question))]
answer = answer.replace("$n", "\n").replace("$t", "\t")
print(answer)
