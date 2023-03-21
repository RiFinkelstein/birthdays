import json
import datetime

# Load the birthday dictionary from the JSON file
with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

while True:
    # Ask the user to enter a name
    option = input("Enter an option: 's' to search for a birthday, 'a' to add a birthday, 'e' to edit a birthday, 'd' to delete a birthday, 'l' to list all birthdays in database or 'q' to quit: ")

    # Check if the user wants to quit
    if option == 'q':
        break


    # Check if the name is in the dictionary
    elif option == 's':
        #ask the user to enter a name
        name = input("Enter a name: ")

        if name in birthdays:
            print(f"{name}'s birthday is {birthdays[name]}")
        else:
            print(f"Sorry, we don't have {name}'s birthday in our database.")
            # Ask the user to enter the birthday and add it to the dictionary
            birthday = input(f"What is {name}'s birthday (MM/DD/YYYY)? ")
            birthdays[name] = birthday
            print(f"{name}'s birthday has been added to the database.")
    
    elif option == 'a':
        #ask the user to enter a name
        name= input("enter a name: ")
        birthday = input(f"What is {name}'s birthday (MM/DD/YYYY)? ")
        birthdays[name] = birthday
        print(f"{name}'s birthday has been added to the database.")

        # Update the JSON file with the new dictionary
        with open('birthdays.json', 'w') as f:
            json.dump(birthdays, f)
    
    elif option == 'e':
        name= input("enter a name: ")
        if name in birthdays:
            # Ask the user to enter the new birthday and update the dictionary
            birthday = input(f"What is {name}'s new birthday (MM/DD/YYYY)? ")
            birthdays[name] = birthday
            print(f"{name}'s birthday has been updated in the database.")

            # Update the JSON file with the new dictionary
            with open('birthdays.json', 'w') as f:
                json.dump(birthdays, f)
        else:
            print(f"Sorry, we don't have {name}'s birthday in our database.")
    elif option == 'd':
        name = input("Enter a name: ")
        if name in birthdays:
            del birthdays[name]
            print(f"{name}'s birthday has been deleted from the database.")
            # Update the JSON file with the new dictionary
            with open('birthdays.json', 'w') as f:
                json.dump(birthdays, f)
        else:
            print(f"Sorry, we don't have {name}'s birthday in our database.")
    
    elif option == 'l':
        for name in birthdays:
            print(f"{name}'s birthday is {birthdays[name]}")

    # Invalid option
    else:
        print("Invalid option. Please try again.")







