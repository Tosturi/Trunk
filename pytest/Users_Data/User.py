from pydantic import BaseModel


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class Support(BaseModel):
    url: str
    text: str


class User(BaseModel):
    data: UserData
    support: Support
