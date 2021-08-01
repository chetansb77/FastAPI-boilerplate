from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from . import models
from . import schemas as blogschemas


class BlogController:

    @staticmethod
    def get_all(db: Session):
        blogs = db.query(models.Blog).all()
        return blogs

    @staticmethod
    def get_by_id(id: int, db: Session):
        blog = db.query(models.Blog).filter(
            models.Blog.id == id).first()
        if not blog:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id:{id} not found")
        return blog

    @staticmethod
    def create(blog: blogschemas.Blog, db: Session):
        new_blog = models.Blog(title=blog.title, description=blog.description,
                                          body=blog.body, published=blog.published)
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog

    @staticmethod
    def delete(id: int, db: Session):
        blog = db.query(models.Blog).filter(
            models.Blog.id == id)
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id:{id} not found")
        blog.delete(synchronize_session=False)
        db.commit()

    @staticmethod
    def update(id: int, blog: blogschemas.Blog, db: Session):
        blog = db.query(models.Blog).filter(
            models.Blog.id == id)
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Blog with id:{id} not found")
        blog.update(blog.__dict__)
        db.commit()
        return "Updated"
