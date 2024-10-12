# 156
# Coding Exercise 1
# Write a script that generates the following GUI.

#  Solution:
# https://pythonhow.com/coding/d16c1/

import FreeSimpleGUI as sg

feet_label = sg.Text("Enter feet:")
feet_input = sg.Input()

inches_label = sg.Text("Enter inches:")
inches_input = sg.Input()

button = sg.Button("Convert")

window = sg.Window("Convertor",
                   layout=[[feet_label, feet_input],
                           [inches_label, inches_input],
                           [button]])

window.read()
window.close()