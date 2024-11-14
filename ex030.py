from dis import dis

people = 30
cats = 20
dogs = 25

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

dis('''
if people < cats:
    print("Too many cats! The world is doomed!")
''')

dis('''
if people >= dogs:
    print("People are greater than or equal to dogs.")
''')

if not people == cats and cats == dogs:
    print("I will not be printed")

if not True or True:
    print("I will be printed")
