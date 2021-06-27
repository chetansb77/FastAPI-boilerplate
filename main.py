from fastapi import FastAPI
from app.blog import schemas as blogschemas

app = FastAPI()


@app.post('/create-blog')
def create_blog(blog: blogschemas.Blog):
    return blog
