from fastapi import FastAPI

from src.core.unitofwork import UOW, IUnitOfWork
from src.db import async_session_maker


def get_uow():
    return UOW(async_session_maker)


def init_dependencies(app: FastAPI):
    ...
