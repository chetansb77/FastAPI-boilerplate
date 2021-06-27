from typing import Optional
from pydantic import BaseModel

# Sample request body model
class Blog(BaseModel):
    title: str
    description: str
    body: str
    published: Optional[bool]