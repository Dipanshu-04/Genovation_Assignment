from pydantic import BaseModel

class UserLogin(BaseModel):
    username: str
    password: str

class PromptRequest(BaseModel):
    prompt: str
