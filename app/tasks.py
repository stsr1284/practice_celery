from app.celery_app import celery_app
import time


@celery_app.task()
def long_running_task(parm: int) -> str:
    print("Task started...")
    time.sleep(10)  # Simulate a long-running task
    print("Task completed!")
    return "Task result: {}".format(parm)
