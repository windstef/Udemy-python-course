# 144
# Code Experiments

# Introduction of 4 important modules

# csv	Write and read tabular data to and from delimited files.
# https://docs.python.org/3/library/csv.html#module-csv

# glob	Unix shell style pathname pattern expansion.
# https://docs.python.org/3/library/glob.html#module-glob

# shutil	High-level file operations, including copying.
# https://docs.python.org/3/library/shutil.html#module-shutil

# webbrowser	Easy-to-use controller for web browsers.
# https: // docs.python.org / 3 / library / webbrowser.html  # module-webbrowser


####################################

# glob
# get a list of file paths
# that satisfy a file pattern.

# import glob
#
# myfiles = glob.glob("files/*.txt")
#
# print(myfiles)
#
# for filepath in myfiles:
#     with open(filepath, 'r') as file:
#         print(file.read())

####################################

# csv
# csv is able to process csv files

# import csv
#
# with open("files/weather.csv", 'r') as file:
#     data = list(csv.reader(file))
#
# print(data)     # data = list of lists
# # [['Station', 'Temperature'], ['Kuala Lumpur', '45'], ['New York', '20']]
#
# city = input("Enter a city: ")
#
# for row in data[1:]:    # each row is a list / starting from the 2nd list, skip the Station,Temperature
#     if row[0] == city:  # row[0] is the 1st item of the row list
#         print(row[1])  # row[1] is the 2nd item of the row list


# ['Station', 'Temperature']
# ['Kuala Lumpur', '45']
# ['New York', '20']


####################################

# shutil

# shell utils
# you can copy files, you can create zip files,
# you can extract files from zip files, etc

# we will get these two text files and we'll create a zip file
# with these files inside the zip file.
# So we give the name of the output file.

# import shutil

# shutil.make_archive("output", "zip", "files")



####################################

# webbrowser

# build a Google searcher basically.

# So we're going to receive a search term
# from the user and we are going to open the browser,
# searching for that term on Google.

import webbrowser

user_term = input("Enter a search term: ")

# webbrowser.open("https://google.com")


# from web browser the url (interesting) is:
# example
# https://www.google.com/search?q=python+website

# webbrowser.open("https://www.google.com/search?q=python+website")

# webbrowser.open("https://google.com/search?q=" + user_term)

# e.g.
# https://www.google.com/search?q=kerkyra%20time

# in case:
# replace spaces with plus +, then use the

webbrowser.open("https://google.com/search?q=" + user_term.replace(" ", "+"))

# e.g.
# https://www.google.com/search?q=kerkyra+winter
