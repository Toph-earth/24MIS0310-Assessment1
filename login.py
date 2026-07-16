credentials = {
    "username" : "admin",
    "pw": "12@3",
}
def login(username, password):
    if credentials["username"] == username and credentials["pw"] == password:
        print(f"User {username} logged in successfully")

def logout(username):
    print(f"User {username} has logged out successfully!")

print(f"\nWelcome to Hospital Appointment Booking System\n")
user = input("Enter username: ")
password = input("Enter password: ")

login(user, password)