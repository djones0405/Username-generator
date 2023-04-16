import csv
import re

def is_valid_username(username):
    # A valid username must start with a letter, be between 3 and 16 characters long,
    # and can only contain letters, numbers, and underscores.
    regex = r'^[a-zA-Z][a-zA-Z0-9_]{2,15}$'
    return re.match(regex, username) is not None

def generate_username(first_name, last_name):
    username = last_name[:7].lower() + first_name[0].lower()
    return username

def check_duplicates(username, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if username == row[0]:
                return True
    return False

def suggest_username(csv_file):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    suggested_username = generate_username(first_name, last_name)

    while check_duplicates(suggested_username, csv_file):
        print(f"Username {suggested_username} is already taken.")
        action = input("Enter 'c' to choose a new username or 'e' to edit the existing one: ")
        if action == 'c':
            new_username = input("Enter a new username: ")
            if not is_valid_username(new_username):
                print(f"{new_username} is not a valid username.")
                continue
            suggested_username = new_username
        elif action == 'e':
            new_username = input("Enter a new username: ")
            if not is_valid_username(new_username):
                print(f"{new_username} is not a valid username.")
                continue
            if check_duplicates(new_username, csv_file):
                print(f"Username {new_username} is already taken.")
                continue
            suggested_username = new_username
        else:
            print("Invalid action. Please try again.")
            continue

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([suggested_username, first_name, last_name])
        print(f"Suggested username: {suggested_username}")

# example usage
suggest_username("usernames.csv")
