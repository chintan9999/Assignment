from fastapi import FastAPI, Request
import random  # to generate random words from the word sample given
from collections import deque # to keep track of last called APIs history
import re # To remove any non alphabetical characters from the input word
import requests
import json
from json import JSONDecodeError

app = FastAPI() # creates a new instance of the FastAPI framework

# A list to store the last 10 API requests

audit_log = deque(maxlen=10) #Max. length of data to be stored

@app.get("/jumble/{word}") #adding HTTP GET route to the app instance
def jumble(word: str):
    # Re-arrange any alpha-numeric characters randomly
    jumbled_word = ''.join(random.sample(word, len(word)))
    # Sanitize the input to only include alphabetical characters
    sanitized_word = re.sub(r'[^a-zA-Z]', '', word)
    word_list = list(sanitized_word)
    random.shuffle(word_list)
    jumbled_word_sanitized = ''.join(word_list)
    return {"original_word": word, "jumbled_word": jumbled_word, "sanitized_jumbled_word": jumbled_word_sanitized}


@app.get("/audit") # defines an HTTP endpoint for handling HTTP GET requests to the "/audit" URL path.
async def audit():
    return {"audit_log": list(audit_log)}

@app.middleware("http") # to register a middleware function that will be executed for every incoming HTTP request.
async def audit_middleware(request, call_next):
    """Logs incoming API requests."""
    response = await call_next(request)
    audit_dict = {}
    audit_dict["Url"] = request.url
    try:
        payload = await request.body()
    except JSONDecodeError:
        payload = None
    audit_dict["payload"] = payload
    
    audit_log.append(audit_dict)
    
    return response


