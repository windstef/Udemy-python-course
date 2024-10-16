# 166
# Coding Exercise 1

# Create a desktop GUI program that gets feet and inches from the user and outputs the results in meters.

# Solution:
# https://pythonhow.com/coding/d17c1/


import FreeSimpleGUI as sg
from convertor_to_meters import convert_feet_inches_to_meters

label_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches:")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
convert_output = sg.Text("", key="output")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, convert_output]])

while True:
    event, values = window.read()
    print(event, values)    # e.g. Convert {'feet': '24', 'inches': '8'}

    if event == sg.WIN_CLOSED:
        break

    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
    except ValueError:
        print("Your input is not valid. Try again!")
        window["output"].update(value="Your input is not valid. Try again!", text_color="red")
        continue

    meters = convert_feet_inches_to_meters(feet, inches)
    window["output"].update(value=f"{meters} m", text_color="white")

window.close()