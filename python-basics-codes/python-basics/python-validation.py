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

test('abc', 'abc')  # Even the type is wrong, python will not raise errors.

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
print(user.model_dump())
print(user.model_dump_json())

# Input convert from JSON.
m = User.model_validate_json('{"id": "5", "name": "Peter"}')
print(m)

print("-" * 65)

'''
Input convert from SQLAlchemy ORM.
'''
from sqlalchemy.orm import registry
from sqlalchemy import Column, Integer, String
from pydantic import ConfigDict

mapper_registry = registry()
@mapper_registry.mapped
class CompanyOrm:
    __tablename__ = "company_orm"

    id = Column(Integer, primary_key=True)
    company = Column(String)


class CompanyModel(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    company: str

co_orm = CompanyOrm(id=1, company="google")
print(co_orm)
co_model = CompanyModel.model_validate(co_orm)
print(co_model)

print("-" * 65)


'''
One can set `strict` to be True to disable the type coercion.
'''

class coerce(BaseModel):
    isTrue: bool

class non_coerce(BaseModel):
    model_config = ConfigDict(strict=True)
    isTrue: bool

print(coerce(isTrue=1))
# print(non_coerce(isTrue=1))       # In strict mode, int cannot be converted to bool.

print("-" * 65)


'''
User can define custom validators for the pydantic model.
'''
from pydantic import field_validator
from pydantic_core.core_schema import FieldValidationInfo

class UserModel(BaseModel):
    name: str
    username: str
    password1: str
    password2: str

    @field_validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    # values contain verified fields.
    @field_validator('password2')
    def passwords_match(cls, v, info: FieldValidationInfo):
        if 'password1' in info.data and v != info.data['password1']:
            raise ValueError('passwords do not match')
        return v

    @field_validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalpha(), 'must be alphanumeric'
        return v
    
print(UserModel(name='samuel colvin', username='scolvin', password1='zxcvbn',
                password2='zxcvbn'))

# Will throw a validation error.
# print(UserModel(name='samuelcolvin', username='scolvin', password1='zxcvbn',
#                 password2='zxcvbn'))