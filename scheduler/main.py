from threading import Thread
from bot import start as bot_start
from scheduler import start as scheduler_start

if __name__ == "__main__":
    tasks = []
    for function in (bot_start, scheduler_start):
        task = Thread(target=function)
        tasks.append(task)
        task.start()
    for run_task in tasks:
        run_task.join()
