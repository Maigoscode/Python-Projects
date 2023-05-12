# Text Adventure Game:
# Build a simple text-based adventure game where the user is presented with choices and must navigate through
# a story to reach an ending.
print("Welcome to Adventure Game!")
print("You are lost in a dark forest.")

while True:
    print("What do you want to do?")
    choice = input("A) Keep walking\nB) Rest for a bit\nC) Climb a tree\n")

    if choice == "A":
        print("You keep walking and find a clearing.")
        print("You see a small house in the distance.")
        break
    elif choice == "B":
        print("You rest for a bit, but the darkness is closing in.")
        print("You decide to keep walking.")
    elif choice == "C":
        print("You climb a tree and get a better view of your surroundings.")
        print("You spot a small house in the distance.")
        break
    else:
        print("Invalid choice. Try again.")

print("You approach the house and knock on the door.")
print("An old woman answers and invites you inside.")

while True:
    print("What do you want to do?")
    choice = input("A Ask for")
