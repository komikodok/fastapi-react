import firebase_admin
from firebase_admin import firestore, credentials
import os
from dotenv import load_dotenv, find_dotenv
from glob import glob


load_dotenv(find_dotenv())

path = os.getenv("PATH_SERVICE_KEY")
service_key = glob(path, recursive=True)
cred = credentials.Certificate(service_key[0])
firebase_admin.initialize_app(cred)

db = firestore.client()

def get_db():
    return db