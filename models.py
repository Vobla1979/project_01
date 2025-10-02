from datetime import datetime

class User:
    def __init__(self, id: int, email: str, login: str, password: str):
        self.id = id
        self.email = email
        self.login = login
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

class Post:
    def __init__(self, id: int, author_id: int, title: str, content: str):
        self.id = id
        self.author_id = author_id
        self.title = title
        self.content = content
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
