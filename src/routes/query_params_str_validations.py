'''
https://fastapi.tiangolo.com/tutorial/query-params-str-validations/
'''
from fastapi import APIRouter,Query
from pydantic import Required

# pylint: disable=invalid-name
# pylint: disable=line-too-long

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

@router.get("/items-with-query-params-required-value-with-ellipsis/")
async def read_items_with_required_query_value_with_ellipsis(q: str = Query(default=..., min_length=3)):
    '''
    <h3>Basic explanation:</h3>\n
    There's an alternative way to explicitly declare that a value is required.
     You can set the default parameter to the literal value '...'\n
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

@router.get("/items-with-query-params-required-value-with-none/")
async def read_items_with_required_query_value_with_none(q: str | None = Query(default=..., min_length=3)):
    '''
    <h3>Basic explanation:</h3>\n
    You can declare that a parameter can accept None, but that it's still required.
     This would force clients to send a value, even if the value is None.\n
    To do that, you can declare that None is a valid type but still use default=... .\n
    If 'q' query is null or "", FastAPI will return an query params error:\n
    Eg.: {"detail":[{"loc":["query","q"],"msg":"field required","type":"value_error.missing"}]}\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"},{"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-with-query-params-required-value-with-pydantic/")
async def read_items_with_required_query_value_with_pydantic(q: str = Query(default=Required, min_length=3)):
    '''
    <h3>Basic explanation:</h3>\n
    If you feel uncomfortable using ..., you can also import and use Required from Pydantic.
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

@router.get("/items-query-params-with-multiple-values/")
async def read_items_query_value_with_multiple_values(q: list[str] | None = Query(default=None)):
    '''
    <h3>Basic explanation:</h3>\n
    When you define a query parameter explicitly with Query you can also declare it to receive a list of values,
     or said in other way, to receive multiple values.\n
    Then, with a URL like:\n
    http://localhost:8000/items/?q=foo&q=bar\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values-with-defaults"
     target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": ["q": ["foo", "bar"]}
    '''
    query_items = {"q": q}
    return query_items

@router.get("/items-query-params-with-multiple-default-values/")
async def read_items_query_value_with_multiple_default_values(q: list[str] = Query(default=["foo", "bar"])):
    '''
    <h3>Basic explanation:</h3>\n
    And you can also define a default list of values if none are provided.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#query-parameter-list-multiple-values-with-defaults"
     target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": ["q": ["foo", "bar"]}
    '''
    query_items = {"q": q}
    return query_items


@router.get("/items-with-query-params-required-value-with-information-metadata-params/")
async def read_items_with_required_query_value_with_information_metadata_params(
    q: str | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        )):
    '''
    <h3>Basic explanation:</h3>\n
    You can add more information about the parameter.\n
    That information will be included in the generated OpenAPI and used by the documentation user
     interfaces and external tools.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#declare-more-metadata"
     target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-with-alias-query-params/")
async def read_items_with_alias_query_params(q: str | None = Query(default=None, alias="item-query")):
    '''
    <h3>Basic explanation:</h3>\n
    Imagine that you want the parameter to be item-query. Like in:\n
    http://127.0.0.1:8000/items/?item-query=foobaritems\n
    But item-query is not a valid Python variable name. The closest would be item_query. But you still need it to be exactly item-query...\n
    Then you can declare an alias, and that alias is what will be used to find the parameter value.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#alias-parameters" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}],"q": "Test"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-with-deprecating-query-params/")
async def read_items_with_deprecating_query_params(
    q: str | None = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,
    )):
    '''
    <h3>Basic explanation:</h3>\n
    Imagine that you want the parameter to be item-query. Like in:\n
    http://127.0.0.1:8000/items/?item-query=foobaritems\n
    But item-query is not a valid Python variable name. The closest would be item_query. But you still need it to be exactly item-query...\n
    Then you can declare an alias, and that alias is what will be used to find the parameter value.\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#deprecating-parameters" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}],"q": "fixedquery"}
    '''
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@router.get("/items-with-query-params-excluded-from-open-api/")
async def read_items_with_query_params_excluded_from_open_api(hidden_query: str | None = Query(default=None, include_in_schema=False)):
    '''
    <h3>Basic explanation:</h3>\n
    To exclude a query parameter from the generated OpenAPI schema (and thus, from the automatic documentation systems),
     set the parameter include_in_schema of Query to False:\n
    <a href="https://fastapi.tiangolo.com/tutorial/query-params-str-validations/#exclude-from-openapi" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    {"hidden_query":"Not found"} or {"hidden_query":"Test"}
    '''
    if hidden_query:
        response = {"hidden_query": hidden_query}
    else:
        response = {"hidden_query": "Not found"}

    return response
