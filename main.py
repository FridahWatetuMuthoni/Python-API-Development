from typing import Optional
from fastapi import FastAPI,Response, status,HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = False
    rating: Optional[int] = None


my_posts = [
    {
        "id": 1,
        "title":"example title one",
        "content": "content example one",
    },
    {
        "id": 2,
        "title":"My favoute foods",
        "content": "I love pizza and chicken",
    }
]

def find_post(id):
    for post in my_posts:
        if(post["id"] == id):
            return post

@app.get("/")
def root():
    return {"message":"hello people"}

@app.get("/posts")
def posts():
    return {"data":my_posts}

@app.get("/posts/{id}")
def get_post(id:int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with the id of {id} was not found")
    return {"data":post}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000000)
    my_posts.append(post_dict)
    status
    return {"data":post_dict}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with the id of {id} was not found")
    return {"message":f"The post of id {id} was deleted successfully"}


@app.put("/posts/{id}")
def update_post(id:int, updated_post: Post):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with the id of {id} was not found")
    print(updated_post.dict())
    return {"message":f"The post of id {id} was updated successfully"}
