import json

with open('DataEn.json', 'r') as f:
    data = json.load(f)

# Create the data structure
question = input("Question:")
answer = input("Answer:")
new_item = {'question': question, 'answer': answer}
data['data'].append(new_item)

# Write the data to the file
with open('DataEn.json', 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True)
