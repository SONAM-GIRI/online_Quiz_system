from config.setting import DatabaseConfig
from models.user import User

class QuizService:
    @staticmethod
    def register_user(username):
        """Registers a user in the database and returns a User object."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("INSERT INTO users (username) VALUES (%s)", (username,))
                connection.commit()
                user_id = cursor.lastrowid
                return User(user_id, username)
            finally:
                cursor.close()
                connection.close()
        return None

    @staticmethod
    def get_questions():
        """Fetches all questions from the database."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor(dictionary=True)
                cursor.execute("SELECT * FROM questions")
                return cursor.fetchall()
            finally:
                cursor.close()
                connection.close()
        return []

    @staticmethod
    def start_quiz(user):
        """Runs the quiz for the given user."""
        questions = QuizService.get_questions()
        if not questions:
            print("No questions available.")
            return

        score = 0
        for question in questions:
            print(f"\nQuestion: {question['question_text']}")
            options = [question['option_a'], question['option_b'], question['option_c'], question['option_d']]
            for i, option in enumerate(options, 1):
                print(f"{i}. {option}")

            answer = input("Your answer (1-4): ")
            try:
                if options[int(answer) - 1] == question['correct_option']:
                    score += 1
            except (ValueError, IndexError):
                print("Invalid input. Moving to the next question.")

        user.score = score
        print(f"\nQuiz finished! Your score: {user.score}")
        QuizService.save_score(user)

    @staticmethod
    def save_score(user):
        """Updates the user's score in the database."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("UPDATE users SET score = %s WHERE user_id = %s", (user.score, user.user_id))
                connection.commit()
            finally:
                cursor.close()
                connection.close()
