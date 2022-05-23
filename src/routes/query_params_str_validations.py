'''
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
'''
from fastapi import APIRouter,Query

# pylint: disable=invalid-name

router = APIRouter()

@router.get("/items-query-params-str-validation/")
async def read_items_query_params_str_validation(q: str | None = None):
    '''
    <h3>Basic explanation:</h3>\n
    FastAPI allows you to declare additional information and validation for your parameters.\n
    The query parameter q is of type Union[str, None] (or str | None in Python 3.10), that means that it's of
     type str but could also be None, and indeed, the default value is None, so FastAPI will know it's not required.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-query-params-str-max-length-validation/")
async def read_items_query_params_str_max_length_validation(q: str | None = Query(default=None, max_length=50)):
    '''
    <h3>Basic explanation:</h3>\n
    Additional validation: We are going to enforce that even though q is optional, whenever it is provided,
     its length doesn't exceed 50 characters.\n
    Use Query as the default value: And now use it as the default value of your parameter,
     setting the parameter max_length to 50 and defaut to None.\n
    This will validate the data, show a clear error when the data is not valid,
     and document the parameter in the OpenAPI schema path operation.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-query-params-str-max-min-length-validation/")
async def read_items_query_params_str_max_mix_length_validation(
    q: str | None = Query(default=None, min_length=3, max_length=50)
    ):
    '''
    <h3>Basic explanation:</h3>\n
    Add more validations: You can also add a parameter 'min_length'.\n
    If 'q' query lengh param < 3 or > 50 will return an query params error.\n
    Eg.: {"detail":[{"loc":["query","q"],"msg":"ensure this value has at least 3 characters",
    "type":"value_error.any_str.min_length","ctx":{"limit_value":3}}]}\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
