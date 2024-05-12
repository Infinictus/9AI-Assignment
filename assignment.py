from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["blogDB"]

app = FastAPI()

class Blog(BaseModel):
    title: str
    content: str
    likes: Optional[int] = 0
    dislikes: Optional[int] = 0

@app.post("/blog/")
async def create_blog(blog: Blog):
    blog_dict = blog.dict()
    db["blogs"].insert_one(blog_dict)
    return blog_dict

@app.get("/blog/{blog_id}")
async def read_blog(blog_id: str):
    blog = db["blogs"].find_one({"_id": blog_id})
    return blog

@app.put("/blog/{blog_id}")
async def update_blog(blog_id: str, blog: Blog):
    db["blogs"].update_one({"_id": blog_id}, {"$set": blog.dict()})
    return db["blogs"].find_one({"_id": blog_id})

@app.delete("/blog/{blog_id}")
async def delete_blog(blog_id: str):
    db["blogs"].delete_one({"_id": blog_id})
    return {"message": "Blog deleted"}
