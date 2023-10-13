from pydantic import BaseModel

class UserUpdate(BaseModel):
    username: str
    email: str

class PasswordChange(BaseModel):
    old_password: str
    new_password: str
