import uvicorn
from fastapi import FastAPI


app = FastAPI()

def index():
    return {"message": "Hello, girlie!"}

@app.get("/trial")
def read_root():
    return index()

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=5000)
