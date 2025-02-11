# 198
# Errors, Comments, Modules, Libraries, Web and Desktop GUIs


# follows:
# 197
# External Files, List Comprehensions


##########################################3


#### Errors ####

## Syntax Errors ##

content = ['Clouds\n', 'Sun\n', 'Rain\n']

# example
# clean_content = [item.strip("\n") for item in content)

# SyntaxError: closing parenthesis ')' does not match opening parenthesis '['

# clean_content = [item,strip("\n") for item in content]

# SyntaxError: did you forget parentheses around the comprehension target?


## Exceptions ##

# clean_content = [item.strip("\n") for item in apples]

# NameError: name 'apples' is not defined


clean_content = [item.streap("\n") for item in content]

# AttributeError: 'str' object has no attribute 'streap'. Did you mean: 'strip'?

# Note: a method is actually an attribute


year_of_birth = int(input("Enter the year: "))
current_year = 3221
age = current_year = year_of_birth
print(age)

# Enter the year: 12.12.3001

# ValueError: invalid literal for int() with base 10: '12.12.3001'


## Exceptions ##

current_year = 3221     # Put code like this outside if you can

try:
    year_of_birth = int(input("Enter the year: "))
    age = current_year - year_of_birth
    print(age)
# except:
except ValueError:
    print("The format should be YYYY")


## Try-except does not catch syntax errors ##

current_year = 3221     # Put code like this outside if you can

try:
    year_of_birth = int(input("Enter the year: "))
    age = current_year - year_of_birth
    # print(age
except:
    print("The format should be YYYY")


# When to use try-except and when to use if-elif-else

current_year = 3221     # Put code like this outside if you can

try:
    year_of_birth = int(input("Enter the year: "))
    age = current_year - year_of_birth
    if age < 150:
        print(age)
    else:
        print("Age too big")
except:
    print("The format should be YYYY")


#### Comments and doc strings ####

# Doc strings are used to document what a function does.
# So you place them inside the function definition
# and you use these triple quotes here and there.

def area(a, b):
    """Calculate the area of a rectangle
    given its two sides
    """
    return a * b

# simple comment. Use if its really useful!
# Call the function
rectangle_area = area(10, 20)


#### Modules ####

# Modules are Python files
# which can be imported into another Python file.

# prerequisite there is a myfile.py with the defined function area()
# import myfile

# rectangle_area = myfile.area(10, 20)


#### Standard libraries ####

# Standard libraries are also Python files.
# They can be one single .py file or multiple files.

import glob
import requests

glob.glob("*.txt")
# ['weather.txt', 'book.txt']

# Hint:
# what you call this a method or a function,
# but if you really want to find out in Python,
# you can right click and then you can go to the go-to menu
# and then go to implementations.


response = requests.get("https://example.com")
content = response.text
content


#### Third party libraries ####

# Third party libraries are libraries
# which have not been included with a Python interpreter.
# So you have to install them with pip install followed by the library name.
# pip install library_name


#### Web apps ####

# Web apps need a third party library,
# also known as a framework, a web framework such as streamlit.



#### Desktop GUI app ####

# We also covered PySimpleGUI,
# a library to create desktop GUI apps.