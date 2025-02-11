# 183
# Adding New Todo Items on the Web App

# following

# 182
# Create a Web App

# How to run:
# terminal:
# streamlit run 183-Adding-New-Todo-Items-on-the-Web-App.py

# Target:
# implement the feature of adding new todos to the todo items.

# So far in the course, we built a command line interface
# and also a desktop graphical user interface for our Todo app.

# So today, you're going to learn how to build a web interface.
# So that is a web app.

# The users can just visit the URL of your web app
# and they can use your app.


# So if you want to create a graphical user interface,
# you have the option of a desktop graphical user interface
# or the option of a web graphical user interface.
# So this is also referred to as a GUI,
# but it's a web GUI.

# First, let me demonstrate you how the app works.
# So the user has a list of existing Todos.
# These Todos come from that same todos.txt file.
# So we are reusing the backend of our program
# because we did create a good design for our program
# so we can extend it now.

# Note: we're going to use the streamlit library to create web apps.
# It also integrates very well with graphs.
# So you can create data dashboards,
# data apps where you show graphs and widgets
# like sliders and text boxes and buttons
# which interacts with your graphs.
# And it's also very easy to deploy your apps
# so you can make your apps public very easily
# so that everyone can use them.

# run command (terminal):

# $ streamlit run 182-Create-a-Web-App.py
#
#   You can now view your Streamlit app in your browser.
#
#   Local URL: http://localhost:8501
#   Network URL: http://192.168.1.4:8501


#######################################

import streamlit as st
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

for todo in todos:
    st.checkbox(todo)
    # print(todo)

st.text_input(label="Enter a todo:", placeholder="Add new todo ...",
              on_change=add_todo, key='new_todo')

print("Hello from bottom")

st.session_state