from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def greet():
    return "Hey! This is my first msg!!"

