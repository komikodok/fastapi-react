from fastapi import Depends
from client.db_client import get_db
from .base import BaseRepository


class RepositoryUser(BaseRepository):
    
    def __init__(self, db=Depends(get_db)):
        self.collection = db.collection("users")

    def index(self, *args, **kwargs): ...

    def show(self, *args, **kwargs): ...
    
    def store(self, *args, **kwargs): ...
    
    def update(self, *args, **kwargs): ...
    
    def delete(self, *args, **kwargs): ...
