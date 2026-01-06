import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {
        "version": "NEW_VERSION",
        "env": os.getenv("ENV", "unknown"),
        "image": os.getenv("IMAGE", "unknown"),
    }