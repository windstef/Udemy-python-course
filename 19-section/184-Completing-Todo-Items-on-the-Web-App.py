# 184
# Completing Todo Items on the Web App
from tabnanny import check

# following


# 183
# Adding New Todo Items on the Web App

# Target:
# implement the complete todo features.
# So when the user checks one todo item,
# that todo item should be removed from this list,
# and also from the list of todos.txt items.


# How to run:
# terminal:
# streamlit run 184-Completing-Todo-Items-on-the-Web-App.py



# Q. why is session_state not displaying
# the information about these other widgets
# such as the checkboxes?

# The answer is that the checkboxes
# don't have a key argument yet,
# but the text_input box does have one.


#######################################

import streamlit as st
from streamlit import checkbox

import functions

print("Hello from header")

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"    # st.session_state is sort of dictionary of streamlit
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

# st.checkbox("Buy grocery.")
# st.checkbox("Throw the trash")

for index, todo in enumerate(todos):
    # st.checkbox(todo)
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        # print(checkbox)
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')

# print("Hello from bottom")

# st.session_state