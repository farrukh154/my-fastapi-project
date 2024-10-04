from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class PostBase(BaseModel):
    text: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    created_at: datetime
    updated_at: datetime
    posts: List[Post] = []

    class Config:
        orm_mode = True
