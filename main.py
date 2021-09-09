from fastapi import FastAPI
import uvicorn
import random

app = FastAPI()

@app.get("/")
async def root():
    a = "Ask the magic 8 ball a question"
    return {"message":a}

@app.get("/question/{q}")
async def add(q: str):
    """Ask the magic 8 ball"""

    magic = random.randint(1,8)
    
    if question == "" OR " ":
        message == "OK, the rules are simple, you just need to type your question in this URL after /question/______"
    
    elif magic == 1:
        message = "It is certain"
    
    elif magic == 2:
        message = "Don't count on it"
    
    elif magic == 3:
        message = "You may rely on it"
    
    elif magic == 4:
        message = "Ask again later"
    
    elif magic == 5:
        message = "Concentrate and ask again"
    
    elif magic == 6:
        message = "Reply hazy, try again"
    
    elif magic == 7:
        message = "Better not tell you now"
    
    elif magic == 8:
        message = "My sources say no"

    return {"message": message}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')