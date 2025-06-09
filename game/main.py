from fastapi import FastAPI
from api.v1 import tournament as tournament_router

app = FastAPI(title="Tournament API", version="1.0.0")

app.include_router(tournament_router.router, prefix="/api/v1")


@app.get("/")
def read_root():
    return {"message": "Tournament api starting to accept connections"}
