from dis import dis

people = 10
cars = 10
trucks = 25

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if people == cars and trucks > cars:
    print("Trying something more difficult.")
elif cars == trucks or people > 40:
    print("This should NOT be printed as the first `it` passed (this is bad code)")

dis('''
if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
''')