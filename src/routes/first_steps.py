'''
Exemples on: https://fastapi.tiangolo.com/tutorial/first-steps/
'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    '''
    <h3>Basic explanation:</h3>\n
    Open your browser at root route. Eg.: http://127.0.0.1:8000.\n
    <a href="https://fastapi.tiangolo.com/tutorial/first-steps/" target="_blank">More details..</a>
    <h3>Response exemple:</h3>\n
    { "message": "Hello World" }
    '''
    return {"message": "Hello World"}
