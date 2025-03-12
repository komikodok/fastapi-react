import firebase_admin
from firebase_admin import firestore, credentials
import os
from dotenv import load_dotenv, find_dotenv
from glob import glob


load_dotenv(find_dotenv())

path_service_key = os.getenv("PATH_SERVICE_KEY")
cred = credentials.Certificate(glob(path_service_key, recursive=True))
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_db():
    return db