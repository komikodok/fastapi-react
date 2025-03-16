from fastapi import Depends
from google.cloud.exceptions import NotFound
from google.cloud import firestore
from typing import List, Dict
from client.db_client import get_db
from .base import BaseRepository

class UserRepository(BaseRepository):
    
    def __init__(self, db: firestore.Client = Depends(get_db)):
        self.__collection = db.collection("users")

    def index(self, filter: dict | None = None) -> List[Dict[str, any]]:
        docs_ref = self.__collection
        if filter:
            for key, value in filter.items():
                docs_ref = docs_ref.where(key, "==", value)
        docs = docs_ref.get()
        return docs

    def show(self, id: str) -> Dict[str, any]:
        doc_ref = self.__collection.document(id)
        doc = doc_ref.get()
        if not doc.exists:
            raise NotFound(f"User with id {id} is not found")
        return doc
    
    def store(self, data: dict | None = None, **kwargs):
        data = data or kwargs
        doc_ref = self.__collection.document()
        doc_ref.set(data)
        doc = doc_ref.get()
        return doc
    
    def update(self, id: str, **kwargs):
        doc_ref = self.__collection.document(id)
        if doc_ref.exists:
            doc_ref.update(**kwargs)
        doc = doc_ref.get()
        return doc
    
    def delete(self, id: str):
        doc = self.__collection.document(id)
        return doc.delete()
