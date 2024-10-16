# 162
# Implementing an Add Todo Button

# following:
# 153
# Create a Desktop Graphical User Interface (GUI)


# two things today:

# First, we're going to make this window bigger,
# all the fonts, all the buttons, the text boxes,
# it's going to look bigger.

# And then the second thing is,
# we are going to implement this Add button.
# So if the user enters a todo here and they press the button,
# that todo item is going to be stored in the todos.txt file.

##################

import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])       # 2 rows: each row in the GUI has to be a list. The outer list of rows (lists)
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 20))       # 3 rows: each row in the GUI has to be a list. The outer list of rows (lists)

while True:

    # event = window.read()
    event, values = window.read()

    print(event)    # tuple, e.g. ('Add', {'todo': 'Hi'}) | or with 2 variables event: Add
    print(values)   # {'todo': 'hi'}
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:     # {'todo': None}
            break

window.close()