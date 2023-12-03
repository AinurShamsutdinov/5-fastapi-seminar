import logging
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()


users: list = list()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str


@app.post('/user/')
async def create_user(user: User):
    users.append(user)
    message = f'User created {user.name}'
    logger.info(f'Amount of users in a base {len(users)}')
    return JSONResponse(content=message, status_code=200)
