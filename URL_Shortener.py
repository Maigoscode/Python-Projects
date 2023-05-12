# URL Shortener:
# Build a simple URL shortener that generates a shortened URL for a given long URL.

import string
import random


def generate_short_url(length):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(characters) for i in range(length))
    return short_url


long_url = "https://www.w3schools.com/python/python_datatypes.asp"
short_url = "https://short.com/" + generate_short_url(2)
print("Short URL: " + short_url)
