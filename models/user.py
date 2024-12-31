class User:
    def __init__(self, user_id, username, score=0):
        self.user_id = user_id
        self.username = username
        self.score = score

    def __str__(self):
        return f"User({self.user_id}, {self.username}, {self.score})"
