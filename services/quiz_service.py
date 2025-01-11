import random
from mysql.connector import Error
from config.setting import DatabaseConfig

class QuizService:
    @staticmethod
    def get_categories():
        """Fetch available quiz categories."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT category_id, category_name FROM categories")
                return cursor.fetchall()
            except Error as e:
                print(f"Error fetching categories: {e}")
                return []
            finally:
                cursor.close()
                connection.close()

    @staticmethod
    def start_quiz(username: str, category_id: int):
        """Starts the quiz for the selected category."""
        connection = DatabaseConfig.get_connection()
        if connection:
            try:
                cursor = connection.cursor()

                # Fetch questions for the selected category
                cursor.execute(
                    "SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_option "
                    "FROM questions WHERE category_id = %s", (category_id,)
                )
                questions = cursor.fetchall()

                if not questions:
                    print("No questions available in this category.")
                    return

                print("\nStarting the quiz...")
                score = 0

                for question in questions:
                    question_id, question_text, option_a, option_b, option_c, option_d, correct_option = question

                    print(f"\n{question_text}")
                    print(f"a) {option_a}")
                    print(f"b) {option_b}")
                    print(f"c) {option_c}")
                    print(f"d) {option_d}")

                    user_answer = input("Enter your answer (a, b, c, or d): ").strip().lower()
                    if user_answer == correct_option.lower():
                        print("Correct!")
                        score += 1
                    else:
                        print(f"Wrong! The correct answer was: {correct_option}")

                print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

                # Update the user's score
                cursor.execute("UPDATE users SET score = %s WHERE username = %s", (score, username))
                connection.commit()
                print("Your score has been saved!")
            except Error as e:
                print(f"Error during the quiz: {e}")
            finally:
                cursor.close()
                connection.close()
