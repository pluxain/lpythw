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


def create_car(color, name, sound, speed):
    def go():
        print(f"{sound}!!")
        return sound

    return {
        "color": color,
        "name": name,
        "go": go,
        "speed": speed
    }


corvette = create_car("red", "corvette", "BRAAAAAAAM", 120)

print(f"Hey! I am {corvette["name"]}, I am {
      corvette["color"]} and can drive up to {corvette["speed"]}, {corvette["go"]()}!!")

audi = create_car("red", "audi", "BROOOOOOM", 160)

print(f"Hey! I am {audi["name"]}, I am {
      audi["color"]} and can drive up to {audi["speed"]}, {audi["go"]()}!!")

corvette["color"] = "black"

print(f"Hey! I am {corvette["name"]}, I am {
      corvette["color"]} and can drive up to {corvette["speed"]}, {corvette["go"]()}!!")

print(f"Hey! I am {audi["name"]}, I am {
      audi["color"]} and can drive up to {audi["speed"]}, {audi["go"]()}!!")
