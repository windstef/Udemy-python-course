# 165
# Bonus Example

# Add the functionality

# following:

# 155
# Bonus Example
# file compressor

# 1st build the GUI
# we have a label widget, an input widget, and a button widgets.

import FreeSimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")    # special button, programmed to select files (multiples on shift button) on the filesystem

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")    # special button, programmed to select folder on the filesystem

compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")
# output_label = sg.Text("In progress ...", key="output", text_color="red")


window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                                   [label2, input2, choose_button2],
                                                   [compress_button, output_label]])


while True:
    event, values = window.read()
    print(event, values)

# example:
# Compress
# {0: '/home/stefkour/PycharmProjects/app1/pythonProject/17-section/functions.py;/home/stefkour/PycharmProjects/app1/pythonProject/17-section/todos.txt',
    # 'files': '/home/stefkour/PycharmProjects/app1/pythonProject/17-section/functions.py;/home/stefkour/PycharmProjects/app1/pythonProject/17-section/todos.txt',
    # 1: '/home/stefkour/PycharmProjects/app1/pythonProject/my-stuff',
    # 'folder': '/home/stefkour/PycharmProjects/app1/pythonProject/my-stuff'}


    filepaths = values["files"].split(";")     # results to a list of the filepaths
    folder = values["folder"]
    make_archive(filepaths, folder)
    # window["output"].update(value="Compression completed!", text_color="green")
    window["output"].update(value="Compression completed!")

window.close()