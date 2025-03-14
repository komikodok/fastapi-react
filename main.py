from fastapi import FastAPI, Depends, status, Path
from models.user import User
from models.response import Response
from repository.user_repository import UserRepository
from serializer.user_serializer import UserSerializer
from exception_handler import exception_handler


app = FastAPI(
    openapi_prefix="/api/v1",
    title="Rest API with Firebase Firestore.",
    description="Integrate fastapi with cloud firestore."
)

@app.get("/users", response_model=Response, summary="get users data")
def get_all_user(user_repository: UserRepository = Depends()):
    try:
        docs = user_repository().index()
        data = UserSerializer(docs).data
    except Exception as e:
        exception_handler(e)

    return Response(
        status_code=status.HTTP_200_OK,
        message="Fetched users data is successfully.",
        data=data
    )
    
@app.get("/users/{user_id}", response_model=Response, summary="get user data by id")
def get_user_by_id(
    user_id: str = Path(),
    user_repository: UserRepository = Depends()
):
    try:
        pass
    except Exception as e:
        exception_handler(e)

@app.post("/users", response_model=Response, summary="create new user")
def create_user(
    user: User,
    user_repository: UserRepository = Depends(),
):
    try:
        doc = user_repository().store(user)
        created_data = UserSerializer(doc).data
    except Exception as e:
        exception_handler(e)

    return Response(
        status_code=status.HTTP_201_CREATED,
        message="Created user data is successfully"
    )
