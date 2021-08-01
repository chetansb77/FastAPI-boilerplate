from fastapi import APIRouter, Depends, status, Response, HTTPException
from ..db import get_db
from sqlalchemy.orm import Session
from typing import List
from ..blog import schemas as blogschemas
from ..blog.controller import BlogController as Blog

router = APIRouter(prefix="/blog", tags=["blogs"])


@router.get('/', status_code=status.HTTP_200_OK, response_model=List[blogschemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = Blog.get_all(db)
    return blogs


@router.post('/create-blog', status_code=status.HTTP_201_CREATED)
def create_blog(blog: blogschemas.Blog, db: Session = Depends(get_db)):
    new_blog = Blog.create(blog=blog, db=db)
    return new_blog


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=blogschemas.ShowBlog)
def get_blob_by_id(id, response: Response, db: Session = Depends(get_db)):
    return Blog.get_by_id(int(id), db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db: Session = Depends(get_db)):
    Blog.delete(int(id), db)
    return {"Details": "Deleted"}


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: blogschemas.Blog, db: Session = Depends(get_db)):
    return Blog.update(int(id), blog, db)
