from pydantic import BaseModel
from typing import Union, List, Optional


class Response(BaseModel):
    status_code: int
    message: str
    data: Optional[Union[dict, List[dict]]] = None