from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome! My name is Clarissa Ache.\n This is what I did for my first project in Data Ops class"}

@app.get("/add/{name}")
async def add(name: str):
    """Enter a name and capitalize first letter"""
    
    name_c = name.capitalize()
    return {"Your name is": name_c}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')