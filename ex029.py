print("Boolean practice")

practices = [
    ("True and True", True, True and True),
    ("False and True", False, False and True),
    ("1 == 1 and 2 == 1", False, 1 == 1 and 2 == 1),
    ('"test" == "test"', True, "test" == "test"),
    ("1 == 1 or 2 != 1", True, 1 == 1 or 2 != 1),
    ("True and 1 == 1", True, True and 1 == 1),
    ("False and 0 != 0", False, False and 0 != 0),
    ("True or 1 == 1", True, True or 1 == 1),
    ('"test" == "testing"', False, "test" == "testing"),
    ("1 != 0 and 2 == 1", False, 1 != 0 and 2 == 1),
    ('"test" != "testing"', True, "test" != "testing"),
    ('"test" == 1', False, "test" == 1),
    ("not (True and False)", True, not (True and False)),
    ("not (1 == 1 and 0 != 1)", False, not (1 == 1 and 0 != 1)),
    ("not (10 == 1 or 1000 == 1000)", False, not (10 == 1 or 1000 == 1000)),
    ("not (1 != 10 or 3 == 4)", False, not (1 != 10 or 3 == 4)),
    ('not ("testing" == "testing" and "Zed" == "Cool Guy")', True, not (
        "testing" == "testing" and "Zed" == "Cool Guy")),
    ('1 == 1 and (not ("testing" == 1 or 1 == 0))',
     True, 1 == 1 and not (("testing" == 1 or 1 == 0))),
    ('"chunky" == "bacon" and (not (3 == 4 or 3 == 3))',
     False, "chunky" == "bacon" and (not (3 == 4 or 3 == 3))),
    ('3 != 3 and (not ("testing" == "testing" or "Python" == "Fun"))',
     False, 3 != 3 and (not ("testing" == "testing" or "Python" == "Fun")))
]

for index, practice in enumerate(practices, start=1):
    problem, answer, check = practice
    print(
        f"{index}. {problem} is {answer}",
        check,
        f"this is {'' if (answer == check) else 'NOT '}correct"
    )
