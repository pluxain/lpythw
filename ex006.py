# affect a variable for further use
types_of_people = 10

# create a variable which contains an f-string
x = f"There are {types_of_people} types of people."

# more variables
binary = "binary"
do_not = "don't"
# more f-string variable
y = f"Those who know {binary} and those who {do_not}."

# print variables
print(x)
print(y)
print(w) # works !!

# print f-string with f-string variables in it
print(f"I said: {x}")
# print("I said: {x}") # not working as expected, broken
print(f"I also said: '{y}'")
# print(f"I also said: '{y)'") # broken

# boolean variable
hilarious = False
# prepare a string to be formatted
joke_evaluation = "Isn't that joke so funny?! {}"
#joke_evaluation = "Isn't that joke so funny?! {s}" # broken

# use the format approach of a string
print(joke_evaluation.format(hilarious))

# prepare variables to be concatenated
w = "This is the left side of..."
e = "a string with a right side"

# print string concatenated
print(w + e)