from fastapi import FastAPI
from app import models
from app.db import engine
from app.routers import blogs, users

app = FastAPI(
    title="Fast API template project",
    description="Template Project for reference and quick start",
    version="1.0.0"
    )

models.Base.metadata.create_all(bind=engine)

app.include_router(blogs.router)
app.include_router(users.router)
