from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, Base, get_db
from typing import List


# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Регистрация пользователя
@app.post("/register/", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)

# Логин (просто проверка существования пользователя)
@app.post("/login/")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=username)
    if not user or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

# Создание поста
@app.post("/posts/", response_model=schemas.Post)
def create_post(post: schemas.PostCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post, user_id=user_id)

# Получение постов пользователя
@app.get("/users/{user_id}/posts", response_model=List[schemas.Post])
def get_posts(user_id: int, db: Session = Depends(get_db)):
    return crud.get_posts_by_user_id(db=db, user_id=user_id)
