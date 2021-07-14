from os import name
from fastapi import FastAPI, Depends, status, Response, HTTPException
from app.blog import schemas as blogschemas
from app.authentication import schemas as authschemas
from app import models
from app.db import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/create-blog', status_code=status.HTTP_201_CREATED)
def create_blog(blog: blogschemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.blogmodels.Blog(title=blog.title, description=blog.description,
                                        body=blog.body, published=blog.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs', status_code=status.HTTP_200_OK, response_model=List[blogschemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.blogmodels.Blog).all()
    return blogs


@app.get('/blog/{id}', status_code=status.HTTP_200_OK, response_model=blogschemas.ShowBlog)
def get_blob_by_id(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.blogmodels.Blog).filter(models.blogmodels.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.blogmodels.Blog).filter(models.blogmodels.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Details": "Deleted"}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: blogschemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.blogmodels.Blog).filter(models.blogmodels.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    blog.update(blog.__dict__)
    db.commit()
    return "Updated"


@app.post('/user')
def create_user(user: authschemas.User, db: Session = Depends(get_db)):
    new_user = models.authmodels.User(name=user.name, email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user