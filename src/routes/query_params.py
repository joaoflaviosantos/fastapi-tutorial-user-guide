'''
Exemples on: https://fastapi.tiangolo.com/tutorial/query-params/
'''
from fastapi import APIRouter

# pylint: disable=invalid-name

router = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Thirt"}]

@router.get("/items/")
async def read_dic_item(skip: int = 0, limit: int = 10):
    '''
    <h3>Basic explanation:</h3>\n
    When you declare other function parameters that are not part of the path parameters,
    they are automatically interpreted as "query" parameters.\n
    The query is the set of key-value pairs that go after the ? in a URL, separated by & characters.\n
    Eg.: http://127.0.0.1:8000/items/?skip=0&limit=10\n
    <a https://fastapi.tiangolo.com/tutorial/query-params/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "file_path": "file_path" }
    '''
    return fake_items_db[skip : skip + limit]

@router.get("/items-optional-param/{item_id}")
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

@router.get("/items-required-query-param/{item_id}")
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

@router.get("/items-optional-query-and-bool-param/{item_id}")
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

@router.get("/items-required-and-optional-params/{item_id}")
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

@router.get("/users/{user_id}/items/{item_id}")
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
