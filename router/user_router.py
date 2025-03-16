from fastapi import (
    APIRouter,
    Depends, 
    status, 
    Path
)
from models.user import User
from models.response import Response
from repository.user_repository import UserRepository
from serializer.user_serializer import UserSerializer
from exception_handler import exception_handler


user_router = APIRouter(prefix="/api")

@user_router.get("/users", summary="get users data")
def get_all_user(user_repository: UserRepository = Depends()):
    try:
        docs = user_repository.index()
        data = UserSerializer(docs).data
    except Exception as e:
        exception_handler(e)

    return Response(
        status_code=status.HTTP_200_OK,
        message="Fetched users data is successfully",
        data=data
    )
    
@user_router.get("/users/{user_id}", response_model=Response, summary="get user data by id")
def get_user_by_id(
    user_id: str = Path(),
    user_repository: UserRepository = Depends(),
):
    try:
        doc = user_repository.show(user_id)
        data = UserSerializer(doc).data
    except Exception as e:
        exception_handler(e)
    
    return Response(
        status_code=status.HTTP_200_OK,
        message="Successfully fetched an user data",
        data=data
    )

@user_router.post("/users", response_model=Response, summary="create new user")
def create_user(
    user: User,
    user_repository: UserRepository = Depends(),
):
    try:
        doc = user_repository.store(user.dict())
        created_data = UserSerializer(doc).data
    except Exception as e:
        exception_handler(e)

    return Response(
        status_code=status.HTTP_201_CREATED,
        message="User data recorded successfully",
        data=created_data
    )

@user_router.put("/users/{user_id}", response_model=Response, summary="update user")
def update_user(
    user_id: str = Path(),
    user_repository: UserRepository = Depends(),
):
    try:
        doc = user_repository.update(user_id)
        updated_data = UserSerializer(doc).data
    except Exception as e:
        exception_handler(e)

    return Response(
        status_code=status.HTTP_200_OK,
        message="User data updated successfully",
        data=updated_data
    )

@user_router.delete("/users/{user_id}", response_model=Response, summary="delete user")
def delete_user(
    user_id: str = Path(),
    user_repository: UserRepository = Depends(),
):
    try:
        user_repository.delete(user_id)
    except Exception as e:
        exception_handler(e)

    return Response(
        status_code=status.HTTP_200_OK,
        message="User data deleted successfully",
    )