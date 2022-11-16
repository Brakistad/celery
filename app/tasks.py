from celery import Celery

app = Celery('tasks', broker='pyamqp://admin:mypass@rabbitmq//')

@app.task
def add(x: int, y: int) -> int:
    return x + y
