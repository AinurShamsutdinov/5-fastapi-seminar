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
    id: str = None
    title: str = None
    description: str = None
    status: str = None


@app.get('/tasks')
async def read_root():
    logger.info('GET request.')
    return tasks


@app.post('/tasks')
async def create_item(task: Task):
    logger.info('POST request.')
    task_id = len(tasks)
    task.id = task_id
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
async def update_item(task_id: int, task_update: Task):
    logger.info(f'Put task with item ID = {task_id}.')
    for task in tasks:
        if task.id == task_id:
            task.title = task_update.title
            task.description = task_update.description
            task.status = task_update.status
            return task
    return list()


@app.delete('/tasks/{task_id}')
async def delete_item(task_id: int):
    logger.info(f'DELETE task with ID = {task_id}.')
    if len(tasks) > 0:
        tasks.pop(task_id)
        return {'task_id': task_id}
    message = f'does not exist task with ID = {task_id}'
    return JSONResponse(content=message, status_code=404)