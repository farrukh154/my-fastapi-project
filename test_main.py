import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

client = TestClient(app)

@pytest.fixture(scope="module")
def test_db():
    engine = create_engine("postgresql://username:password@localhost:5432/test_db")
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base.metadata.create_all(bind=engine)
    
    yield TestingSessionLocal()

    Base.metadata.drop_all(bind=engine)

def test_register(test_db):
    response = client.post(
        "/register/",
        json={"username": "testuser", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"

def test_login(test_db):
    response = client.post(
        "/login/",
        data={"username": "testuser", "password": "testpassword"},
    )
    assert response.status_code == 200
    assert response.json()["message"] == "Login successful"

def test_create_post(test_db):
    response = client.post(
        "/posts/",
        json={"title": "Test Post", "content": "This is a test post."},
        params={"user_id": 1},
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"

def test_get_posts(test_db):
    response = client.get("/users/1/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
