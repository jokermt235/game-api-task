from fastapi import FastAPI
#from app.api.v1 import user  # если у тебя есть свои роутеры

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello, world!"}
