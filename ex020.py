from sys import argv

# input_file = "ex020_test.txt"
script, input_file = argv

# print a file content


def print_all(f):
    print(f.read())


# rewind a file
def rewind(f):
    f.seek(0)


# print the next line of the file
def print_a_line(line_count, f):
    print(line_count, f.readline())


current_file = open(input_file)
print("First let's print the whole file:\n")
print_all(current_file)


print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")
current_line = 1
# current_line is 1
print_a_line(current_line, current_file)


current_line += 1
# current_line is 2
print_a_line(current_line, current_file)

current_line += 1
# current_line is 3
print_a_line(current_line, current_file)
