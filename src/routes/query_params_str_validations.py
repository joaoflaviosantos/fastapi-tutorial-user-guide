'''
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
'''
from fastapi import APIRouter,Query

# pylint: disable=invalid-name

router = APIRouter()

@router.get("/items-with-query-params-str-validation/")
async def read_items_with_query_params_str_validation(q: str | None = None):
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

@router.get("/items-with-query-params-str-max-length-validation/")
async def read_items_with_query_params_str_max_length_validation(q: str | None = Query(default=None, max_length=50)):
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

@router.get("/items-with-query-params-str-max-min-length-validation/")
async def read_items_with_query_params_str_max_mix_length_validation(
    q: str | None = Query(default=None, min_length=3, max_length=50)
    ):
    '''
    <h3>Basic explanation:</h3>\n
    Add more validations: You can also add a parameter 'min_length'.\n
    If 'q' query lengh param < 3 or > 50, FastAPI will return an query params error.\n
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

@router.get("/items-with-query-params-str-max-min-length-and-regex-validation/")
async def read_items_with_query_params_str_max_mix_length_and_regex_expression_validation(
    q: str | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")
    ):
    '''
    <h3>Basic explanation:</h3>\n
    You can define a regular expression that the parameter should match. If 'q' query != "fixedquery"
     FastAPI will return an query params error.\n
    Eg.: {"detail":[{"loc":["query","q"],"msg":"string does not match regex \"^fixedquery$\"",\n
     "type":"value_error.str.regex","ctx":{"pattern":"^fixedquery$"}}]}\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "fixedquery"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-with-query-params-default-value/")
async def read_items_with_default_query_params_value(q: str = Query(default="defaultquery", min_length=3)):
    '''
    <h3>Basic explanation:</h3>\n
    You can pass None as the value for the default parameter, you can pass other values.\n
    Let's say that you want to declare the q query parameter to have a min_length of 3, and to have a default
     value of "defaultquery".\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "defaultquery"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-with-query-params-required-value/")
async def read_items_with_required_query_value(q: str = Query(min_length=3)):
    '''
    <h3>Basic explanation:</h3>\n
    When we don't need to declare more validations or metadata, we can make the q query parameter
     required just by not declaring a default value.\n
     If 'q' query is null or "", FastAPI will return an query params error.\n
    Eg.: {"detail":[{"loc":["query","q"],"msg":"field required","type":"value_error.missing"}]}\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
