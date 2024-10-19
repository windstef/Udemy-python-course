
# 179
# FAQ

# Q1: Sometimes, the widgets are not so well aligned. For example, the GUI below doesn't look so good. How can we better align widgets?

# A: The widgets above do not align well because the two labels on the left have different lengths. That can be avoided by using columns. Here is a code sample:


import FreeSimpleGUI as sg

# from zip_extractor import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select destination directory:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

col1 = sg.Column([[label1], [label2]])
col2 = sg.Column([[input1], [input2]])
col3 = sg.Column([[choose_button1], [choose_button2]])

window = sg.Window("Archive Extractor",
                   layout=[[col1, col2, col3], [extract_button]])
while True:
    event, values = window.read()
    print(event, values)
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="Extraction Completed!")

window.close()


###########################3

# Solution:
# https://www.udemy.com/course/the-python-mega-course/learn/lecture/32759810#learning-tools

# As you can see, the widgets are well aligned now. All we did to achieve that was put the widgets inside Column widgets using these lines:
#
# col1 = sg.Column([[label1], [label2]])
# col2 = sg.Column([[input1], [input2]])
# col3 = sg.Column([[choose_button1], [choose_button2]])
# Then, we use supplied those column widgets to layout:
#
# layout=[[col1, col2, col3], [extract_button]]
