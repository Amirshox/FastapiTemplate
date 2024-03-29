from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from src.core.schemas import (UserCreateResponse, UserDeleteResponse,
                              UserEditResponse, UserGetResponse, UserSchemaAdd,
                              UserSchemaEdit, UsersGetResponse)
from src.core.services import UsersService
from src.core.unitofwork import IUnitOfWork
from src.dependencies import get_uow

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/get_all/", response_model=UsersGetResponse)
async def get_users(uow: Annotated[IUnitOfWork, Depends(get_uow)]):
    response = await UsersService().get_users(uow)
    return UsersGetResponse(users=response)


@router.get("/get/", response_model=UserGetResponse)
async def get_user(id: int, uow: Annotated[IUnitOfWork, Depends(get_uow)]):
    response = await UsersService().get_user(id, uow)
    if response is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return UserGetResponse(user=response)


@router.post("/create/", response_model=UserCreateResponse)
async def create_user(
    user: UserSchemaAdd, uow: Annotated[IUnitOfWork, Depends(get_uow)]
):
    response = await UsersService().add_user(uow, user)
    if response is False:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="username already exists"
        )
    return UserCreateResponse(user_id=response)


@router.delete("/delete/", response_model=UserDeleteResponse)
async def delete_user(id: int, uow: Annotated[IUnitOfWork, Depends(get_uow)]):
    response = await UsersService().delete_user(id, uow)
    if response is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return UserDeleteResponse(status=response)


@router.put("/edit/", response_model=UserEditResponse)
async def edit_user(
    id: int, user: UserSchemaEdit, uow: Annotated[IUnitOfWork, Depends(get_uow)]
):
    response = await UsersService().edit_user(id, user, uow)
    if response is False:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    return UserEditResponse(user_id=response)
