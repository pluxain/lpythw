def print_number(x):
    print("NUMBER IS", x)


rename_print = print_number
print_number(100)
rename_print(100)


def add(a, b):
    print(f"{a} + {b} is {a + b}")


addition = add
add(3, 5)
addition(3, 5)
