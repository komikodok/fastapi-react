from pydantic import BaseModel
from typing import Union, List, Optional


class Response(BaseModel):
    status_code: int
    message: str
    error: Optional[Union[str, List[str]]] = None
    data: Optional[Union[dict, List[dict]]] = None