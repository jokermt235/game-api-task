from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    name: str
    email: str


class UserReadSchema(BaseModel):
    id: int
    name: str
    email: str
