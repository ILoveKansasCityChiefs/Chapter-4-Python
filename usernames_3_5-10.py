current_usernames = ["Jaden", "Admin", "Jake", "Josiah", "Jacuzzi"]

new_usernames = ["Ayden", "jaden", "Jake", "Michael", "Jaykob"]

for username in new_usernames:
    if username in current_usernames:
        print("Username Taken. Try Again.")
    else:
        print("Username Available")
