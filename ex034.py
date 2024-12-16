from dis import dis

i = 0
numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom is is {i}")

print("The numbers: ")
for n in numbers:
    print(n)

dis("""
i = 0
while i < 6:
    i = i + 1
""")


def print_while_lt(n):
    print("print_while_lt")
    i = 0
    numbers = []
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")

    return numbers


def print_while_lt_with_step(n, s):
    print("print_while_lt")
    i = 0
    numbers = []
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + s
        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")

    return numbers


def print_for_in_range_strange(n):
    print("print_for_in_range_strange")
    numbers = []
    for i in range(0, n):
        print(f"At the top i is {i}")
        numbers.append(i)

        # Note: this is really interesting ! it still works but is very strange!
        # the incrementor is not needed, but it does not affect the loop
        # i will still be reaffected correctly on the next iteration
        i = i + 1
        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")

    return numbers


def print_for_in_range(n):
    print("print_for_in_range")
    numbers = []
    for i in range(0, n):
        print(f"At the top i is {i}")
        numbers.append(i)

        print("Numbers now: ", numbers)
        print(f"At the bottom is is {i}")

    return numbers


numbers = print_while_lt(10)
print("The numbers from while function: ")
for n in numbers:
    print(n)

numbers = print_while_lt_with_step(20, 5)
print("The numbers from while function with step: ")
for n in numbers:
    print(n)


numbers = print_for_in_range_strange(10)
print("The numbers from for and range strange function: ")
for n in numbers:
    print(n)

numbers = print_for_in_range(10)
print("The numbers from for and range function: ")
for n in numbers:
    print(n)
