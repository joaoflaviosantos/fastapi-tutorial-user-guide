'''Instancing the FastAPI class and include routes from APIRouter instances'''
from fastapi import FastAPI

# pylint: disable=pointless-string-statement
# pylint: disable=invalid-name
# pylint: disable=import-error

from routes.first_steps import router as first_steps
from routes.path_params import router as path_params
from routes.query_params import router as query_params
from routes.body import router as body
from routes.query_params_str_validations import router as query_params_str_validations

app = FastAPI(title="FastAPI Official Tutorial - User Guide")

app.include_router(first_steps, prefix="", tags=["first-steps"])
app.include_router(path_params, prefix="", tags=["path-params"])
app.include_router(query_params, prefix="", tags=["query-params"])
app.include_router(body, prefix="", tags=["body"])
app.include_router(query_params_str_validations, prefix="", tags=["query-params-str-validations"])
