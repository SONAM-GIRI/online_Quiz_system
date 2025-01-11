from services.user_service import UserService
from services.quiz_service import QuizService

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
                print(f"Welcome {username}!")

                # Display categories
                categories = QuizService.get_categories()
                if categories:
                    print("\nSelect a category:")
                    for category in categories:
                        print(f"{category[0]}. {category[1]}")

                    try:
                        category_id = int(input("Enter the category ID: "))
                        category_names = [cat[0] for cat in categories]
                        if category_id in category_names:
                            QuizService.start_quiz(username, category_id)
                        else:
                            print("Invalid category. Try again.")
                    except ValueError:
                        print("Invalid input. Enter a number.")
                else:
                    print("No categories available.")
        elif choice == '3':  # Exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
