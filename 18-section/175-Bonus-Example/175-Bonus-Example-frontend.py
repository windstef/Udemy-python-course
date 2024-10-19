# 175
# Bonus Example
# Frontend

# Remarks
# 1. Design the Frontend
# 2. Code the Frontend
# 3. Code the Backend
# 4. Finish Up


# Target: create a program which extracts a zip file to a destination directory.

# follow-up:
# 165
# Bonus Example
# zip creator

# Hint:
# If it's a simple program
# you can just use a piece of paper where you make a drawing
# how your app front end will look like.
# If it's a more complex program, you can use software
# such as Figma, which we'll cover later on.
# So Figma is a software which allows you to create designs
# for your apps before you build your apps.

# file that depicts the graphical design:
# 175-Bonus-Example-design-screenshot.png

##########################

import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")    # Note: not FilesBrowse, it's for multiple files

label2 = sg.Text("Select dest dir:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")    # By default empty. It will hold the message 'Extraction completed.

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                            [extract_button, output_label]])

while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()