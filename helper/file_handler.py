import json

class FileHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self._initialize_file()

    def _initialize_file(self):
        try:
            with open(self.file_path, "r") as file:
                pass
        except FileNotFoundError:
            with open(self.file_path, "w") as file:
                json.dump({}, file)

    def load_users(self):
        with open(self.file_path, "r") as file:
            return json.load(file)

    def save_users(self, users):
        with open(self.file_path, "w") as file:
            json.dump(users, file)
