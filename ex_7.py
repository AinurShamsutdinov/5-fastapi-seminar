import logging
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


@app.get('/tasks/{task_id}')
async def get_task(task_id: str):
    logger.info(f'GET request, ID = {task_id}.')
    for task in tasks:
        if str(task.id) == task_id:
            return task
    message = f'Task does not exist with ID = {task_id}'
    return JSONResponse(message, status_code=404)


@app.get('/tasks')
async def get_tasks():
    logger.info('GET request.')
    return tasks


@app.post('/tasks')
async def create_task(task: Task):
    logger.info('POST request.')
    task_id = len(tasks)
    task.id = task_id
    tasks.append(task)
    return task


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, task_update: Task):
    logger.info(f'Put task with item ID = {task_id}.')
    for task in tasks:
        if task.id == task_id:
            task.title = task_update.title
            task.description = task_update.description
            task.status = task_update.status
            return task
    return list()


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    logger.info(f'DELETE task with ID = {task_id}.')
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            message = f'Delete task with ID = {task_id}'
            return JSONResponse(content=message, status_code=200)
    message = f'does not exist task with ID = {task_id}'
    return JSONResponse(content=message, status_code=404)
