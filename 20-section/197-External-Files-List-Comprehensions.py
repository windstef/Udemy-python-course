# 197
# External Files, List Comprehensions

# follows

# 196
# Code Blocks, f-string


##################################


#### External Files ####

## Creating file ##

# Create file with "w" mode
# Note the created file will be at the same level with the python script
with open("book.txt", "w") as file:
    file.write("Hello there!")

# multiline string
content = """Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi.
"""

# Note: it will override the already created book.txt file
with open("book.txt", "w") as file:
    file.write(content)


with open("weather.txt", "w") as file:
    file.writelines(["Clouds\n", "Sun\n", "Rain\n"])


## Reading files ##

# the file must be existed in order to read it. Note "r" mode
with open("book.txt", "r") as file:
    content = file.read()

# the backslashes will not be printed, but newlines will be generated.
print(content)

# Note: reads every line as a separate string and produces a list of those lines
with open("weather.txt", "w") as file:
    content = file.readlines()

# output:
# ['Clouds\n', 'Sun\n', 'Rain\n']

# Note:
# It's important to use a break line after these lines in here
# if you want them to be separated in separate lines,
# when you read this, of course, you'll read it together
# with those \n as you see down here.



#### List Comprehensions ####

# If you want to get rid of those \n,
# you can use list comprehensions.

# Iteration in the read file content.
# So for each string in the content list,
# stripping out the string from those \n

clean_content = [item.strip("\n") for item in content]

# output:
# ['Clouds', 'Sun', 'Rain']
