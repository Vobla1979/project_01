from fastapi import FastAPI, HTTPException
from crud import create_user, get_user, get_all_users, update_user, delete_user
from crud import create_post, get_post, get_all_posts, update_post, delete_post
from schemas import UserCreate, UserUpdate, UserOut, PostCreate, PostUpdate, PostOut

app = FastAPI()

# --- User Endpoints ---
@app.post("/users/", response_model=UserOut)
async def create_user_view(user: UserCreate):
    new_user = create_user(user.email, user.login, user.password)
    return UserOut(
        id=new_user.id,
        email=new_user.email,
        login=new_user.login,
        created_at=new_user.created_at.isoformat(),
        updated_at=new_user.updated_at.isoformat()
    )

@app.get("/users/", response_model=list[UserOut])
async def list_users():
    return [
        UserOut(
            id=u.id,
            email=u.email,
            login=u.login,
            created_at=u.created_at.isoformat(),
            updated_at=u.updated_at.isoformat()
        )
        for u in get_all_users()
    ]

@app.get("/users/{user_id}", response_model=UserOut)
async def get_user_view(user_id: int):
    user = get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut(
        id=user.id,
        email=user.email,
        login=user.login,
        created_at=user.created_at.isoformat(),
        updated_at=user.updated_at.isoformat()
    )

@app.put("/users/{user_id}", response_model=UserOut)
async def update_user_view(user_id: int, user: UserUpdate):
    updated_user = update_user(user_id, **user.dict(exclude_unset=True))
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut(
        id=updated_user.id,
        email=updated_user.email,
        login=updated_user.login,
        created_at=updated_user.created_at.isoformat(),
        updated_at=updated_user.updated_at.isoformat()
    )

@app.delete("/users/{user_id}")
async def delete_user_view(user_id: int):
    if not delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

# --- Post Endpoints ---
@app.post("/posts/", response_model=PostOut)
async def create_post_view(post: PostCreate):
    if not get_user(post.author_id):
        raise HTTPException(status_code=404, detail="Author not found")
    new_post = create_post(post.author_id, post.title, post.content)
    return PostOut(
        id=new_post.id,
        author_id=new_post.author_id,
        title=new_post.title,
        content=new_post.content,
        created_at=new_post.created_at.isoformat(),
        updated_at=new_post.updated_at.isoformat()
    )

@app.get("/posts/", response_model=list[PostOut])
async def list_posts():
    return [
        PostOut(
            id=p.id,
            author_id=p.author_id,
            title=p.title,
            content=p.content,
            created_at=p.created_at.isoformat(),
            updated_at=p.updated_at.isoformat()
        )
        for p in get_all_posts()
    ]

@app.get("/posts/{post_id}", response_model=PostOut)
async def get_post_view(post_id: int):
    post = get_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostOut(
        id=post.id,
        author_id=post.author_id,
        title=post.title,
        content=post.content,
        created_at=post.created_at.isoformat(),
        updated_at=post.updated_at.isoformat()
    )

@app.put("/posts/{post_id}", response_model=PostOut)
async def update_post_view(post_id: int, post: PostUpdate):
    updated_post = update_post(post_id, **post.dict(exclude_unset=True))
    if not updated_post:
        raise HTTPException(status_code=404, detail="Post not found")
    return PostOut(
        id=updated_post.id,
        author_id=updated_post.author_id,
        title=updated_post.title,
        content=updated_post.content,
        created_at=updated_post.created_at.isoformat(),
        updated_at=updated_post.updated_at.isoformat()
    )

@app.delete("/posts/{post_id}")
async def delete_post_view(post_id: int):
    if not delete_post(post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}
