'''Exemples on: https://fastapi.tiangolo.com/tutorial/path-params/''' # pylint: disable=invalid-name
from enum import Enum
from fastapi import APIRouter

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

router = APIRouter()

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    '''
    <h3>Basic explanation:</h3>\n
    Basic request item.\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "item_id": "item_id" }
    '''
    return {"item_id": item_id}

@router.get("/users/me")
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


@router.get("/users/{user_id}")
async def read_user(user_id: str):
    '''
    <h3>Basic explanation:</h3>\n
    Basic request item.\n
    <a href="https://fastapi.tiangolo.com/tutorial/path-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "user_id": "the user_id user" }
    '''
    return {"user_id": user_id}

@router.get("/models/{model_name}")
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


@router.get("/files/{file_path:path}")
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
