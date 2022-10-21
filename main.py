from fastapi import FastAPI, Request
import time
from typing import Union
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()


@app.get("/")
def read_root():
    return "Server is Up"


origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

