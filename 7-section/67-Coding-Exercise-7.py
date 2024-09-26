# Coding Exercise 7

# Please download the three text files a.txt, b.txt, and c.txt from the resources and place them in your computer IDE.
#
# Then, create a program that:
#
# 1. reads each text file and
#
# 2. prints out the content of each file in the command line.
#
# The expected output would be like the following:
#
# I am a.
# I am b.
# I am c.


# filenames = ["a.txt", "b.txt", "c.txt"]
#
# for filename in filenames:
#     file = open("files/files-coding-exercise-7/" + filename, 'r')
#     print(file.read())


####

# Solution
# https://pythonhow.com/coding/d6c5/

# filenames = ['a.txt', 'b.txt', 'c.txt']
#
# for filename in filenames:
#     file = open(filename, 'r')
#     content = file.read()
#     print(content)


########

# 69. Bug fixing Exercises

# The code creates a text file which contains the following content:
#
# 100.12111.23
#
# However, the correct content should be:
#
# 100.12
#
# 111.23
#
# Please fix the code so it creates the file with the correct content.

# file = open("files/data.txt", 'w')

# file.write("100.12")
# file.write("111.23")

# Solution:
# https://pythonhow.com/bug-fixing/d6b1/
# file.write("100.12\n")
# file.write("111.23\n")
#
# file.close()




####
# Bug-Fixing Exercise 2: The code below tries to write the string "100.2" to the text file.
# However, there is an error. Try to fix the error.

# file = open("files/data.txt", 'r')

# Error: io.UnsupportedOperation: not writable
# Solution
# https://pythonhow.com/bug-fixing/d6b2/
file = open("files/data.txt", 'w')


file.write("100.12")
file.close()


