fruit = [
    ['Apples', 12, 'AAA'], ['Oranges', 1, 'B'],
    ['Pears', 2, 'A'], ['Grapes', 14, 'UR']
]

cars = [
    ['Cadillac', ['Black', 'Big', 34500]],
    ['Corvette', ['Red', 'Little', 1000000]],
    ['Ford', ['Blue', 'Medium', 1234]],
    ['BMW', ['White', 'Baby', 7890]]
]

languages = [
    ['Python', ['Slow', ['Terrible', 'Mush']]],
    ['Javascript', ['Moderate', ['Alright', 'Bizarre']]],
    ['Perl6', ['Moderate', ['Fun', 'Weird']]],
    ['C', ['Fast', ['Annoying', 'Dangerous']]],
    ['Forth', ['Fast', ['Fun', 'Difficult']]]
]

solutions = [
    [
        "fruit", [
            [12, 'fruit[0][1]', fruit[0][1]],
            ["'AAA'", 'fruit[0][2]', fruit[0][2]],
            [2, 'fruit[2][1]', fruit[2][1]],
            ["'Oranges'", 'fruit[1][0]', fruit[1][0]],
            ["'Grapes'", 'fruit[3][0]', fruit[3][0]],
        ]
    ],
    [

        "cars", [
            ["'Big'", 'cars[0][1][1]', cars[0][1][1]],
            ["'Red'", 'cars[1][0][0]', cars[1][1][0]],
            [1234, 'cars[2][1][2]', cars[2][1][2]],
            ["'White'", 'cars[3][1][0]', cars[3][1][0]],
            [7890, 'cars[3][1][2]', cars[3][1][2]],
            ["'Black'", 'cars[0][1][0]', cars[0][1][0]],
            [34500, 'cars[0][1][2]', cars[0][1][2]],
            ["'Blue'", 'cars[2][1][0]', cars[2][1][0]]
        ]
    ],
    [
        "languages",
        [
            ["'Slow'", 'languages[0][1][0]', languages[0][1][0]],
            ["'Alright'", 'languages[1][1][1][0]', languages[1][1][1][0]],
            ["'Dangerous'", 'languages[3][1][1][1]', languages[3][1][1][1]],
            ["'Fast'", 'languages[3][1][0]', languages[3][1][0]],
            ["'Fast'", 'languages[4][1][0]', languages[4][1][0]],
            ["'Difficult'", 'languages[4][1][1][1]', languages[4][1][1][1]],
            ["'Fun'", 'languages[2][1][1][0]', languages[2][1][1][0]],
            ["'Fun'", 'languages[4][1][1][0]', languages[4][1][1][0]],
            ["'Annoying'", 'languages[3][1][1][0]', languages[3][1][1][0]],
            ["'Weird'", 'languages[2][1][1][1]', languages[2][1][1][1]],
            ["'Moderate'", 'languages[1][1][0]', languages[1][1][0]],
            ["'Moderate'", 'languages[2][1][0]', languages[2][1][0]],
        ]
    ],
    [
        "final find the value from the expression",
        [
            ["'Little'", 'cars[1][1][1]', cars[1][1][1]],
            ["'Red'", 'cars[1][1][0]', cars[1][1][0]],
            ["'Corvette'", 'cars[1][0]', cars[1][0]],
            ["'Baby'", 'cars[3][1][1]', cars[3][1][1]],
            ["'UR'", 'fruit[3][2]', fruit[3][2]],
            ["'Mush'", 'languages[0][1][1][1]', languages[0][1][1][1]],
            [2, 'fruit[2][1]', fruit[2][1]],
            ["'Fast'", 'languages[3][1][0]', languages[3][1][0]]
        ]
    ]
]

for solution in solutions:
    print(f"{solution[0]}")

    for riddle in solution[1]:
        print(f"\t{riddle[0]} is at {riddle[1]}", riddle[2])
