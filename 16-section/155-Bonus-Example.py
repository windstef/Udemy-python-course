# 155
# Bonus Example

# file compressor

# 1st build the GUI
# we have a label widget, an input widget, and a button widgets.

import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")    # special button, programmed to select files (multiples on shift button) on the filesystem

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")    # special button, programmed to select folder on the filesystem

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button1],
                                                   [label2, input2, choose_button2],
                                                   [compress_button]])

window.read()
window.close()