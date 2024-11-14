from dis import dis

print('''
x = 10
y = 20
z = x + y
''')
dis('''
x = 10
y = 20
z = x + y
''')

print("while True: x = 10")
dis("while True: x = 10")

print('''
x = 1
if x > 0:
    y = 10
''')
dis('''
x = 1
if x > 0:
    y = 10
''')

print('''
x = -1
if x > 0:
    y = 10
''')
dis('''
x = -1
if x > 0:
    y = 10
''')

x = 10
while x > 0:
    x -= 1
    print(f"x is {x}")

print('''
x = 10
while x > 0:
    x -=1
    print(f"x is {x}")
''')
dis('''
x = 10
while x > 0:
    x -=1
    print(f"x is {x}")
''')

print("input('Yes? ')")
dis("input('Yes? ')")
