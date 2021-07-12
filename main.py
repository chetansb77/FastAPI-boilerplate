from fastapi import FastAPI, Depends, status, Response, HTTPException
from app.blog import schemas as blogschemas
from app.blog import models
from app.db import engine, SessionLocal
from sqlalchemy.orm import Session

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
    new_blog = models.Blog(title=blog.title, description=blog.description,
                           body=blog.body, published=blog.published)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get('/blogs')
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@app.get('/blog/{id}',  status_code=status.HTTP_200_OK)
def get_blob_by_id(id, response: Response, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    return blog


@app.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {"Details": "Deleted"}


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id, blog: blogschemas.Blog, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id:{id} not found")
    blog.update(blog.__dict__)
    db.commit()
    return "Updated"