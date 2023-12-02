import logging
from typing import Optional
from fastapi.responses import JSONResponse

from fastapi import FastAPI
from pydantic import BaseModel

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


tasks = list()


class Task(BaseModel):
    id: str
    title: str = None
    description: str = None
    status: bool = None


@app.get('/tasks')
async def read_root():
    logger.info('GET request.')
    return JSONResponse(tasks)


@app.post('/task/')
async def create_item(task: Task):
    logger.info('POST request.')
    return task


@app.put('/task/{task_id}')
async def update_item(task_id: int, task: Task):
    logger.info(f'Put request with item ID = {task_id}.')
    return {'item_id': task_id, 'item': task}


@app.delete('/task/{task_id}')
async def delete_item(task_id: int):
    logger.info(f'DELETE request with item ID = {task_id}.')
    return {'item_id': task_id}
