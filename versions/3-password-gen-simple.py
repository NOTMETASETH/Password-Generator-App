import PySimpleGUI as sg
import string
import random
from csv import writer

sg.theme('DarkGrey6')

layout = [
    [sg.Text("Platform:", font=("Arial", 12), text_color="lime")],
    [sg.Input(key='-PLATFORM-', font=("Arial", 12), background_color="black", text_color="lime")],
    [sg.Text("Password Length:", font=("Arial", 12), text_color="lime")],
    [sg.Input(key='-LENGTH-', font=("Arial", 12), background_color="black", text_color="lime", default_text="8")],
    [sg.Button("Generate Password", key='-GENERATE-', font=("Arial", 12), button_color=("lime", "black"), border_width=2, pad=(20, 10))],
    [sg.Button("Clear", key='-CLEAR-', font=("Arial", 12), button_color=("lime", "black"), border_width=2, pad=(20, 10))],
    [sg.Text("Generated Password:", font=("Arial", 12), text_color="lime")],
    [sg.Input(key='-OUTPUT-', font=("Arial", 12), background_color="black", text_color="lime", readonly=True)],
]

window = sg.Window("Password Generator", layout, element_justification='c')

def generate_password(platform, pass_length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    try:
        pass_length = int(pass_length)
    except ValueError:
        window['-OUTPUT-'].update("Invalid password length.")
        return
    
    s = []
    s.extend(list(lower_case))
    s.extend(list(upper_case))
    s.extend(list(digits))
    s.extend(list(symbols))
    random.shuffle(s)
    password = ("".join(s[0:pass_length]))
    
    window['-OUTPUT-'].update(password)
    pass_data = [platform, password]
    with open('pass.csv', 'a') as f:
        writedata = writer(f)
        writedata.writerow(pass_data)

def clear_output():
    window['-PLATFORM-'].update("")
    window['-LENGTH-'].update("8")
    window['-OUTPUT-'].update("")

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == '-GENERATE-':
        platform = values['-PLATFORM-']
        pass_length = values['-LENGTH-']
        generate_password(platform, pass_length)
    elif event == '-CLEAR-':
        clear_output()

window.close()
