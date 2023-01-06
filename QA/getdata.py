import requests
from bs4 import BeautifulSoup
import json

link = "https://stackoverflow.com/questions/44472162/how-can-i-play-audio-playsound-in-the-background-of-a-python-script" # works

# Make a request to the website
response = requests.get(link).text

# Parse the HTML of the page
soup = BeautifulSoup(response, 'html.parser')

# Find all elements with the class "s-prose js-post-body"
element = soup.find_all('div', {"class": 's-prose js-post-body'})

question = element[0].get_text()
answer = element[1].get_text()
print("Question:", question)
print("Answer:", answer)

if input("Do you want to write it into the Dataset(yes,no)?").startswith("y"):
    # write into file
    # Read the JSON file
    with open('DataCodeExamples.json', 'r') as f:
        data = json.load(f)

    # Add a new item to the list
    new_item = {'question': question, 'answer': answer}
    data['data'].append(new_item)

    # Write the modified data back to the file
    with open('DataCodeExamples.json', 'w') as f:
        json.dump(data, f, indent=2, sort_keys=True)

else:
    exit()