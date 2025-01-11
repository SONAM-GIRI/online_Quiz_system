import bcrypt
from mysql.connector import Error
from config.setting import DatabaseConfig

class UserService:
    @staticmethod
    def register_user(username: str, password: str) -> bool:
        """Registers a new user with a hashed password."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Check if the username already exists
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                if cursor.fetchone():
                    print("Username already exists. Please choose another username.")
                    return False

                # Hash the password
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                # Insert new user into the database
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
                connection.commit()
                print("Registration successful!")
                return True
            except Error as e:
                print(f"Error during registration: {e}")
                return False
            finally:
                cursor.close()
                connection.close()
        return False

    @staticmethod
    def login_user(username: str, password: str) -> bool:
        """Logs in a user by verifying their username and password."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Fetch the user by username
                cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
                user = cursor.fetchone()

                if user:
                    # The password from the database
                    stored_password = user[0]

                    # Verify the entered password against the hashed password
                    if bcrypt.checkpw(password.encode('utf-8'), stored_password.encode('utf-8')):
                        print("Login successful!")
                        return True
                    else:
                        print("Invalid password.")
                        return False
                else:
                    print("Username not found.")
                    return False
            except Error as e:
                print(f"Error during login: {e}")
                return False
            finally:
                cursor.close()
                connection.close()
        return False
