from fastapi import FastAPI, Body, Cookie, Header, Response, Form
from typing import Union, List, Set, Dict
from typing_extensions import Annotated
from pydantic import BaseModel, Field, HttpUrl
from fastapi.responses import JSONResponse, RedirectResponse

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

# Body parameters.
@app.put("/items-bodyparam/{item_id}")
async def update_item(
    item_id: int, item: Item, user: User, importance: Annotated[int, Body(gt=0)]
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results

# Embed keyword in Body(), only working when single body.
@app.put("/items-embed/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# Use Field as model attributes.
class Item_Field(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None

@app.put("/items-field/{item_id}")
async def update_item(item_id: int, item: Annotated[Item_Field, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results

# Use list as model attributes.
class Item_List(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: list = []


@app.put("/items-list/{item_id}")
async def update_item(item_id: int, item: Item_List):
    results = {"item_id": item_id, "item": item}
    return results


# Alternative way of using list as model attributes.
class Item_List_Alt(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: List[str] = []


@app.put("/items-list-alt/{item_id}")
async def update_item(item_id: int, item: Item_List_Alt):
    results = {"item_id": item_id, "item": item}
    return results


# Use set as model attributes.
class Item_Set(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set = set()


@app.put("/items-set/{item_id}")
async def update_item(item_id: int, item: Item_Set):
    results = {"item_id": item_id, "item": item}
    return results


class Item_Set_Alt(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.put("/items-set-alt/{item_id}")
async def update_item(item_id: int, item: Item_Set_Alt):
    results = {"item_id": item_id, "item": item}
    return results


# Model nesting and URL special types.
class Image(BaseModel):
    url: HttpUrl
    name: str

class Item_Nest(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()
    images: Union[List[Image], None] = None

@app.put("/items-nest/{item_id}")
async def update_item(item_id: int, item: Item_Nest):
    results = {"item_id": item_id, "item": item}
    return results  

# Dictionaray.
@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights


# Modify examples.
class Item_Example(BaseModel):
    name: str = Field(example="Foo")
    description: Union[str, None] = Field(default=None, example="A very nice Item HHHHHHH")
    price: float = Field(example=35.4)
    tax: Union[float, None] = Field(default=None, example=3.2)

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item_Example):
    results = {"item_id": item_id, "item": item}
    return results


# Cookie.
@app.get("/items-cookie/")
async def read_items(ads_id: Annotated[Union[str, None], Cookie()] = None):
    return {"ads_id": ads_id}


# Header
@app.get("/items-header/")
async def read_items(user_agent: Annotated[Union[str, None], Header()] = None):
    return {"User-Agent": user_agent}

# Redirect and JSON Response
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


# Forms.
@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    return {"username": username}