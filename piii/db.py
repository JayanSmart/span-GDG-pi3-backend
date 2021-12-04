from firebase_admin import credentials, firestore, initialize_app

CRED_CERTIFICATE_PATH = "piii/secrets/piii-74022-backend-user.json"

# Initialize Firestore DB


def create_connection():
    cred = credentials.Certificate(CRED_CERTIFICATE_PATH)
    default_app = initialize_app(cred)
    db = firestore.client()
    return db

def get_collection(db, collection_name):
    return db.collection(collection_name)