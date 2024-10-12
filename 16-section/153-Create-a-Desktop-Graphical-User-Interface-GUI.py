# 153
# Create a Desktop Graphical User Interface (GUI)

# Target:
# By the end of this video, you will have learned how to create this graphical user interface.
# This has four elements.
# First, it is the window which contains everything the window elements.
# Then it contains this label which writes type in a to do.
# Then it contains this input text box and then it contains this button.
# So you will learn how to create all these four elements the window, the label,
# the input box and the button.

# file aka gui.py

# type to use for: window, text box, button
# these kinds of objects, they don't exist by default in Python.
# Python does have a standard module called Tkinter or Tkinter, so that's a standard library, but I
# would prefer to use a more advanced library.
# And this advanced library is made available as a third party module or library.

# A complete list of Python third party libraries can be found on
# pypi.org

# type for search term: freesimplegui

# the library we're going to use to create our graphical user interface.
# So the Python files of this library contain those special types the button, the window, etc..

# https://pypi.org/project/FreeSimpleGUI/

# If I click over here, it's going to take me to the homepage of this library.
# And up here you see this (command to by typed in the terminal, not in the Python console)
# pip install FreeSimpleGUI
# That is the command that copies all the Python files of this library and puts them on your computer.

# 2 ways to install the 3rd party module (library)
# a. PyCharm > Settings > Project (expand) > + Install the package FreeSimpleGUI
# b. execute in the console the command: pip install FreeSimpleGUI

# So what is Pip?
# Pip is also a third party library for Python.
# And pip is used to install other third party libraries.

###############################

# import functions
# import FreeSimpleGUI

# error:
#   File "/home/stefkour/PycharmProjects/app1/pythonProject/venv/lib/python3.12/site-packages/FreeSimpleGUI/__init__.py", line 23, in <module>
#     import tkinter as tk
# ModuleNotFoundError: No module named 'tkinter'

# Solution, follow guidelines from
# https://www.geeksforgeeks.org/how-to-fix-modulenotfounderror-no-module-named-tkinter/

# execute the command:
# sudo apt-get install python3-tk

# verify with:
# from tkinter import *


# Resources
# PySimpleGUI Cookbook
# https://docs.pysimplegui.com/en/latest/cookbook/


##################

import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])       # 2 rows: each row in the GUI has to be a list. The outer list of rows (lists)
window = sg.Window('My To-Do App', layout=[[label], [input_box], [add_button]])       # 3 rows: each row in the GUI has to be a list. The outer list of rows (lists)
window.read()
print("Hello")
window.close()

