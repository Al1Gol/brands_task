from fastapi import FastAPI
from mainapp.router import router
import os

app = FastAPI()

app.include_router(router)
