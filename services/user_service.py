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

                # Check if username already exists
                cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
                if cursor.fetchone():
                    print("Username already exists. Please choose another username.")
                    return False

                # Hash the password
                hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

                # Insert new user
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password))
                connection.commit()
                print("Registration successful!")
                return True
            except Error as e:
                print(f"Error during registration: {e}")
            finally:
                cursor.close()
                connection.close()
        return False

    @staticmethod
    def login_user(username: str, password: str) -> bool:
        """Logs in a user by verifying the username and password."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Fetch user by username
                cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
                user = cursor.fetchone()
                if user:
                    hashed_password = user[0]

                    # Verify password
                    if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                        print("Login successful!")
                        return True
                    else:
                        print("Invalid password.")
                else:
                    print("User not found.")
            except Error as e:
                print(f"Error during login: {e}")
            finally:
                cursor.close()
                connection.close()
        return False
