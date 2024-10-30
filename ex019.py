def cheese_and_cracker(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 1
amount_of_crackers = 5
# will print 1 cheeses! and 5 boxes or crackers!
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10  20, 5 + 6)

print("And we can combine the two, variables and math:")
# will print `You have 11 cheeses!`
cheese_and_crackers(amount_of_cheese + 10, amount_of_crackers + 1000)
