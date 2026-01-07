import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "version": "OLD",
        "env": os.getenv("ENV", "unknown"),
        "image": os.getenv("IMAGE", "unknown"),
    }