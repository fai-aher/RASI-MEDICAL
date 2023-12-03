from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine, Column, Integer, String, Sequence, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
from typing import List

from pydantic import BaseModel

# Define the FastAPI app
app = FastAPI()

# Define SQLAlchemy models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(100))
    created_at = Column(DateTime, default=datetime.utcnow)

# Database configuration
DATABASE_URL = "postgresql://auth_user:auth_password@10.46.16.3/auth_db"
engine = create_engine(DATABASE_URL)

# Create tables
Base.metadata.create_all(bind=engine)

# Define SessionLocal as a function
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# OAuth2PasswordBearer for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Pydantic model for the response
class UserResponse(BaseModel):
    username: str
    created_at: datetime

# Dependency to get the current user
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return authenticate_user(db, token, credentials_exception)

# Function to verify a user's credentials
def verify_token(db: Session, token: str):
    user = db.query(User).filter(User.username == token).first()
    if user:
        return user

# Function to authenticate a user
def authenticate_user(db: Session, token: str, credentials_exception):
    user = verify_token(db, token)
    if not user:
        raise credentials_exception
    return user

# Function to create a new user
def create_user(db: Session, username: str, password: str):
    hashed_password = pwd_context.hash(password)
    db_user = User(username=username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Endpoint to create a new user
@app.post("/users/", response_model=UserResponse)
def create_user_endpoint(username: str, password: str, db: Session = Depends(get_db)):
    user = create_user(db, username, password)
    return UserResponse(username=user.username, created_at=user.created_at)

# Function to create a JWT token
def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
    return encoded_jwt

# Token expiration time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Endpoint to retrieve a token
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = authenticate_user(form_data.username, form_data.password)

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_jwt_token(data={"sub": form_data.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}

# Endpoint to check health
@app.get("/health")
def health():
    return {"status": "ok"}

print("Auth service started")
