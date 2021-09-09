import random
def question(what: str):
    """Ask the magic 8 ball"""
    
    magic = random.randint(1,8)
    message = what
    
    if question == " ":
        message == "OK, the rules are simple. You just need to type your question in this URL after /question/______"
    
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
    else:
        message = "OK, the rules are simple, you just need to type your question in the URL bar after \"/question/\"______"

    return {"message": message}
    
print(question('Will I ever become famous'))