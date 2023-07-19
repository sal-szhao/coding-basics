from fastapi import FastAPI, Query, Path
from typing import Union, List
from typing_extensions import Annotated
from pydantic import Required


app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello World"}

# @app.get('/items/{item_id}')
# async def read_item(item_id: int):
#     return {'item_id': item_id}


# Path is evaluated in order.
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


from enum import Enum

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

# File path in URL
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


# Query Parameters
fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip:skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Multiple parameters
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


# Required query parameter.
@app.get("/items-req/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Union[int, None] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item

# Required parameter by Required class.
@app.get("/items-reqreq/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)]=Required):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Required parameter by ...
@app.get("/items-reqdots/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)]=...):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Required parameter by removing default values (best practice).
@app.get("/items-reqdefault/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)]):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Validator on the parameters. (Preferred method of adding default values)
@app.get("/items-annodefault/")
async def read_items(q: Annotated[
        Union[str, None], Query(min_length=3, max_length=50, regex="^fixedquery$")
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Alternative way of setting default value.
@app.get("/items-altdefault/")
async def read_items(q: Union[str, None] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Query parameter list with defaults.
@app.get("/items-qlist/")
async def read_items(q: Annotated[List[str], Query()] = ["foo", "bar"]):
    query_items = {"q": q}
    return query_items


# Add title and description.
@app.get("/items-titledesc/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Create alias for the query parameter.
@app.get("/items-alias/")
async def read_items(item_query: Annotated[Union[str, None], Query(alias="item-query")] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if item_query:
        results.update({"item_query": item_query})
    return results

# Deprecated.
@app.get("/items-deprecated/")
async def read_items(
    q: Annotated[
        Union[str, None],
        Query(deprecated=True)
    ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

# Path variable & Greater than or equal to.
@app.get("/items-path/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
    q: str,
    size: Annotated[float, Query(gt=0, lt=10.5)]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
