import logging
from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from typing import Annotated

app = FastAPI()
templates = Jinja2Templates(directory='./templates')


users: list = list()


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class User(BaseModel):
    id: str = None
    name: str = None
    email: str = None
    password: str = None


# 3rd exercise
@app.post('/user/')
async def create_user(user: User):
    users.append(user)
    message = f'User created {user.name}'
    logger.info(f'Amount of users in a base {len(users)}')
    return JSONResponse(content=message, status_code=200)


# 4th exercise
@app.put('/user/')
async def update_user(us_up: User):
    for user in users:
        if user.id == us_up.id:
            if us_up.name is not None:
                user.name = us_up.name
            if us_up.email is not None:
                user.email = us_up.email
            if us_up.password is not None:
                user.password = us_up.password
            return user
    message = f'User with ID = {us_up.id}, does not exist'
    return JSONResponse(content=message, status_code=404)


# 5th exercise
@app.delete('/user/{email}')
async def delete_user(email: str):
    for user in users:
        if user.email == email:
            users.remove(user)
            message = f'User with Email = {email} deleted'
            return JSONResponse(content=message, status_code=200)
    message = f'User with Email = {email}, does not exist'
    return JSONResponse(content=message, status_code=404)


# 6th exercise
@app.get('/users/', response_class=HTMLResponse)
async def get_users(request: Request):
    context = dict()
    context['request'] = request
    context['users'] = users
    return templates.TemplateResponse('index.html', context)


@app.post('/usercreate/')
async def create_user(user_id: Annotated[str, Form()],
                      user_name: Annotated[str, Form()],
                      user_email: Annotated[str, Form()],
                      user_password: Annotated[str, Form()],
                      request: Request):
    users.append(User(id=user_id, name=user_name, email=user_email, password=user_password))
    redirect_url = request.url_for('get_users')
    return RedirectResponse(redirect_url, status_code=303)
