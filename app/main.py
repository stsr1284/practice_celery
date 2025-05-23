from fastapi import FastAPI
from app.celery_app import celery_app

app = FastAPI()

# redis 실행
# docker run --rm --name some-redis -p 6379:6379 redis:latest

# celery 실행
# uv run Celery -A app.celery_app.celery_app worker --loglevel=info

# fastAPI 실행
# uv run uvicorn app.main:app --host 0.0.0.0


@app.get("/start-task")
async def start_long_task(parm: int):
    task_result = celery_app.send_task("app.tasks.long_running_task", args=[parm])
    # task_result = long_running_task.delay(parm)

    return {"task_id": task_result.id}


@app.get("/task-status/{task_id}")
async def get_task_status(task_id: str):

    task_result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_result.id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None,
    }
