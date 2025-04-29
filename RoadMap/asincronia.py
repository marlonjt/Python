import asyncio
import time
from datetime import datetime


"""
Funciones async son tareas a realizar para la carga de trabajo o que se ejecuten en paralelo estableciendo tiempos de espera.
"""


async def task_async(task, duration):
    now = datetime.now()
    print(f"la tarea {task}, Duración: {duration}.s, Inicio: {datetime.now()}")
    await asyncio.sleep(duration)
    print(f"la tarea {task}, Duración: {duration}.s, Finalizo: {datetime.now()}")


async def tasks():
    await asyncio.gather(
        task_async("Task C", 3), task_async("Task B", 2), task_async("Task A", 1)
    )
    await task_async("Task D", 1)


asyncio.run(tasks())
