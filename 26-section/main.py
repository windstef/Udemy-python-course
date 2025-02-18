## 247. Programming Tool/Concept of the Day: Using the PyCharm Debugger


## 1st part ##
# text = "I love sun"
# word = "love"
#
# # convert to list of strings, words space separated
# # on purpose error for debugging breakline
# # words = text.sleep(" ")
# words = text.split(" ")
#
# # on purpose error for debugging
# # count = text.count("word")
# count = text.count(word)
#
# frequency = count / len(words) * 100
# print(frequency)



##################
# debugging with functions
## 2nd part ##

message = "Hello"
import glob

def get_frequency(text, word):
    # error for debugging
    # words = text.sleep(" ")
    words = text.split(" ")
    glob.glob("*")
    # error for debugging
    # count = text.count("word")
    count = text.count(word)
    frequency = count / len(words) * 100
    return frequency

frequency = get_frequency("I love sun", "love")
if frequency > 5:
    print("High frequency")
else:
    print("Low frequency")

print(message)