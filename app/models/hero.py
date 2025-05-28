from sqlmodel import SQLModel, Field
from typing import Optional

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int]
    
    
# class HeroUpdate(SQLModel):
#     name: Optional[str] = None
#     secret_name: Optional[str] = None
#     age: Optional[int] = None