import PySimpleGUI as sg

layout = [[]]

window = sg.Window('Simple Calculator', layout)

while True:
    event, values = window.read(100)
    if event == sg.WIN_CLOSED:
        break

window.close()