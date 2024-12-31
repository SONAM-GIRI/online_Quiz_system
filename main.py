from services.user_service import UserService

def main():
    print("Welcome to the Online Quiz System!")

    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':  # Registration
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            success = UserService.register_user(username, password)
            if success:
                print("You can now log in.")
        elif choice == '2':  # Login
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            success = UserService.login_user(username, password)
            if success:
                print(f"Welcome {username}! Let's start the quiz.\n")
                # Start the quiz functionality can go here
                # QuizService.start_quiz(username)
        elif choice == '3':  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
