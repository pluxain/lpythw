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
