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

color = "Red"

corvette = {
    "color": color
}

print("LITTLE", corvette['color'], "CORVETTE")


def run():
    print("VROOM")


corvette = {
    "color": "Red",
    "run": run
}

print("My", corvette["color"], "can go")
corvette["run"]()
