credentials = {
    "username" : "admin",
    "pw": "12@3",
}
def login(username, password):
    if credentials["username"] == username and credentials["pw"] == password:
        print(f"User {username} logged in successfully")
    elif credentials["username"] == username and credentials["pw"] != password:
        print("Incorrect password. Retry login")
    elif credentials["username"] != username and credentials["pw"] == password:
        print("Incorrect username. Retry login")
    else:
        print("Incorrect username and password. Retry login")

def logout(username):
    print(f"User {username} has logged out successfully!")

print("\t\tWelcome to Hospital Appointment Booking System\n\t\tPlease login")
user = input("Enter username: ")
pw = input("Enter password: ")

login(user, pw)