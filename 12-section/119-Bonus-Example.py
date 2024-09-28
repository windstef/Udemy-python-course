# 119
# Bonus Example

# We're going to create a function which will deepen the understanding
# about functions in Python, and also it'll introduce you to the concept of decoupling.

feet_inches = input("Enter feet and inches: ")

# expected 2 numbers divided by space
# create function to convert that user input, feet and inches to meters.

# Useful:

# help(str.split)
# Help on method_descriptor:
# split(self, /, sep=None, maxsplit=-1) unbound builtins.str method
#     Return a list of the substrings in the string, using sep as the separator string.


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])

    meters = feet * 0.3048 + inches * 0.0254
    # return f"{feet} feet and {inches} inches is equal to {meters} meters"
    return float(meters)    # decoupling output (simplify the function)

# print(convert(feet_inches))
result = convert(feet_inches)

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")