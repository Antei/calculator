import PySimpleGUI as sg

def create_window(theme):
    sg.theme(theme)
    sg.set_options(font='Franklin 18', button_element_size=(6,3))
    button_params = {'size': (6, 3)}
    layout = [
        [sg.Text(
            '0', 
            font='Franklin 42', 
            justification='right', 
            expand_x=True, 
            pad=(10, 20),
            right_click_menu=theme_menu,
            key='-TEXT-')],
        [sg.Button('Сброс', key='-CLEAR-', expand_x=True), sg.Button('=', key='-ENTER-', expand_x=True)],
        [sg.Button(7, **button_params), sg.Button(8, **button_params), sg.Button(9, **button_params), sg.Button('*', **button_params)],
        [sg.Button(4, **button_params), sg.Button(5, **button_params), sg.Button(6, **button_params), sg.Button('/', **button_params)],
        [sg.Button(1, **button_params), sg.Button(2, **button_params), sg.Button(3, **button_params), sg.Button('-', **button_params)],
        [sg.Button(0, expand_x=True), sg.Button('.', **button_params), sg.Button('+', **button_params)]
        ]

    return sg.Window('Simple Calculator', layout, alpha_channel=1)

theme_menu = ['menu', ['Random', 'Black', 'BlueMono', 'BrownBlue', 'Dark', 'DarkAmber', 
                       'DarkBrown', 'DarkGreen', 'DarkGrey9', 'DarkPurple', 'Default', 'GrayGrayGray', 
                       'Green', 'GreenMono', 'GreenTan', 'LightGray1', 'LightGreen', 'LightGrey']]
window = create_window('DarkGrey9')

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
        window['-TEXT-'].update(num_string)

    if event in operations:
        full_operation.append(''.join(current_number))
        current_number = ''
        full_operation.append(event)
        window['-TEXT-'].update(' '.join(full_operation))

    if event == '-ENTER-':
        if len(current_number) > 0:
            full_operation.append(''.join(current_number))
        if len(full_operation) >= 3:
            print(full_operation)
            result = eval(' '.join(full_operation))
            window['-TEXT-'].update(result)
            full_operation, current_number = [str(result)], ''
            print(full_operation)

    if event == '-CLEAR-':
        full_operation, current_number = [], ''
        window['-TEXT-'].update('0')

window.close()