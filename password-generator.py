import string
import random
from csv import writer
    
def password_generator():
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    platform = input("Enter the name of the platform: \n")
    pass_length = int(input("Enter the length of the password: \n"))
    s = []
    s.extend(list(lower_case))
    s.extend(list(upper_case))
    s.extend(list(digits))
    s.extend(list(symbols))
    random.shuffle(s)
    password = ("".join(s[0:pass_length]))
    print(password)
    passdata= [platform,password]
    with open ('pass.csv','a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)

password_generator()