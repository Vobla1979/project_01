from typing import List, Dict, Optional
from models import User, Post

users_db: Dict[int, User] = {}
posts_db: Dict[int, Post] = {}

user_id_seq = 1
post_id_seq = 1

def create_user(email, login, password) -> User:
    global user_id_seq
    user = User(user_id_seq, email, login, password)
    users_db[user_id_seq] = user
    user_id_seq += 1
    return user

def get_user(user_id: int) -> Optional[User]:
    return users_db.get(user_id)

def get_all_users() -> List[User]:
    return list(users_db.values())

def update_user(user_id: int, **kwargs) -> Optional[User]:
    user = users_db.get(user_id)
    if not user:
        return None
    for field, value in kwargs.items():
        if value:
            setattr(user, field, value)
    user.updated_at = user.updated_at.now()
    return user

def delete_user(user_id: int) -> bool:
    return users_db.pop(user_id, None) is not None

def create_post(author_id, title, content) -> Post:
    global post_id_seq
    post = Post(post_id_seq, author_id, title, content)
    posts_db[post_id_seq] = post
    post_id_seq += 1
    return post

def get_post(post_id: int) -> Optional[Post]:
    return posts_db.get(post_id)

def get_all_posts() -> List[Post]:
    return list(posts_db.values())

def update_post(post_id: int, **kwargs) -> Optional[Post]:
    post = posts_db.get(post_id)
    if not post:
        return None
    for field, value in kwargs.items():
        if value:
            setattr(post, field, value)
    post.updated_at = post.updated_at.now()
    return post

def delete_post(post_id: int) -> bool:
    return posts_db.pop(post_id, None) is not None
