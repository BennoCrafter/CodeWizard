import json
import find_nearest

question_answer_dict = {}

# Open the .json file
with open('/Users/benno/PycharmProjects/CodeWizard/DataEn.json', 'r') as f:
    data = json.load(f)

# Iterate through the data array and read data
for item in data['data']:
    question = item['question']
    question.lower()
    answer = item['answer']
    question_answer_dict[question] = answer

questions = [v for v in question_answer_dict.keys()]


ask = input("Input:")
output = find_nearest.find_nearest(questions, ask)
answer = question_answer_dict.get(output)
print(answer)
