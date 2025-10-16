import os
import firebase_admin
from firebase_admin import credentials, db
from dotenv import load_dotenv

def init_firebase():
    load_dotenv()

    database_url = os.getenv("FIREBASE_DATABASE_URL")
    cred_path = os.getenv("FIREBASE_CREDENTIALS_FILE")

    if not database_url:
        raise RuntimeError("Falta FIREBASE_DATABASE_URL en .env")
    if not cred_path or not os.path.exists(cred_path):
        raise RuntimeError("Falta FIREBASE_CREDENTIALS_FILE o la ruta no existe: " + str(cred_path))

    if not firebase_admin._apps:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred, {"databaseURL": database_url})
