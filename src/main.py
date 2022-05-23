'''Instancing the FastAPI class and work with path params'''
from enum import Enum
from datetime import datetime
from fastapi import FastAPI
from pydantic import BaseModel

# pylint: disable=pointless-string-statement
# pylint: disable=invalid-name

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Thirt"}]

class ModelName(str, Enum):
    '''
    <h3>Basic explanation:</h3>\n
    Class attributes with fixed values, which will be the available valid values
    <h3>Response exemple:</h3>\n
    Simple ModelName instance
    '''
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class Item(BaseModel):
    '''
    <h3>Basic explanation:</h3>\n
    A request body is data sent by the client to your API. A response body is the data your API sends to the client.\n
    Your API almost always has to send a response body. But clients don't
     necessarily need to send request bodies all the time.\n
    To declare a request body, you use Pydantic models with all their power and benefits.
    The same as when declaring query parameters, when a model attribute has a default value,
     it is not required. Otherwise, it is required. Use None to make it just optional.\n
    <h3>Response exemple:</h3>\n
    For example, this model above declares a JSON "object" (or Python dict) like.
    '''
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.post("/items/")
async def create_item(item: Item):
    '''
    <h3>Basic explanation:</h3>\n
    The same as when declaring query parameters, when a model attribute has a default value,\n
     it is not required. Otherwise, it is required. Use None to make it just optional.\n
    ...as description and tax are optional (with a default value of None), this JSON "object" would also be valid:
     { "name": "Foo", "price": 45.2 }\n
    <a href="https://fastapi.tiangolo.com/tutorial/body/" target="_blank">More details..</a>
    <h3>Request body exemple:</h3>\n
    { "name": "Foo", "description": "An optional description", "price": 45.2, "tax": null }
    <h3>Response exemple:</h3>\n
    { "name": "...", "description": "...", "price": 45.2, "tax": null, "price_with_tax": 45.2,
     "create_time": "2022-05-23 02:45:45.893837", "create_user": "Test User" }
    '''
    # Convert: convert the received Item object (Pydantic) and convert it to dict object
    item_dict = item.dict()
    # Manipulation: manipulate the dictionary as needed before performing the action.
    if item.tax:
        item_dict.update({"price_with_tax": item.price + item.tax})
    else:
        item_dict.update({"price_with_tax": item.price})
    current_time = str(datetime.now())
    request_user = "Test User"
    item_dict.update({"create_time": current_time, "create_user": request_user})
    # Action: perform the action
    #print(item_dict)
    return item_dict

@app.put("/items-request-body-path-params/{item_id}")
async def create_item_request_body_path_params(item_id: int, item: Item):
    '''
    <h3>Basic explanation:</h3>\n
    You can declare path parameters and request body at the same time.\n
    FastAPI will recognize that the function parameters that match path parameters should be
     taken from the path, and that function parameters that are declared to be Pydantic models should be
     taken from the request body.\n
    <a href="https://fastapi.tiangolo.com/tutorial/body/" target="_blank">More details..</a>
    <h3>Request body exemple:</h3>\n
    { "name": "Foo", "description": "An optional description", "price": 45.2, "tax": 3.9 }
    <h3>Response exemple:</h3>\n
    { "item_id": 3, "name": "...", "description": "...", "price": 45.2, "tax": 3.9, "price_with_tax": 49.1,
     "last_edit_time": "2022-05-23 03:29:58.636867", "last_edit_user": "Test User" }

    '''
    # Convert: convert the received Item object (Pydantic) and convert it to dict object
    item_dict = item.dict()
    # Manipulation: manipulate the dictionary as needed before performing the action.
    if item.tax:
        item_dict.update({"price_with_tax": item.price + item.tax})
    else:
        item_dict.update({"price_with_tax": item.price})
    current_time = str(datetime.now())
    request_user = "Test User"
    item_dict.update({"last_edit_time": current_time, "last_edit_user": request_user})
    # Action: perform the action
    #print(item_dict)
    return {"item_id": item_id, **item_dict}

@app.put("/items-request-body-path-query-params/{item_id}")
async def create_item_request_body_path_query_params(item_id: int, item: Item, q: str | None = None):
    '''
    <h3>Basic explanation:</h3>\n
    You can also declare body, path and query parameters, all at the same time.
     FastAPI will recognize each of them and take the data from the correct place.\n
    <a href="https://fastapi.tiangolo.com/tutorial/body/" target="_blank">More details..</a>
    <h3>Request body exemple:</h3>\n
    { "name": "Foo", "description": "An optional description", "price": 45.2, "tax": 3.9 }
    <h3>Response exemple:</h3>\n
    { "item_id": 3, "name": "...", "description": "...", "price": 45.2, "tax": 3.9, "price_with_tax": 49.1,
     "q": "string query param", "last_edit_time": "2022-05-23 03:29:58.636867", "last_edit_user": "Test User" }
    '''
    # Convert: convert the received Item object (Pydantic) and convert it to dict object
    item_dict = item.dict()
    # Manipulation: manipulate the dictionary as needed before performing the action.
    if item.tax:
        item_dict.update({"price_with_tax": item.price + item.tax})
    else:
        item_dict.update({"price_with_tax": item.price})
    current_time = str(datetime.now())
    request_user = "Test User"
    item_dict.update({"q": q, "last_edit_time": current_time, "last_edit_user": request_user})
    # Action: perform the action
    #print(item_dict)
    return {"item_id": item_id, **item_dict}

@app.get("/")
async def root():
    '''
    <h3>Basic explanation:</h3>\n
    Open your browser at root route. Eg.: http://127.0.0.1:8000.\n
    <a href="https://fastapi.tiangolo.com/tutorial/first-steps/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "message": "Hello World" }
    '''
    return {"message": "Hello World"}

@app.get("/items/")
async def read_dic_item(skip: int = 0, limit: int = 10):
    '''
    <h3>Basic explanation:</h3>\n
    When you declare other function parameters that are not part of the path parameters,
    they are automatically interpreted as "query" parameters.\n
    The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.\n
    Eg.: http://127.0.0.1:8000/items/?skip=0&limit=10\n
    <a href="https://fastapi.tiangolo.com/tutorial/body/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "file_path": "file_path" }
    '''
    return fake_items_db[skip : skip + limit]


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    '''
    <h3>Basic explanation:</h3>\n
    Basic request item.\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id": "item_id" }
    '''
    return {"item_id": item_id}


@app.get("/items-optional-param/{item_id}")
async def read_item_optional_param(item_id: str, q: str | None = None):
    '''
    <h3>Basic explanation:</h3>\n
    The same way, you can declare optional query parameters, by setting their default to None.\n
    In this case, the function parameter q will be optional, and will be None by default.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id": "item_id", "q": "..." } or { "item_id": "item_id" }
    '''
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}


@app.get("/items-required-query-param/{item_id}")
async def read_item_required_query_param(item_id: str, needy: str):
    '''
    <h3>Basic explanation:</h3>\n
    When you want to make a query parameter required, you can just not declare any default value.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id":"rest", "needy":"..." }
    '''
    item = {"item_id": item_id, "needy": needy}
    return item


@app.get("/items-optional-query-and-bool-param/{item_id}")
async def read_item_optional_query_and_bool_param(item_id: str, q: str | None = None, short: bool = False):
    '''
    <h3>Basic explanation:</h3>\n
    The same way, you can declare optional query parameters, by setting their default to None.\n
    In this case, the function parameter q will be optional, and will be None by default.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id": "item_id", "q": "...", description": "..." } or { "item_id": "item_id" }
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
    <h3>Basic explanation:</h3>\n
    When you want to make a query parameter required, you can just not declare any default value.\n
    In this case, the function parameter q will be required, and not have a value by default.\n
    You can define some parameters as required, some as having a default value, and some entirely optional.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id":"1", "needy":"...", "skip":skip, "limit": 10 }
    or { "item_id":"1", "needy":"...","skip": skip,"limit": null }
    '''
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item


@app.get("/users/me")
async def read_user_me():
    '''
    <h3>Basic explanation:</h3>\n
    Because path operations are evaluated in order, you need to make sure that the path
    for /users/me is declared before the one for /users/{user_id}\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "user_id": "the current user" }
    '''
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    '''
    <h3>Basic explanation:</h3>\n
    Basic request item.\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "user_id": "the user_id user" }
    '''
    return {"user_id": user_id}


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item_multiple_path_and_query_params(
    user_id: int, item_id: str, q: str | None = None, short: bool = False
    ):
    '''
    <h3>Basic explanation:</h3>\n
    You can declare multiple path parameters and query parameters at the same time, FastAPI knows which is which.\n
    And you don't have to declare them in any specific order. They will be detected by name.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id":"1", "owner_id":1,"q":"...","description":"This is an amazing item that has a long description" }
    or { "item_id":"1","owner_id":1 }
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
    <h3>Basic explanation:</h3>\n
    If you have a path operation that receives a path parameter,
     but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "model_name": ModelName.value, "message": Conditional get_model function return options }
    '''
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    '''
    <h3>Basic explanation:</h3>\n
    Using an option directly from Starlette you can declare a path parameter containing
     a path using a URL like '/files/{file_path:path}'\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "file_path": "file_path" }
    '''
    return {"file_path": file_path}
