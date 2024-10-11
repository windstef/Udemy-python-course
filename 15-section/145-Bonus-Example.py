# 145
# Bonus Example

# Target: learn how to work with one of the most important data structures
# and that is JSON.

# Exercise: we are going to build this quiz app

# Today we are going to build this quiz app
# which works like this.
# So you see the command line interface,
# and that's the output of the program.
# So once the user runs the program,
# they are asked several questions, the quiz questions.
# So that is the first question, what are dolphins?
# And then you have several alternatives.
# We show to the user, each of them is numbered,
# so the user can enter a number here.
# For example, if they think one is the correct answer, they enter one.
# In this case three is the correct answer
# because dolphins are mammals.
# So you can press Enter as a user,
# then you get asked the second question:
# what occupies most of the Earth's surface?
# Let's put the incorrect answer this time
# which is one, press Enter.

# The program lists all the questions and it tells the user
# if that question was a correct answer or not.
# And then we show the score to the user which was one out of two.

# Note: output + selection of data structure

# Hint: So a question contains three elements as you see here:
# question text, alternatives and correct answer.

# refer to screenshot:
# 145-Bonus-Example-Question-screenshot.png

# Data structure: a list of dictionaries

# a= [{"question_text":"What are dolphins?",
#   "alternatives": ["Amphibians", "Fish", "Mammals", "Birds"],
#   "correct_answer": 3},
# {"question_text":"What occupies most of the Earth's surface?",
#  "alternatives": ["Land", "Water"],
#  "correct_answer": 2}]

# print(a)

import json

with open("questions.json", 'r') as file:
    content = file.read()

# print(content)  # string
# print(type(content))    # <class 'str'>

data = json.loads(content)  # list of dictionaries (data structrure)

# print(type(data))   # <class 'list'>

score = 0

for question in data:   # each question is a dictionary (list item)
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, "-", alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice   # add new dict item in question dictionary
    # if question["user_choice"] == question["correct_answer"]:
    #     score = score + 1


# display the chosed / correct answers the user made
# iterate the 2nd time with the user's answers in the data list
for index, question in enumerate(data):
    if question["user_choice"] == question["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Wrong Answer"

    message = f"{index + 1} {result} - Your answer: {question['user_choice']}, " \
              f"Correct answer: {question['correct_answer']}"
    print(message)

# print(data)
print(score, "/", len(data))




####################################

# file: questions.json

# list of dictionaries
# [{"question_text":"What are dolphins?",
#   "alternatives": ["Amphibians", "Fish", "Mammals", "Birds"],
#   "correct_answer": 3},
# {"question_text":"What occupies most of the Earth's surface?",
#  "alternatives": ["Land", "Water"],
#  "correct_answer": 2}]


# dictionary of dictionaries
# {"question1":{"question_text":"What are dolphins?",
#   "alternatives": ["Amphibians", "Fish", "Mammals", "Birds"],
#   "correct_answer": 3},
# "question1":{"question_text":"What occupies most of the Earth's surface?",
#  "alternatives": ["Land", "Water"],
#  "correct_answer": 2}}


# python console

# with open("15-section/questions.json") as file:
#     content = file.read()
#
# x = json.loads(content)
# x
# {'question1': {'question_text': "What occupies most of the Earth's surface?", 'alternatives': ['Land', 'Water'],
#                'correct_answer': 2}}
# type(x)
# <class 'dict'>

####################################
