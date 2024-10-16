# 167
# Bug-Fixing Exercise 1
# The program down below is supposed to convert kilometers to miles.

# However, when the user runs the code above, enters a number, and presses the Convert button, the program stops, and an error is displayed in the command line:

# TypeError: can't multiply sequence by non-int of type 'float'

# TypeError: unsupported operand type(s) for /: 'str' and 'float'

import FreeSimpleGUI as sg


def km_to_miles(km):
    return km / 1.6


label = sg.Text("Kilometers: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

window = sg.Window('Km to Miles Converter',
                   layout=[[label, input_box], [miles_button, output]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Convert":
            km = float(values["kms"])
            result = km_to_miles(km)
            window['output'].update(value=result)
        case sg.WIN_CLOSED:
            break

window.close()


######### Solution ###########
# https://pythonhow.com/coding/d17b1/

# Explanation
# Line 23 was
# km = values["kms"]
# but it should be
# km = float(values["kms"])
# We need to convert the kilometers to a float type because they are originally a string.
