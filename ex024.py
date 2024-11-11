email = {
    "From": "john.doe@example.com",
    "To": "jane.doe@example.org",
    "Subject": "I HAVE AN AMAZING INVESTMENT FOR YOU!!!"
}

print(f"Message from {email["From"]} to {
      email["To"]} about {email["Subject"]}")

messages = [
    {"to": "Sun", "from": "Moon", "message": "Hi!"},
    {"to": "Moon", "from": "Sun", "message": "What to you want Sun!"},
    {"to": "Sun", "from": "Moon", "message": "I'm awake!"},
    {"to": "Moon", "from": "Sun", "message": "I can see that Sun."},
]


for message in messages:

    print(f"Message from {message["from"]} to {
        message["to"]} saying {message["message"]}")

fruit = [
    {
        'kind': 'Apples',
        'count': 12,
        'rating': 'AAA'
    },
    {
        'kind': 'Oranges',
        'count': 1,
        'rating': 'B'
    },
    {
        'kind': 'Pears',
        'count': 2,
        'rating': 'A'
    },
    {
        'kind': 'Grapes',
        'count': 14,
        'rating': 'UR'
    },
]

cars = [
    {
        'type': 'Cadillac',
        'color': 'Black',
        'size': 'Big',
        'miles': 34500
    },
    {
        'type': 'Corvette',
        'color': 'Red',
        'size': 'Little',
        'miles': 1_000_000
    },
    {
        'type': 'Ford',
        'color': 'Blue',
        'size': 'Medium',
        'miles': 1234
    },
    {
        'type': 'BMW',
        'color': 'White',
        'size': 'Baby',
        'miles': 7890
    },
]

languages = [
    {
        'name': 'Python',
        'speed': 'Slow',
        'opinion': ['Terrible', 'Mush']
    },
    {
        'name': 'JavaScript',
        'speed': 'Moderate',
        'opinion': ['Alright', 'Bizarre']
    },
    {
        'name': 'Perl6',
        'speed': 'Moderate',
        'opinion': ['Fun', 'Weird']
    },
    {
        'name': 'C',
        'speed': 'Fast',
        'opinion': ['Annoying', 'Dangerous']
    },

    {
        'name': 'Forth',
        'speed': 'Fast',
        'opinion': ['Fun', 'Difficult']
    },
]

solutions = {
    "fruit": [
        {'result': 12, 'path': "fruit[0]['count']",
            'value': fruit[0]['count']},
        {'result': 'AAA',
            'path': "fruit[0]['rating']", 'value': fruit[0]['rating']},
        {'result': 2, 'path': "fruit[2]['count']", 'value': fruit[2]['count']},
        {'result': 'Oranges',
            'path': "fruit[1]['kind']", 'value': fruit[1]['kind']},
        {'result': 'Grapes',
            'path': "fruit[3]['kind']", 'value': fruit[3]['kind']},
        {'result': 14, 'path': "fruit[3]['count']",
            'value': fruit[3]['count']},
        {'result': 'Apples',
            'path': "fruit[0]['kind']", 'value': fruit[0]['kind']},
    ],
    "cars": [
        {'result': 'Big',
            'path':  "cars[0]['type']", 'value': cars[0]['size']},
        {'result': 'Red',
            'path':  "cars[1]['color']", 'value': cars[1]['color']},
        {'result': 1234,
            'path':  "cars[2]['miles']", 'value': cars[2]['miles']},
        {'result': 'White',
            'path':  "cars[3]['color']", 'value': cars[3]['color']},
        {'result': 7890,
            'path':  "cars[3]['miles']", 'value': cars[3]['miles']},
        {'result': 'Black',
            'path':  "cars[0]['color']", 'value': cars[0]['color']},
        {'result': 34500,
            'path':  "cars[0]['miles']", 'value': cars[0]['miles']},
        {'result': 'Blue',
            'path':  "cars[2]['color']", 'value': cars[2]['color']},
    ],
    "languages": [
        {'result': 'Slow',
            'path':  "languages[0]['speed']", 'value': languages[0]['speed']},
        {'result': 'Alright',
            'path':  "languages[1]['opinion'][0]", 'value': languages[1]['opinion'][0]},
        {'result': 'Dangerous',
            'path':  "languages[3]['opinion'][1]", 'value': languages[3]['opinion'][1]},
        {'result': 'Fast',
            'path':  "languages[3]['speed']", 'value': languages[3]['speed']},
        {'result': 'Fast',
            'path':  "languages[4]['speed']", 'value': languages[4]['speed']},
        {'result': 'Difficult',
            'path':  "languages[4]['opinion'][1]", 'value': languages[4]['opinion'][1]},
        {'result': 'Fun',
            'path':  "languages[2]['opinion'][0]", 'value': languages[2]['opinion'][0]},
        {'result': 'Fun',
            'path':  "languages[4]['opinion'][0]", 'value': languages[4]['opinion'][0]},
        {'result': 'Annoying',
            'path':  "languages[3]['opinion'][0]", 'value': languages[3]['opinion'][0]},
        {'result': 'Weird',
            'path':  "languages[2]['opinion'][1]", 'value': languages[2]['opinion'][1]},
        {'result': 'Moderate',
            'path':  "languages[1]['speed']", 'value': languages[1]['speed']},
        {'result': 'Moderate',
            'path':  "languages[2]['speed']", 'value': languages[2]['speed']},

    ]
}

for section in solutions:
    print(f"{section}")
    for solution in solutions[section]:
        print(f"\t{solution['result']} is accessible using this path {
              solution['path']} -> {solution['value']}")
        print(f"\tIs this correct ? {
              solution['result'] == solution['value']}")
