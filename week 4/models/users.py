from pydantic import BaseModel;

class UserModel(BaseModel):
    name: str
    year: str
    month: str
    day: str