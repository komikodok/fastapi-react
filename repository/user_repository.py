from client.db_client import get_db
from typing import List, Dict
from .base import BaseRepository

class UserRepository(BaseRepository):
    
    def __init__(self, db=get_db):
        self.__collection = db.collection("users")

    def index(self, filter: dict | None = None) -> List[Dict[str, any]]:
        docs = self.__collection
        if filter:
            for key, value in filter.items():
                docs = docs.where(key, "==", value)
        return docs.get()

    def show(self, id: str) -> Dict[str, any]:
        doc = self.__collection.document(id)
        return doc.get()
    
    def store(self, data: dict | None = None, **kwargs):
        data = data or kwargs
        doc, _ = self.__collection.add(data)
        return doc.get()
    
    def update(self, id: str, **kwargs):
        doc = self.__collection.document(id)
        doc = doc.update(**kwargs)
        return doc.get()
    
    def delete(self, id: str):
        doc = self.__collection.document(id)
        return doc.delete()
