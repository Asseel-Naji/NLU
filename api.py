from fastapi import FastAPI
import os
from fastapi.middleware.cors import CORSMiddleware

from config import *
### I know I know what I'm doing here hurts the eyes but I have 3 hours left and I still didn't shoot the video.

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    None,
    "null"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/test/")
async def root():
    return {"message": "Hello World"}
    # os.system(f"fish -C {path_api}")


@app.get("/run/")
async def run():
    # pass
    
    with open("./random_tests/trans.txt", "r") as f:
        text = f.read()
    # os.system(f"poetry run python {path_api}") 
    return {"text": text}
# RUN 
# uvicorn main:app --reload