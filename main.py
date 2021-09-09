from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    a = "Welcome! My name is Clarissa Ache.\n This is what I did for my first project in Data Ops class"
    return {"message":a}

@app.get("/program/mids")
async def program(prog_name: str):
    """Greet students"""
        message = "Welcome MIDS Student!"
    return {"message": message}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')