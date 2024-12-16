from dis import dis
import random

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2? """ )

door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else: 
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif "sleep" in door:
    print("You find a place good enough, sit down and fall asleep")
    luck = random.randint(1, 20)
    print(f"{luck}")
    if luck < 5:
        print("You are suddenly awaken by a group of Skavens")
        print("But too late and cannot react")
        print("You end up on a spit")
        print("Good job!")
    elif luck < 12:
        print("You wake up with a headache")
        print("Probably some herbs were injected in your tea at the auberge...")
        print("You decide to leave the maze as you puke all your guts!")
        print("Good job!")
    elif luck < 20:
        print("You slept well")
        print("You are now ready to continue your adventure")
    else:
        print("You wake up and feel full of energy")
        print("As you start going back to your buiseness you trip on a stone")
        print("You find a ring hidden under a rock in the mud")
        print("Awesome!! This is a ring of invisibility")
else:
    print("You stumble around and fall on a knife and die.  Good job!")

dis('''
if door == "1":
    print("1")
    bear = input("> ")
    if bear == "1":
        print("bear 1")
    elif bear == "2":
        print("bear 2")
    else:
        print("bear 3")
''')
