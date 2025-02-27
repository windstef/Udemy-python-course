# Section 19: Day 19: App 1 - Build a Todo List App | #web-apps
# !86
# Code Experiments



# 185
# Deploying the Web App to the Cloud


# following

# Section 19:
# 184
# Completing Todo Items on the Web App



# How to run:
# terminal:
# streamlit run web.py

# generate the requirements.txt file via command:
# pip freeze > requirements.txt


# Q. what is requirements.txt?

# This is a file which will be uploaded to the server
# where we host this web app.
# So that server should know
# all the Python libraries the server needs to install
# in order to run the web app correctly.

# show the list of those packages in the command line:
# pip freeze

# 1st push the project to github
# deploy via streamlit free cloud service
# sign-in via github account
# url: https://app1-1-todo-list.streamlit.app/


## Code Experiments (4) ##

# 1st experiment:
# The first thing I wanted to show you is that the order
# of the widgets, the components matter.

# 2nd experiment:
# provided HTML instead of a plain string.

# 3rd experiment:
# try is the first one is st.set_page_config.
# This is a method which allows you to configure the page.
# You can set the argument layout to wide
# and let's refresh the page to see how it will change.
# So you see that now the horizontal length of the webpage
# expands the entire width of the browser
# and it's still responsive.
# So you see that the button here,
# the text box is shrinking when we shrink the webpage.
# So that will also work for mobile devices.


# 4th experiment:
# how to have multiple pages for your web apps.
# All you have to do is go to the root directory
# of your project where you have the main web.py file
# and here you want to create a new folder, name it pages.

# So pages, exactly pages, don't change the name.
# And then inside the folder, you add pages.
# So these are Python files for example About.py.

###################################

from tabnanny import check



# How to run:
# terminal:
# streamlit run web.py

# generate the requirements.txt file via command:
# pip freeze > requirements.txt


# Q. what is requirements.txt?

# This is a file which will be uploaded to the server
# where we host this web app.
# So that server should know
# all the Python libraries the server needs to install
# in order to run the web app correctly.

# show the list of those packages in the command line:
# pip freeze

# 1st push the project to github
# deploy via streamlit free cloud service
# sign-in via github account
# url: https://app1-1-todo-list.streamlit.app/

#######################################

import streamlit as st
from PIL.ImageMath import unsafe_eval
from streamlit import checkbox

import functions

print("Hello from header")

todos = functions.get_todos()

# 3rd experiment:
# st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"    # st.session_state is sort of dictionary of streamlit
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")

# st.write("This app is to increase your productivity.")
# 2nd experiment: (Note: html is available for the write method)
st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)
# st.write("<h1>This app is to increase your <b>productivity</b>.</h1>",
#          unsafe_allow_html=True)

# st.checkbox("Buy grocery.")
# st.checkbox("Throw the trash")

# 1st experiment: move the input before the checkboxes
# st.text_input(label="Enter a todo:", placeholder="Add new todo ...",
#               on_change=add_todo, key='new_todo')


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
