import json

# Load the birthday dictionary from the JSON file
with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

while True:
    # Ask the user to enter a name
    name = input("Enter a name (or 'q' to quit): ")

    # Check if the user wants to quit
    if name == 'q':
        break

    # Check if the name is in the dictionary
    if name in birthdays:
        print(f"{name}'s birthday is {birthdays[name]}")
    else:
        print(f"Sorry, we don't have {name}'s birthday in our database.")
        # Ask the user to enter the birthday and add it to the dictionary
        birthday = input(f"What is {name}'s birthday (MM/DD/YYYY)? ")
        birthdays[name] = birthday
        print(f"{name}'s birthday has been added to the database.")

        # Update the JSON file with the new dictionary
        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)
