# 195

# Methods, Lists, Tuples, Dictionaries


###############################

## Methods ##

# Note: they are associated with a certain type/object
# and also be applied to the variable which is holding the object.

"hello there".upper()
# 'HELLO THERE'

"hello there".capitalize()
# 'Hello there'

"hello there".title()
# 'Hello There'

greeting = "hello there"
greeting.title()
#'Hello There'

# String are IMMUTABLE.

## Methods that return an output ##

# It returns a new string, but does not modify the original
greeting.title()
# 'Hello There'


# List methods modify the original list
# Lists are MUTABLE
groceries = ["vinegar", "olives", "bread"]
groceries.append("apples")      # It does not return an output

# groceries
# ['vinegar', 'olives', 'bread', 'apples']

groceries.sort()
# groceries
# ['apples', 'bread', 'olives', 'vinegar']

## A list of methods ##
# use the dir() method, e.g.
# string: dir(str)
# lists: dir(list)

# or an instance of a class
# e.g.: dir(greeting), dir(groceries)


#### How to create new methods? ####
# The methods are connected to the object types (class)
# First, you need to learn how to create classes.
# To be learned to the advanced level of the course ...


## Lists and tuples ##

# Lists # are most to store homogeneous items
groceries = ["vinegar", "olives", "bread"]

# Tuples are IMMUTABLES
# are most to store heterogeneous items
# Like strings, tuples also have no methods that modify the original
values = (1920, 1080, "grayscale", "JPG")

values.append() # It will Not work


# Indexing #
string = "vinegar"
groceries = ["vinegar", "olives", "bread"]
values = (1920, 1080, "grayscale", "JPG")

groceries[0]    # first item
# 'vinegar'

groceries[2]    # 3rd item
# 'bread'

values[2]   # 3rd item
# 'grayscale'

string[2]   # 3rd character

# Negative indexing
# You might want to use negative indexing
# when you are accessing items which are closer to the end
# of an array, array, I mean, a list or a tuple or string.
# Also called sequence.
# So these are also known as sequence types.

string[-1]      # last item
# 'r'

# Access a slice/range

values[1:3]   # Note: it returns the items with index 1 and index 2. The item with index 3 is not included.
# (1080, 'grayscale')

# Negative slice/range indexing
values[-3:-1]   # Note: it returns the items with index -3 and index -2. The item with index -1 is not included.
# (1080, 'grayscale')



## Dictionaries ##

# Hint:
# You should use dictionaries to store your data
# when your values are more heterogeneous,
# and it's important to have labels on them.
# key/values

john = {"first name": "John", "last name": "smith", "age": 40}

# access with the key
john["last name"]
# 'smith

# Dictionaries can also be inside other items such as lists.
# list with items dictionaries
persons1 = [{"first name": "John", "last name": "smith", "age": 40},
            {"first name": "laura", "last name": "eager", "age": 45},
            {"first name": "sim", "last name": "agraval", "age": 42}]

persons1[1]
# {'first name': 'laura', 'last name': 'eager', 'age': 45}

persons1[2]["first name"]
# 'sim'


# Hint:
# in certain applications, depending on the scenario,
# you may want to store those data differently.
# For example, here, we also have data about persons,
# but this will be a dictionary.
# key, value is a list
persons2 = {"first name": ["John", "laura", "sim"],
            "last name": ["smith", "eager", "agraval"],
            "age": [40, 45, 42]}

persons2['age']
# [40, 45, 42]

persons2["first name"][2]
# sim
