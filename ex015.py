# import argv from sys package
from sys import argv

# unpack argv into variables the first one is the name of the executed script
script, filename = argv

# open the file according to the argument passed
txt = open(filename)

# print the filename and content
print(f"Here's your file {filename}")
print(txt.read())
txt.close()

# ask fo another filename
print("Type the filename again:")
file_again = input("> ")

# open and read the other filename
txt_again = open(file_again)
print(txt_again.read())
txt_again.close()