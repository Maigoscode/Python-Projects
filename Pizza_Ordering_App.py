# pizza ordering app using Python and the Tkinter library.
# This app allows the user to select their pizza toppings and size,
# and then displays the total price of the order.

import tkinter as tk

# Dictionary of available pizza toppings and their prices
toppings = {
    "Pepperoni": 1.50,
    "Mushrooms": 1.00,
    "Onions": 0.75,
    "Sausage": 1.25,
    "Bacon": 1.50,
    "Extra cheese": 1.00
}

# Dictionary of available pizza sizes and their prices
sizes = {
    "Small": 5.00,
    "Medium": 7.00,
    "Large": 9.00
}

# Function to calculate the total price of the pizza order
def calculate_price():
    # Calculate the price of the selected toppings
    topping_prices = [toppings[topping.get()] for topping in topping_vars if topping.get()]
    topping_price = sum(topping_prices)

    # Calculate the price of the selected size
    size_price = sizes[size.get()]

    # Calculate the total price of the pizza order
    total_price = topping_price + size_price

    # Display the total price of the pizza order
    total_price_label.config(text="Total Price: ${:.2f}".format(total_price))

# Create a window
window = tk.Tk()
window.title("Pizza App")

# Create pizza toppings checkboxes
topping_vars = [tk.BooleanVar() for _ in toppings]
topping_checkboxes = [tk.Checkbutton(window, text=topping, variable=topping_var) for topping, topping_var in zip(toppings, topping_vars)]
for checkbox in topping_checkboxes:
    checkbox.pack()

# Create pizza size radio buttons
size = tk.StringVar()
size.set("Small")
size_radios = [tk.Radiobutton(window, text=size_name, variable=size, value=size_name) for size_name in sizes]
for radio in size_radios:
    radio.pack()

# Create a calculate button
calculate_button = tk.Button(window, text="Calculate Price", command=calculate_price)
calculate_button.pack()

# Create a label to display the total price of the pizza order
total_price_label = tk.Label(window, text="Total Price: $0.00")
total_price_label.pack()

# Run the window
window.mainloop()
