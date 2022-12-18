import find_closest_element
import difflib
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter

own_method = True
questions = []
answers = []
data = open('data.txt').read().split("\n")
ask = input("Input:").lower()


def split_answer_and_question():
    for element in data:
        question, answer = element.split(';')
        questions.append(question)
        answers.append(answer)


def find_closest_match():
    global question
    # us difflib
    if not own_method:
        question = difflib.get_close_matches(ask, questions, n=5, cutoff=0.7)
        question = question[0]
    # use own variant
    if own_method:
        question = find_closest_element.find_closest_element(ask, questions)

    answer = answers[(questions.index(question))]
    answer = answer.replace("$n", "\n").replace("$t", "\t")
    print("My Answer is: \n " + highlight(answer, PythonLexer(), TerminalFormatter()) + "\n")

    # feedback
    feedback = input("Was this correct?(yes no):")
    if feedback.startswith("y"):
        feedback = "CORRECT!"
        deeper_feedback = "Question: " + ask + " Expected ask: " + question + " Expected answer: " + answer
    elif feedback.startswith("n"):
        feedback = "WRONG!"
        deeper_feedback = "Question: " + ask + " Expected ask: " + question + " Expected answer: " + answer
    with open('feedback.txt', 'w') as f:
        f.write("Feedback: " + feedback + "   ||||   Deeper Feedback: " + deeper_feedback)

    print("Thank you for your feedback!")


split_answer_and_question()
find_closest_match()
