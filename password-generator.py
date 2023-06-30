import string
import random

def password_generator():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    # pass_length = int(input("Enter the length of password: \n"))
    s = []
    s.extend(list(lower_case))
    s.extend(list(upper_case))
    s.extend(list(digits))
    s.extend(list(symbols))
    print(s)

password_generator()