# 178
# Programming Tool/Concept of the Day:
# Creating a Standalone Executable

# following:
# 173
# Final Touches


# Target:
# how to convert your Python scripts, your Python programs,
# into standalone executables,
# which can run on Windows, Mac, and Linux.


# Note:
# The process to create executable files is different on Windows, Mac, and Linux
# for Linux go to minute 18:52

# 3rd party package: PyInstaller
# PyInstaller bundles a Python application and all its dependencies into a single package. The user can run the packaged app without installing a Python interpreter or any modules.

# terminal, linux command:
# pyinstaller --onefile --windowed --clean 178-Programming-Tool-Concept-of-the-Day-Creating-a-Standalone-Executable.py

# output, final:
# 66149 INFO: Building EXE from EXE-00.toc completed successfully

# file generated the executable file:
# path: /home/stefkour/PycharmProjects/app1/pythonProject/18-section/dist
# file: 178-Programming-Tool-Concept-of-the-Day-Creating-a-Standalone-Executable
# share this with the others

# the todos.txt file is generated automatically, as programmed below.

from anyio.abc import value

# 3 things

# following:

# 172
# Implementing Complete and Exit Buttons


# First, we're going to fix a couple of errors that we have.
# We're going to handle them using try and accept.

# Second, we're going to add a live date and time
# with a second sticking on the gui.

# And third, we're going to polish the program,
# change the theme of the program, play around with the sizes
# of the elements, and so on.


## ## ## ##
# 1
# So when the user runs the program
# and without selecting anything, they press on edit.
# Then we get this error, index error.

# IndexError: list index out of range
# 1 Edit
# 2 {'todo': '', 'todos': []}

# We have the same issue with complete, the complete case.
# So if the user presses complete without selecting an item,
# we still have an error here.


# Tip:
# I do suggest you to use the rainbow plugin
# which you can install by going to settings
# and then going to plugins and then going to marketplace
# and search for rainbow, install it, then restart PyCharm.
# And what that plugin does is it colors the brackets,
# parenthesis and brackets.
# So now this yellow parenthesis corresponds to that yellow parenthesis.


###########################################


import functions
import FreeSimpleGUI as sg
import time


import os

# control if the todos.txt file exists, otherwise create it
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", size=10)
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])       # 2 rows: each row in the GUI has to be a list. The outer list of rows (lists)
window = sg.Window('My To-Do App',
                   layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=('Helvetica', 20))       # 3 rows: each row in the GUI has to be a list. The outer list of rows (lists)

while True:
    event, values = window.read(timeout=200)     # the loop runs every 200ms, to see the actual time
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    # print(1, event)    # tuple, e.g. ('Add', {'todo': 'Hi'}) | or with 2 variables event: Add
    # print(2, values)   # {'todo': 'hi'}
    # print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + '\n'     # update the todos list
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                # print("Please select an item first.")
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)      # Remove first occurrence of value.
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                # print("Please select an item first.")
                sg.popup("Please select an item first.", font=("Helvetica", 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:     # {'todo': None}
            break

window.close()
