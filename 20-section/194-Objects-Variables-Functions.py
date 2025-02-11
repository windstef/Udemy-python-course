# 194
# Objects, Variables, Functions


# Note:
# I've placed the code already in something called Jupyter Lab.
# So what you're looking at is a tool called Jupyter Lab.
# In Jupyter Lab, you can write in code and execute it
# but that is something that you learn in day 30.


####################################################

#### Objects and variables ####

## Objects can be stored in variables ##

# Strings
name = "John"
last_name = "Smith"
id = "10221"

# numbers
members = 5     # integer
height = 1.75   # float

## Objects can also be produced by functions ##

name = input("What is your age?")

height = input("What is your height?")      # Note, it is stored as a STRING


## Converting to another type

height = float(input("What is your height?"))       # Converts to a float (if its number)


#### Functions ####

## Not all functions return a value ##

x = print("Hello")      # The print function does Not return a value.

## Custom functions can also return or not a value ##

def foo():
    value = 10
    return value

x = foo()   # it returns x assigned to 10


def foo():
    value = 10

x = foo()       # it does not return anything, so x is not assigned to anything (None)


# Return vs Print #

def foo1():
    value = 10
    return value

def foo2():
    value = 10
    print(value)

x1 = foo1()      # It assigns x to returned 10

x2 = foo2()   # It assigns x2 to nothing. The called function prints the output '10'


## Functions with parameters/arguments ##

def foo(number):
    result = number * number
    return result

# With argument name
x = foo(number=10)      # result: 100

# Without argument name
x = foo(10)      # results: 100


## Functions with multiple parameters/arguments ##

def foo(number1, number2):
    result = number1 * number2
    return result

x = foo(10, 20)     # result: 200


## Functions with default parameters/arguments ##

def foo(number1, number2=2):
    result = number1 * number2
    return result

# The default argument can be omitted
x = foo(10)     # result: 20

x = foo(10,3)   # result: 30