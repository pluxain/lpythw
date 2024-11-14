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

print('''
GAME OF CODE

Taking the 5 Rules we have the following Game of Code:

1. You read data as input to your program (Rule #5).
2. You store this data in storage (variables) (Rule #4).
3. You use these variables to perform tests... (Rule #3).
4. ...so you can JUMP around... (Rule #2)
5. ...the sequence of instructions... (Rule #1)
6. ...transforming the data to new variables (Rule #4)...
7. ...which you then write to output for storage or display. (Rule #5).
''')

print("A list of Python Byte Code can be found at https://docs.python.org/3/library/dis.html#python-bytecode-instructions")
