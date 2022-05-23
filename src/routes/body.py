'''Exemples on: https://fastapi.tiangolo.com/tutorial/body/'''
from datetime import datetime
from fastapi import APIRouter
from pydantic import BaseModel

# pylint: disable=invalid-name

router = APIRouter()

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

@router.post("/items/")
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

@router.put("/items-request-path-body-params/{item_id}")
async def create_item_request_path_body_params(item_id: int, item: Item):
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

@router.put("/items-request-body-path-query-params/{item_id}")
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
