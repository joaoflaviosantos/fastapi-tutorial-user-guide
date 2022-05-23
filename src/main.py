'''Instancing the FastAPI class and work with path params'''
from enum import Enum
from fastapi import FastAPI

# pylint: disable=pointless-string-statement
# pylint: disable=invalid-name

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Thirt"}]

class ModelName(str, Enum):
    '''Class attributes with fixed values, which will be the available valid values'''
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/items/")
async def read_dic_item(skip: int = 0, limit: int = 10):
    '''
    When you declare other function parameters that are not part of the path parameters,
    they are automatically interpreted as "query" parameters.\n
    The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.\n
    Eg.: http://127.0.0.1:8000/items/?skip=0&limit=10\n
    Retuns {"file_path": "file_path"} message.
    '''
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    '''
    Basic request item.\n
    Retuns {"item_id": "item_id"} message.
    '''
    return {"item_id": item_id}


@app.get("/items-optional-param/{item_id}")
async def read_item_optional_param(item_id: str, q: str | None = None):
    '''
    The same way, you can declare optional query parameters, by setting their default to None.\n
    In this case, the function parameter q will be optional, and will be None by default.\n
    Retuns {"item_id": "item_id", "q": "q"} or {"item_id": "item_id"} message.
    '''
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items-required-param/{item_id}")
async def read_item_required_param(item_id: str, needy: str):
    '''
    When you want to make a query parameter required, you can just not declare any default value.\n
    Retuns {"item_id":"rest", "needy":"..."} message.
    '''
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items-optional-and-bool-param/{item_id}")
async def read_item_optional_and_bool_param(item_id: str, q: str | None = None, short: bool = False):
    '''
    The same way, you can declare optional query parameters, by setting their default to None.\n
    In this case, the function parameter q will be optional, and will be None by default.\n
    Retuns {"item_id": "item_id", "q": "...", description": "..."} or {"item_id": "item_id"} message.
    '''
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/items-required-and-optional-params/{item_id}")
async def read_item_required_and_bool_param(
    item_id: str, needy: str, skip: int = 0, limit: int | None = None
    ):
    '''
    When you want to make a query parameter required, you can just not declare any default value.\n
    In this case, the function parameter q will be required, and not have a value by default.\n
    You can define some parameters as required, some as having a default value, and some entirely optional:\n
    Retuns {"item_id":"1","needy":"...", "skip":skip,"limit": limit}
    or {"item_id":"1","needy":"...","skip": skip,"limit": null} message.
    '''
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/users/me")
async def read_user_me():
    '''
    Because path operations are evaluated in order, you need to make sure that the path
    for /users/me is declared before the one for /users/{user_id}\n
    Retuns {"user_id": "the current user"} message.
    '''
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    '''
    Basic request item.\n
    Retuns {"user_id": "the user_id user"} message.
    '''
    return {"user_id": user_id}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item_multiple_path_and_query_params(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
    ):
    '''
    You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.\n
    And you don't have to declare them in any specific order. They will be detected by name.\n
    Retuns {"item_id":"1","owner_id":1,"q":"q","description":"This is an amazing item that has a long description"}
    or {"item_id":"1","owner_id":1} message.
    '''
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    '''
    If you have a path operation that receives a path parameter,
     but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.\n
    Retuns {"item_id": "item_id"} message.
    '''
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    '''
    Using an option directly from Starlette you can declare a path parameter containing\n
     a path using a URL like '/files/{file_path:path}'\n
    Retuns {"file_path": "file_path"} message.
    '''
    return {"file_path": file_path}
