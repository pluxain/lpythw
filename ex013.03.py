from sys import argv

script, department = argv

print(f"We are going to register a User for the {department} department")

name = input("What is the name of the User? ")
role = input("What is the role of the User? ")

print(f"Thanks ! {name}({role}) is now part of { department}")