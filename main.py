from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"data": {"name": "Gabby Jablo"}}

@app.get("/about")
def about():
    return {"data": {"age": 30, "hobbies": ["coding", "traveling", "cooking"]}}


