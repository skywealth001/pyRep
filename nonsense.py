Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> Option = input("Enter 1 to states Newtons First law of motion, 2 to print out your biodata, 3 to Login to your portal: ")
... def Option1():
...     print("Newton's first law of motion states that if a body remain at rest will remain at rest, and object in motion will continue to move with a constant velocity, unless acted upon by an external force")
... 
... 
... def Option2():
...  print("****************Fill up your Biodata***********")
... Names = input("Enter your names: ")
... Nationality = input("Enter your nationality: ")
... State = input("Enter your state: ")
... Phone_number = input("Enter your phone number: ")
... Address = input("Enter your address: ")
... print("Enter your names: ", Names, "\nNationality: ", Nationality, "\nState: ", State, "\nPhone number: ", Phone_number, "\nAddress: ", Address)
... 
... 
... def Option3():
...     Username = "OLA_MI"
...     Password = "ola419"
...     print("******LOGIN******")
...     Username = input("Enter your username: ")
...     Password = input("Enter your password: ")
...     if Username == "OLA_MI" and Password == "ola419":
...             print("Login Successful")
...         else:
...             print("Login Failed")
