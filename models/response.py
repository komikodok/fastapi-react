from pydantic import BaseModel
from typing import Union, List, Optional


class Response(BaseModel):
    status: str
    message: str
    error: Optional[Union[str, List[str]]] = None