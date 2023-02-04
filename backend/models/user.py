from pydantic import BaseModel


class User(BaseModel):
    username: str
    _disabled: bool | None = None

class UserInDB(User):
    hpwd: str
