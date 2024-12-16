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
