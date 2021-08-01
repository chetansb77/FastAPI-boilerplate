from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..db import get_db
from sqlalchemy.orm import Session
from typing import List
from ..authentication import schemas as authschemas
from ..authentication.controller import UserController as User

router = APIRouter(prefix="/user", tags=['users'])


@router.post('/', response_model=authschemas.ShowUser)
def create_user(user: authschemas.User, db: Session = Depends(get_db)):
    return User.create(user, db)


@router.get('/getall', response_model=List[authschemas.ShowUser])
def get_all_user(db: Session = Depends(get_db)):
    return User.get_all(db)
