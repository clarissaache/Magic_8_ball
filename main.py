from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    a = "Welcome! My name is Clarissa Ache.\n This is what I did for my first project in Data Ops class"
    return {"message":a}

@app.get("/program/{prog_name}")
async def program(prog_name: str):
    """Enter a name and capitalize first letter"""
    if prog_name == 'mids'
        message = "Welcome MIDS Student!"
    else:
        message = "Sorry! Your Master's program is not supported by this website"
    return {"message": message}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')