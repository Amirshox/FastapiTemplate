import os

import dotenv
from fastapi import FastAPI

from src.api import root_router
from src.core import settings
from src.dependencies import init_dependencies


def init_routers(app: FastAPI):
    app.include_router(root_router)


def create_app():
    app = FastAPI(title=settings.app_title, version=settings.version)
    init_routers(app)
    init_dependencies(app)
    return app
