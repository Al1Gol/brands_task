from fastapi import FastAPI
from mainapp.router import router
from fastapi.logger import logger

import os
import logging

app = FastAPI()

app.include_router(router)


gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers
if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)