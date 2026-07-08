
usernames = ["Jaden", "Admin", "Jake", "Josiah", "Jacuzzi"]

if not usernames:
    print("We need to find some users!")
    
else:
    
    for username in usernames:
     if username == "Admin":
        print("Greetings Admin! Would you like to see reports?")
     else:
        
        print(f"Hello {username}! Welcome Back!")
