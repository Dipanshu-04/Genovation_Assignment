from fastapi import FastAPI, Depends, HTTPException, Header
from models import UserLogin, PromptRequest
from auth import *
from datetime import datetime, timezone
from response import generate_dummy_response
import json
import os


app = FastAPI()


# Store prompt history per user
HISTORY_FILE = "history.json"

# Initialize user_history
if os.path.exists(HISTORY_FILE):
    with open(HISTORY_FILE, "r") as f:
        user_history = json.load(f)
else:
    user_history = {}

def save_history():
    with open(HISTORY_FILE, "w") as f:
        json.dump(user_history, f, indent=2)

#Login Route
@app.post("/login")
def login(user: UserLogin):
    stored_pw = users_db.get(user.username)
    if not stored_pw or not verify_password(user.password, stored_pw):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_token(user.username)
    return {"token": token}

#token authorization
def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    token = authorization.split(" ")[1]
    return decode_token(token)

#Prompt Route
@app.post("/prompt")
def submit_prompt(request: PromptRequest, username: str = Depends(get_current_user)):
    # Dummy response
    response = generate_dummy_response(request.prompt)

    # Save to user history
    entry = {
        "timestamp": datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", ""),
        "prompt": request.prompt,
        "response": response
    }
    # Append to the user's history
    if username not in user_history:
        user_history[username] = []  # initialize list
    user_history[username].append(entry)
    save_history()

    return {"response": response}
#History Route
@app.get("/history")
def get_history(username: str = Depends(get_current_user)):
    return user_history.get(username, [])

