import csv

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
    username = generate_username(first_name, last_name)
    if check_duplicates(username, csv_file):
        print("Username already taken. Please try again.")
    else:
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, first_name, last_name])
            print("Suggested username: " + username)

# example usage
suggest_username("usernames.csv")
