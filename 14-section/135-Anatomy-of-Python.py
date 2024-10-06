# 135
# Anatomy of Python

# So the key concept to take
# from this video was the distinction
# between classes or types, in other words,
# and the instances that these classes create.

def get_todos(filepath="todos.txt"):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(filepath, 'r') as file_local:
        # yellow underlined todos: Shadows name 'todos' from outer scope. And it's not a good idea to have this variable with the same name as in function.
        # todos = file.readlines()
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todos))


# no return anything, except of None. Behaves as procedure.
# with default argument/parameter
# Hint: non-default parameter must not follows default parameters
def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# docstring
# print(help(write_todos))