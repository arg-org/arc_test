from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health():
    return {"status": "ok 0105T0910"}
