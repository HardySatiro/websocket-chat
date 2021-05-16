from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from v1.duplex import duplex_router

app = FastAPI()

app.mount('/static',StaticFiles(directory='static'), name='static')

app.include_router(duplex_router)