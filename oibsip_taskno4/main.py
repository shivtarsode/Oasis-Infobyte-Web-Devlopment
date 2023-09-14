import os


user_database = {}


user_data_file = "user_data.txt"


def load_user_data():
    if os.path.exists(user_data_file):
        with open(user_data_file, "r") as file:
            lines = file.readlines()
            for line in lines:
                username, password = line.strip().split(":")
                user_database[username] = password

def save_user_data():
    with open(user_data_file, "w") as file:
        for username, password in user_database.items():
            file.write(f"{username}:{password}\n")


def register():
    while True:
        username = input("Enter a username: ")
        if username in user_database:
            print("Username already exists. Please choose another one.")
        else:
            password = input("Enter a password: ")
            user_database[username] = password
            save_user_data()
            print("Registration successful!")
            break


def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in user_database and user_database[username] == password:
            print("Login successful!")
            break
        else:
            print("Incorrect username or password. Please try again.")


def secured_page():
    print("Welcome to the secured page!")
    

if __name__ == "__main__":
    load_user_data()
    while True:
        print("\nMenu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
            if input("Do you want to access the secured page? (yes/no): ").lower() == "yes":
                secured_page()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

