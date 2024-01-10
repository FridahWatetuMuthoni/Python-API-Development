from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = False
    rating: Optional[int] = None

@app.get("/")
def root():
    return {"message":"hello people"}

@app.get("/posts")
def posts():
    return {"message":"This is the post page"}

@app.post("/createposts")
def create_post(post: Post):
    post = post.dict()
    print(type(post))
    return {"data":"new post"}