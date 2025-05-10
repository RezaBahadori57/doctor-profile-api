from pydantic import BaseModel, EmailStr
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    email: EmailStr
    name: Optional[str]
    facebook_id: Optional[str]
