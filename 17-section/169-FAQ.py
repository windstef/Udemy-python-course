# 169
# Q1: How can we have more structured layouts using PySimpleGUI?

# A: For more structured layouts, you can use sg.Column to create column instances. Here is an example:

# That will produce the following output. Left 1 and Left 2 are part of the left
#
# column, while Right 1 and Right 2 are part of the right column.

import PySimpleGUI as sg
# import FreeSimpleGUI as sg

# Prepare the widgets for the left column
left_column_content = [[sg.Text('Left 1')],
                       [sg.Text('Left 2')]]

# Prepare the widgets for the right column
right_column_content = [[sg.Text('Right 1')],
                        [sg.Text('Right 2')]]

# Construct the Column widgets
left_column = sg.Column(left_column_content)
right_column = sg.Column(right_column_content)

# Construct the layout
layout = [[left_column, right_column]]

# Construct and display the window
window = sg.Window('Columns', layout)
window.read()
window.close()