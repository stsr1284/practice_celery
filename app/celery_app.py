import os
from celery import Celery

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL,  # 결과 저장소도 redis로 설정
)

celery_app.conf.update(
    result_expires=3600,  # 결과 만료 시간 (초)
    task_serializer="json",  # 직렬화 형식
    accept_content=["json"],  # 수용할 직렬화 형식
    result_serializer="json",  # 결과 직렬화 형식
    timezone="Asia/Seoul",  # 타임존 설정
    enable_utc=True,  # UTC 사용 여부
)

# celery가 자동으로 태스크를 발견하도록 설정
celery_app.autodiscover_tasks(["app"])
