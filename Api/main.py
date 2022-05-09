from hepatica import write, read, manage

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

@app.get("/")
async def main():
    pass

@app.post("/write")
async def write_api():
    pass

@app.post("/write")
async def write_api():
    pass

@app.get("/product_info")
async def read_api(product:str):
    pass

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)