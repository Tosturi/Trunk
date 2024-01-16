from pydantic import BaseModel, ValidationError
import requests


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


sup = """
{
        "url": "https://http.cat/",
        "text": "something else"
}
"""

try:
    ps = Support.model_validate_json(sup)
except ValidationError as e:
    print(e.json())
else:
    print(ps)
