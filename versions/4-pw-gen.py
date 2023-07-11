import os
import PySimpleGUI as sg
import string
import random
import csv

sg.theme('DarkGrey6')

stored_csv_path = "/Users/m1/Developer/Projects/Password-Generator-App/stored_pw/stored.csv"

def generate_layout():
    return [
        [sg.Text("Platform:", font=("Arial", 12), text_color="lime")],
        [sg.Input(key='-PLATFORM-', font=("Arial", 12), background_color="black", text_color="lime")],
        [sg.Text("Password Length:", font=("Arial", 12), text_color="lime")],
        [sg.Input(key='-LENGTH-', font=("Arial", 12), background_color="black", text_color="lime", default_text="8")],
        [sg.Button("Generate Password", key='-GENERATE-', font=("Arial", 12), button_color=("lime", "black"), border_width=2, pad=(20, 10))],
        [sg.Button("Clear", key='-CLEAR-', font=("Arial", 12), button_color=("lime", "black"), border_width=2, pad=(20, 10))],
        [sg.Text("Generated Password:", font=("Arial", 12), text_color="lime")],
        [sg.Input(key='-OUTPUT-', font=("Arial", 12), background_color="black", text_color="lime", readonly=True)],
        [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-', visible=False)],
    ]

def generate_password(window, platform, pass_length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    if not platform:
        window['-OUTPUT-'].update("Please enter a platform.")
        return
    
    try:
        pass_length = int(pass_length)
        if pass_length < 4:
            window['-OUTPUT-'].update("Password length should be at least 4.")
            return
    except ValueError:
        window['-OUTPUT-'].update("Invalid password length.")
        return
    
    s = []
    s.extend(random.sample(lower_case, 1))
    s.extend(random.sample(upper_case, 1))
    s.extend(random.sample(digits, 1))
    s.extend(random.sample(symbols, 1))
    s.extend(random.sample(lower_case + upper_case + digits + symbols, pass_length - 4))
    random.shuffle(s)
    password = "".join(s)
    
    window['-OUTPUT-'].update(password)
    
    pass_data = [platform, password]
    with open(stored_csv_path, "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(pass_data)

def clear_output(window):
    window['-PLATFORM-'].update("")
    window['-LENGTH-'].update("8")
    window['-OUTPUT-'].update("")
    window['-PROGRESS-'].update(visible=False)

def main():
    window = sg.Window("Password Generator", generate_layout(), element_justification='c')

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == '-GENERATE-':
            window['-PROGRESS-'].update(current_count=0, visible=True)
            for i in range(100):
                window['-PROGRESS-'].update_bar(i+1)
                sg.time.sleep(0.01)
            platform = values['-PLATFORM-']
            pass_length = values['-LENGTH-']
            generate_password(window, platform, pass_length)
        elif event == '-CLEAR-':
            clear_output(window)

    window.close()

main()
