from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from ..db import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    body = Column(String)
    published = Column(Boolean)