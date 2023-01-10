from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def index():
    return 'this is my first fastapi app'

@app.get("/about")
def about():
    return 'this is my about page'
