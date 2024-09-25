import pyrebase
import os
from dotenv import load_dotenv
load_dotenv()
firebase_config = {
    "apiKey":os.getenv('FIREBASE_API_KEY'),
    "authDomain": "",
    "databaseURL": os.getenv('FIREBASE_DATABSE_URL'),
    "projectId": "",
    "storageBucket": "",
}
firebase = pyrebase.initialize_app(firebase_config)
Auth = firebase.auth()
db = firebase.database()
st= firebase.storage()
