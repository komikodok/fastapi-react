from fastapi import HTTPException, status
from firebase_admin.exceptions import (
    NotFoundError,
    FirebaseError,
    InvalidArgumentError,
    UnavailableError,
    DeadlineExceededError,
    ResourceExhaustedError
)
from google.cloud.exceptions import (
    NotFound,
    GoogleCloudError,
    BadRequest,
    ServiceUnavailable,
    TooManyRequests,
)
from pydantic import ValidationError


def exception_handler(e):
    match e:
        case FirebaseError():
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An internal Firebase occurred"
            )
        case NotFound() | NotFoundError():
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Resource not found"
            )
        case BadRequest() | ValidationError() | InvalidArgumentError():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Validation error"
            )
        case ServiceUnavailable() | UnavailableError():
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Firestore service is unavailable"
            )
        case DeadlineExceededError():
            raise HTTPException(
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
                detail="Operation timed out"
            )
        case ResourceExhaustedError() | TooManyRequests():
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Firestore quota exceeded"
            )
        case _:
            print(f"Exception: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An internal Server error occurred"
            )