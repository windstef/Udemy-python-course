# 102
from reprlib import aRepr

# In the code experiment video, you understood the difference

# between syntax errors and exceptions.

# Now there is another type of issue which neither the grammar checker of the interpreter,
# nor the interpreter itself can capture.

# These are more logical issues which only humans can spot in a program,
# and for that you need to use different tools.

# So to discover what these issues are exactly, I will create a program which asks the user
# to enter the dimensions of a rectangle and the program should output the area of the rectangle.


try:
    width = float(input("Enter rectangle width: "))
    length = float(input("Enter rectancle length: "))

    # Scenario: we don't accept square calculations of areas in our program".
    # So we want to show a message to the user.
    if width == length:
        exit("That looks like a square.")

    area = width * length

    print(area)
except ValueError:
    print("Please enter a number.")


# Conclusion:
# So "if" conditionals do not catch errors, they check values.
# That's something I wanted you to keep in mind
# and that's what I was trying to demonstrate
# with this example.
# So the difference between "try" "accept"
# and the "if" conditionals.
