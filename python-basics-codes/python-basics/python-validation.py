from typing_extensions import Annotated
from dataclasses import dataclass

'''
In python, semi-column is a type hint instead of a type check.
Similary, `Annotated` is also a type hint (type, metadata).
Annoatated used in FastAPI is a type hint.
'''
@dataclass
class ValueRange:
    lo: int
    hi: int

def test(T1: Annotated[int, ValueRange(-10, 5)], T2: int):
    pass

test('abc', 'abc')  # Even the tyoe is wrong, python will not raise errors.

'''
Pydantic v2 is often used in data type validation, which is extremely fast.
It is also convenient in data serialization like converting to JSON / HTML.
A good practice in fastAPI is to use Pydantic as inputs / response model.
'''

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str='John Doe'

user = User(id=4, name='Marcus')
# User(id='abc', name=123)      # Will raise a validation error.

# Output to dict / json.
print(user.dict())
print(user.json())

# Input convert from JSON.
m = User.parse_raw('{"id": "5", "name": "Peter"}')
print(m)

# Input convert from SQLAlchemy ORM.
from sqlalchemy.orm import registry
from sqlalchemy import Column, Integer, String

mapper_registry = registry()
@mapper_registry.mapped
class CompanyOrm:
    __tablename__ = "company_orm"

    id = Column(Integer, primary_key=True)
    company = Column(String)


class CompanyModel(BaseModel):
    id: int
    company: str

    class Config:
        orm_mode = True

co_orm = CompanyOrm(id=1, company="google")
print(co_orm)
co_model = CompanyModel.from_orm(co_orm)
print(co_model)

'''
User can define custom validators for the pydantic model.
'''
from pydantic import validator

class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    # values contain verified fields.
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalpha(), 'must be alphanumeric'
        return v
    
print(UserModel(name='samuel colvin', username='scolvin', password1='zxcvbn',
                password2='zxcvbn'))
