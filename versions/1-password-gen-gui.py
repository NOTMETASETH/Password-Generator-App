import string
import random
from csv import writer
import tkinter as tk

def generate_password():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    platform = platform_entry.get()
    pass_length = pass_length_entry.get()
    try:
        pass_length = int(pass_length)
    except ValueError:
        pass_output.configure(text="Invalid password length.")
        return
    s = []
    s.extend(list(lower_case))
    s.extend(list(upper_case))
    s.extend(list(digits))
    s.extend(list(symbols))
    random.shuffle(s)
    password = ("".join(s[0:pass_length]))
    pass_output.configure(text=password)
    pass_data = [platform, password]
    with open ('pass.csv','a') as f:
        writedata = writer(f)
        writedata.writerow(pass_data)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create the platform label and entry field
platform_label = tk.Label(window, text="Platform")
platform_label.grid(row=0, column=0, padx=10, pady=10)
platform_entry = tk.Entry(window)
platform_entry.grid(row=0, column=1, padx=10, pady=10)

# Create the password length label and entry field
pass_length_label = tk.Label(window, text="Password Length")
pass_length_label.grid(row=1, column=0, padx=10, pady=10)
pass_length_entry = tk.Entry(window)
pass_length_entry.grid(row=1, column=1, padx=10, pady=10)

# Create the generate password button
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create the password output label
pass_output_label = tk.Label(window, text="Password")
pass_output_label.grid(row=3, column=0, padx=10, pady=10)
pass_output = tk.Label(window, text="")
pass_output.grid(row=3, column=1, padx=10, pady=10)

# Run the main loop
window.mainloop()