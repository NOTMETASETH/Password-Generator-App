## Improved GUI for the password generator

import string
import random
from csv import writer
import tkinter as tk
from tkinter import ttk

class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x250")
        self.root.resizable(False, False)
        self.root.configure(bg="#222222")
        
        # Password Variables
        self.password_var = tk.StringVar()
        self.platform_var = tk.StringVar()
        self.pass_len_var = tk.StringVar()
        self.pass_len_var.set("8")
        
        # Labels
        tk.Label(self.root, text="Platform:", font=("Helvetica", 12), bg="#222222", fg="#00ff00").place(x=20, y=30)
        tk.Label(self.root, text="Password Length:", font=("Helvetica", 12), bg="#222222", fg="#00ff00").place(x=20, y=80)
        tk.Label(self.root, text="Generated Password:", font=("Helvetica", 12), bg="#222222", fg="#00ff00").place(x=20, y=130)
        
        # Entries
        self.platform_entry = ttk.Entry(self.root, textvariable=self.platform_var, font=("Helvetica", 12), foreground="#00ff00", background="#444444")
        self.platform_entry.place(x=150, y=30, width=200)
        self.pass_len_entry = ttk.Entry(self.root, textvariable=self.pass_len_var, font=("Helvetica", 12), foreground="#00ff00", background="#444444")
        self.pass_len_entry.place(x=200, y=80, width=50)
        
        # Generate Password Button
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password, font=("Helvetica", 12), bg="#00ff00", fg="#222222")
        generate_button.place(x=120, y=190, width=150)
        
        # Clear Button
        clear_button = tk.Button(self.root, text="Clear", command=self.clear, font=("Helvetica", 12), bg="#ff0000", fg="#222222")
        clear_button.place(x=280, y=190, width=70)
        
        # Password Output
        tk.Entry(self.root, textvariable=self.password_var, font=("Helvetica", 12), state="readonly", foreground="#00ff00", background="#444444").place(x=200, y=130, width=150)
        
    def generate_password(self):
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation
        platform = self.platform_var.get()
        pass_length = self.pass_len_var.get()
        try:
            pass_length = int(pass_length)
        except ValueError:
            self.password_var.set("Invalid password length.")
            return
        s = []
        s.extend(list(lower_case))
        s.extend(list(upper_case))
        s.extend(list(digits))
        s.extend(list(symbols))
        random.shuffle(s)
        password = ("".join(s[0:pass_length]))
        self.password_var.set(password)
        pass_data = [platform, password]
        with open ('pass.csv','a') as f:
            writedata = writer(f)
            writedata.writerow(pass_data)
        
    def clear(self):
        self.platform_var.set("")
        self.pass_len_var.set("8")
        self.password_var.set("")
        
if __name__ == "__main__":
    root = tk.Tk()
    PasswordGenerator(root)
    root.mainloop()


# In this code, I've made the following modifications:

## - Changed the background color of the main window to a dark gray (#222222).
## - Changed the foreground and background colors of the entry fields and password output field to a lighter gray (#444444) and neon green (#00ff00) to improve visibility.
## - Changed the "Generate Password" button to a neon green color and the "Clear" button to a neon red color to make them more visually distinct.
## - Changed the font colors of the labels to neon green (#00ff00).

### I hope this color scheme is easier to read.