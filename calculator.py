import PySimpleGUI as sg

def create_window(theme, params):
    sg.theme(theme)
    sg.set_options(font='Franklin 18', button_element_size=(6,3))
    layout = [
        [sg.Text(
            '0', 
            font='Franklin 42', 
            justification='right', 
            expand_x=True, 
            pad=(10, 20),
            key='-EVAL-')],
        [sg.Text(
            '0', 
            font='Franklin 42', 
            justification='right', 
            expand_x=True, 
            pad=(10, 20),
            key='-RESULT-')],
        [sg.Button('C', key='-CLEAR-', expand_x=True), sg.Button('=', key='-ENTER-', expand_x=True)],
        [sg.Button(7, **params), sg.Button(8, **params), sg.Button(9, **params), sg.Button('*', **params)],
        [sg.Button(4, **params), sg.Button(5, **params), sg.Button(6, **params), sg.Button('/', **params)],
        [sg.Button(1, **params), sg.Button(2, **params), sg.Button(3, **params), sg.Button('-', **params)],
        [sg.Button(0, expand_x=True), sg.Button('.', **params,), sg.Button('+', **params)]
        ]

    return sg.Window('Simple Calculator', layout, alpha_channel=1, right_click_menu=theme_menu)

button_params = {'size': (6, 3)}
theme_menu = ['menu', ['Random', 'Black', 'BlueMono', 'BrownBlue', 'Dark', 'DarkAmber', 
                       'DarkBrown', 'DarkGreen', 'DarkGrey9', 'DarkPurple', 'Default', 'GrayGrayGray', 
                       'Green', 'GreenMono', 'GreenTan', 'LightGray1', 'LightGreen', 'LightGrey']]
window = create_window('DarkGrey9', button_params)

current_number = ''
decimal_buttons = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
operations = ['+', '-', '/', '*']
full_operation = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = create_window(event)

    if event in decimal_buttons:
        current_number += event
        num_string = ''.join(current_number)
        window['-RESULT-'].update(num_string)

    if event in operations:
        full_operation.append(''.join(current_number))
        current_number = ''
        full_operation.append(event)
        window['-EVAL-'].update(' '.join(full_operation))

    if event == '-ENTER-':
        if len(current_number) > 0:
            full_operation.append(''.join(current_number))
            window['-EVAL-'].update(' '.join(full_operation))
        if len(full_operation) >= 3:
            result = eval(' '.join(full_operation))
            window['-RESULT-'].update(result)
            full_operation, current_number = [str(result)], ''

    if event == '-CLEAR-':
        full_operation, current_number = [], ''
        window['-EVAL-'].update('0')
        window['-RESULT-'].update('0')

window.close()