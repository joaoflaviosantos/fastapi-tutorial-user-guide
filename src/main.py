'''Instancing the FastAPI class and work with path params'''
from enum import Enum
from fastapi import FastAPI

# pylint: disable=pointless-string-statement
# pylint: disable=invalid-name

class ModelName(str, Enum):
    '''Class attributes with fixed values, which will be the available valid values'''
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    'Retuns {"item_id": "item_id"} message.'
    return {"item_id": item_id}

'''
Because path operations are evaluated in order, you need to make sure that the path
for /users/me is declared before the one for /users/{user_id}
'''
@app.get("/users/me")
async def read_user_me():
    'Retuns {"user_id": "the current user"} message.'
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    'Retuns {"user_id": "the user_id user"} message.'
    return {"user_id": user_id}

'''
If you have a path operation that receives a path parameter,
but you want the possible valid path parameter values to be predefined, you can use a standard Python Enum.
'''
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    '''Retuns {"item_id": "item_id"} message.'''
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

'''
Using an option directly from Starlette you can declare a path parameter containing a path using a URL like '/files/{file_path:path}'
'''
@app.get("/files//{file_path:path}")
async def read_file(file_path: str):
    '''Retuns {"file_path": "file_path"} message.'''
    return {"file_path": file_path}
