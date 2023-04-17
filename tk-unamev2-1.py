import csv
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random


def check_duplicates(username, csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if username == row[0]:
                return True
    return False


def generate_username(first_name, last_name, csv_file):
    attempts = 0
    while attempts < 10:
        # Keep up to 7 letters of last name and first letters of first name to create username
        username = last_name[:7].lower() + first_name[:min(len(first_name), 8 - len(last_name))].lower()

        # If username is too short, pad with zeros
        if len(username) < 8:
            username += '0' * (8 - len(username))

        # If username already exists, modify it
        while check_duplicates(username, csv_file):
            if len(last_name) > 1:
                last_name = last_name[:-1]  # Remove last letter of last name
                username = last_name[:7].lower() + first_name[:min(len(first_name), 8 - len(last_name))].lower()
            else:
                first_name = first_name[1:]  # Remove first letter of first name
                username = last_name[:7].lower() + first_name[:min(len(first_name), 8 - len(last_name))].lower()

            # If username is too short, pad with zeros
            if len(username) < 8:
                username += '0' * (8 - len(username))

        if len(username) == 8:
            return username

        attempts += 1

    raise ValueError("Could not generate a unique username after 10 attempts")


def on_submit():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()

    try:
        suggested_username = generate_username(first_name, last_name, "usernames.csv")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
        return

    message = f"Suggested username: {suggested_username}. Do you want to edit the username before saving?"
    action = messagebox.askquestion("Preview Username", message)

    if action == 'yes':
        new_username = simpledialog.askstring(
            "Edit Username", f"Edit username {suggested_username}:")
        if not new_username:
            return
        if not (set(new_username) <= set(first_name + last_name)):
            messagebox.showerror(
                "Invalid Username", "Username can only contain letters from first and last name.")
            return
        if check_duplicates(new_username, "usernames.csv"):
            messagebox.showerror("Duplicate Username",
                                 f"Username {new_username} is already taken.")
            return
        suggested_username = new_username

    with open("usernames.csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([suggested_username, first_name, last_name])
        messagebox.showinfo("Suggested Username",
                            f"Suggested username: {suggested_username}")
        window.destroy()


window = tk.Tk()
window.title("Suggest Username")
window.geometry("400x200")
window.resizable(False, False)

first_name_label = tk.Label(window, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(window)
first_name_entry.pack()

last_name_label = tk.Label(window, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(window)
last_name_entry.pack()

submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

window.mainloop()






def on_submit():
    first_name = first_name_entry.get().strip()
    last_name = last_name_entry.get().strip()

    csv_file = "usernames.csv"

    suggested_username = generate_username(first_name, last_name, csv_file)

    while True:
        message = f"Suggested username: {suggested_username}. Do you want to edit the username before saving?"
        action = messagebox.askquestion("Preview Username", message)

        if action == 'yes':
            new_username = simpledialog.askstring(
                "Edit Username", f"Edit username {suggested_username}:")
            if not new_username:
                break
            if not re.match(r'^[a-zA-Z0-9]+$', new_username):
                messagebox.showerror(
                    "Invalid Username", f"{new_username} is not a valid username.")
                continue
            if check_duplicates(new_username, csv_file):
                messagebox.showerror("Duplicate Username",
                                     f"Username {new_username} is already taken.")
                continue
            suggested_username = new_username
        elif action == 'no':
            break
        else:
            messagebox.showerror(
                "Invalid Action", "Invalid action. Please try again.")
            continue

    with open(csv_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([suggested_username, first_name, last_name])
        messagebox.showinfo("Suggested Username",
                            f"Suggested username: {suggested_username}")
        window.destroy()


window = tk.Tk()
window.title("Suggest Username")
window.geometry("400x200")
window.resizable(False, False)

first_name_label = tk.Label(window, text="First Name:")
first_name_label.pack()
first_name_entry = tk.Entry(window)
first_name_entry.pack()

last_name_label = tk.Label(window, text="Last Name:")
last_name_label.pack()
last_name_entry = tk.Entry(window)
last_name_entry.pack()

submit_button = tk.Button(window, text="Submit", command=on_submit)
submit_button.pack()

window.mainloop()
