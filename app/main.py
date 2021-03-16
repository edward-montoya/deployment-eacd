from fastapi import Depends, FastAPI

from .routers import datasets, models

app = FastAPI()

app.include_router(datasets.router)
app.include_router(models.router)
