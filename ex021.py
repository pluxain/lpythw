def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def substact(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some maths with just functions!")
age = add(30, 5)
height = substact(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")
what = add(age, substact(height, multiply(weight, divide(iq, 3))))

print("That becomes: ", what, "Can you do it by hand")

print("A simple formula.")
print("34 - (23 + (4 / (2 * 1)))", 34 - (23 + (4 / (2 * 1))))
which = substact(34, add(23, divide(4, multiply(2, 1))))
print("Using the functions", which)
