from fastapi import FastAPI, Query, Path
from typing import Union, List
from typing_extensions import Annotated
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class User(BaseModel):
    username: str
    full_name: Union[str, None] = None
    
app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.post("/items-body/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

@app.put("/items-body/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}