from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": "Blog list"}

@app.get("/blog/{blog_id}")
def get_blog(blog_id: int):
    return {"data": {"id": blog_id, "title": f"Blog {blog_id}", "content": "This is the content of the blog post."}}

@app.get("/blog/{blog_id}/comments")
def get_comments(blog_id: int):
    return {"data": [{"id": 1, "blog_id": blog_id, "content": "Great post!"}, {"id": 2, "blog_id": blog_id, "content": "Thanks for sharing!"}]}


