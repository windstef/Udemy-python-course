# 166
# Coding Exercise 1

# Your task for this exercise is to add an Exit button that quits
# the program and apply a black theme to the program you built-in
# yesterday's coding exercise.


# following

# 166
# Coding Exercise 1

# Create a desktop GUI program that gets feet and inches from the user and outputs the results in meters.

# Solution:
# https://pythonhow.com/coding/d18c1/


import FreeSimpleGUI as sg
from convertor_to_meters import convert_feet_inches_to_meters

sg.theme(("black"))     # apply a Black theme

label_feet = sg.Text("Enter feet:")
input_feet = sg.Input(key="feet")

label_inches = sg.Text("Enter inches:")
input_inches = sg.Input(key="inches")

convert_button = sg.Button("Convert")
convert_output = sg.Text("", key="output")

exit_button = sg.Button("Exit")

window = sg.Window("Convertor", layout=[[label_feet, input_feet],
                                        [label_inches, input_inches],
                                        [convert_button, exit_button, convert_output]])

while True:
    event, values = window.read()
    print(event, values)    # e.g. Convert {'feet': '24', 'inches': '8'}

    # if event == sg.WIN_CLOSED:
    #     break

    # # add an Exit button that quits the program
    # if event == "Exit":
    #     break

    # or with match statements for the exit
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

    try:
        feet = float(values["feet"])
        inches = float(values["inches"])
        meters = convert_feet_inches_to_meters(feet, inches)
        window["output"].update(value=f"{meters} m", text_color="white")

    except ValueError:
        print("Your input is not valid. Try again!")
        # window["output"].update(value="Your input is not valid. Try again!", text_color="red")
        # Bug Fixing Exercise 1
        # Solution: https://pythonhow.com/coding/d18b1/
        # the program should show a popup window telling the user to enter numbers in the input boxes.
        sg.popup("Please provide two numbers.", font=("Helvetica", 20))
        continue

    # meters = convert_feet_inches_to_meters(feet, inches)
    # window["output"].update(value=f"{meters} m", text_color="white")

window.close()