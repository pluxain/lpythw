from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv


print("The script is called (packed):", argv[0])
print("Your first variable is (packed):", argv[1])
print("Your second variable is (packed):", argv[2])
print("Your third variable is (packed):", argv[3])

print("The script is called (unpacked):", script)
print("Your first variable is (unpacked):", first)
print("Your second variable is (unpacked):", second)
print("Your third variable is (unpacked):", third)