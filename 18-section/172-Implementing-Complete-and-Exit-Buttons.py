# 172
# Implementing Complete and Exit Buttons


# following:

# 163
# Implementing an "Edit" Button


# two things today:

# 1 add a Complete button #next to the Edit button.
# It will delete the selected to-do.
# So we select a to-do, press Complete.
# The to-do is deleted from todos.txt
# and also from this list box,


# 2 add Exit button
# It  will close the program.
# So the Exit button will be an addition to this button.

##################

import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])       # 2 rows: each row in the GUI has to be a list. The outer list of rows (lists)
window = sg.Window('My To-Do App',
                   layout=[[label],
                           [input_box], [add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))       # 3 rows: each row in the GUI has to be a list. The outer list of rows (lists)

while True:

    # event = window.read()
    event, values = window.read()

    print(1, event)    # tuple, e.g. ('Add', {'todo': 'Hi'}) | or with 2 variables event: Add
    print(2, values)   # {'todo': 'hi'}
    # print(3, values['todos'])

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + '\n'     # update the todos list
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)      # Remove first occurrence of value.
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:     # {'todo': None}
            break

window.close()