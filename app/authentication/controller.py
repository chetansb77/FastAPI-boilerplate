from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Authentication:

    @staticmethod
    def get_password_hash(password: str):
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str):
        return pwd_context.verify(plain_password, hashed_password)


class UserController:

    @staticmethod
    def get_all(db: Session):
        users = db.query(models.User).all()
        if not users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail=f"No users available")
        return users

    def create(user: schemas.User, db: Session):
        new_user = models.User(name=user.name, email=user.email,
                               password=Authentication.get_password_hash(user.password))
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
