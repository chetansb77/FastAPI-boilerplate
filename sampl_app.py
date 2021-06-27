from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Default endpoint


@app.get('/')
def index():
    return {'data': {
        'name': "Chetan"
    }}

# About endpoint
@app.get('/about')
def about():
    return {'data': 'about details'}


# Example for path params
@app.get('/blog/{id}')
def blog(id: int):
    return {'data': id}


# Example for Query Params
@app.get('/blog')
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f"{limit} published number of blogs"}
    else:
        return {'data': f"{limit} number of blogs"}


# Sample request body model
class Blog(BaseModel):
    title: str
    description: str
    body: str
    published: Optional[bool]


@app.post('/create-blog')
def create_blog(blog: Blog):
    return {'data': f'Blog has been created with title: {blog.title}'}