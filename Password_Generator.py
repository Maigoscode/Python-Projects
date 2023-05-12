# Password Generator:
# Create a tool that generates random passwords of a specified length.

import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password


print(generate_password(20))
