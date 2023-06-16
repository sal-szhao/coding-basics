from fastapi import FastAPI, HTTPException, Request, status, Depends, Cookie, Header
from fastapi.responses import JSONResponse

from typing import Union, Set
from typing_extensions import Annotated

from pydantic import BaseModel

app = FastAPI()

items = {"foo": "The Foo Wrestlers"}

# Raising exceptions and customized headers. 
@app.get("/items/{item_id}", tags=['items'])
async def read_item(item_id: str):
    if item_id not in items:
        raise HTTPException(
            status_code=404, 
            detail="Item not found", 
            headers={"X-Error": "There goes my error"}
        )
    return {"item": items[item_id]}


# Exception handler.
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    return JSONResponse(
        status_code=418,
        content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
    )

@app.get("/unicorns/{name}", tags=["unicorn"])
async def read_unicorn(name: str):
    if name == "yolo":
        raise UnicornException(name=name)
    return {"unicorn_name": name}


# Add status code, tags, summary and descriptions.
class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: Set[str] = set()


@app.post(
    "/items-status/", 
    response_model=Item, 
    status_code=status.HTTP_201_CREATED, 
    tags=["items"],
    summary="Create an item",
    response_description="The created item",
    # description="Create an item with all the information, name, description, price, tax and a set of unique tags",
)
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag strings for this item
    """
    return item



# Dependencies.
async def common_parameters(
    q: Union[str, None] = None, skip: int = 0, limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}

CommonsDep = Annotated[dict, Depends(common_parameters)]

@app.get("/items-depend/")
async def read_items(commons: CommonsDep):
    return commons

@app.get("/users-depend/")
async def read_users(commons: CommonsDep):
    return commons


# Using classes and shortcuts.
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

class CommonQueryParams:
    def __init__(self, q: Union[str, None] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items-classdepend/")
async def read_items(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response



# Sub-dependencies.
def query_extractor(q: Union[str, None] = None):
    return q

def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()] = "123",
):
    if not q:
        return last_query
    return q

@app.get('/items-subdepend/')
async def read_query(
    query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]
):
    return {"q_or_cookie": query_or_default}


# Dependencies in path operations.
async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != "fake-super-secret-key":
        raise HTTPException(status_code=400, detail="X-Key header invalid")
    return x_key

@app.get("/items-pathdepend/", dependencies=[Depends(verify_token), Depends(verify_key)])
async def read_items():
    return [{"item": "Foo"}, {"item": "Bar"}]


# Global dependencies.
app1 = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

@app1.get("/items/")
async def read_items():
    return [{"item": "Portal Gun"}, {"item": "Plumbus"}]

