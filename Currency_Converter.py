# Currency Converter:
# Create a simple currency converter that converts a specified amount of one currency to another using an API.


import requests


def convert_currency(amount, from_currency, to_currency):
    url = "https://api.exchangerate-api.com/v4/latest/" + from_currency
    response = requests.get(url)
    data = response.json()
    conversion_rate = data['rates'][to_currency]
    converted_amount = amount * conversion_rate
    return converted_amount


print(convert_currency(100, "USD", "EUR"))
