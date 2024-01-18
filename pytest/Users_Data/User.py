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


class SingleUser(BaseModel):
    data: UserData
    support: Support


class UserList(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[UserData]
    support: Support


class CreateData(BaseModel):
    name: str = None
    job: str = None
    id: str
    createdAt: str


class UpdateData(BaseModel):
    name: str = None
    job: str = None
    updatedAt: str
