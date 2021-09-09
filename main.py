from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    a = "Welcome! My name is Clarissa Ache.\n This is what I did for my first project in Data Engineering & Ops class"
    return {"message":a}

@app.get("/add/{num1}/{num2}")
async def add(num1: int, num2: int):
    """Add two numbers together"""

    total = num1 + num2
    return {"total": total}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')