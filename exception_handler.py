from fastapi import HTTPException, status
from firebase_admin.exceptions import (
    FirebaseError,
    NotFoundError,
    InvalidArgumentError,
    UnavailableError,
    DeadlineExceededError,
    ResourceExhaustedError
)
from google.cloud.exceptions import NotFound
from pydantic import ValidationError


def exception_handler(exc):
    match exc:
        case FirebaseError():
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An internal Firebase error occurred"
            )
        case NotFoundError() | NotFound():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource not found"
            )
        case InvalidArgumentError() | ValidationError():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Validation error"
            )
        case UnavailableError():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Firestore service is unavailable"
            )
        case DeadlineExceededError():
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Operation timed out"
            )
        case ResourceExhaustedError():
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Firestore quota exceeded"
            )
        case _:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An internal Server error occurred"
            )