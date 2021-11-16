import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
from datetime import datetime
from structs.bubbles import Bubbles
from structs import server_globals

# Use the application default credentials

class FishFirestore:

    def __init__(self):
        print("initalizing firestore client...")
        cred = credentials.Certificate(server_globals.gcs_cred_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        print("finished created firestore client!")

    def add_request_to_queue(self, message: str, commands: str):
        # prepare post object
        new_request = Bubbles()
        new_request.queue_count = datetime.utcnow().timestamp()
        new_request.speech_text = message
        new_request.commands = commands
        request_json = new_request.dict()

        # send object to database
        document_name = str(uuid.uuid4())
        doc_ref = self.db.collection("fish_1_queue").document(document_name)
        doc_ref.set(request_json)
        print("Successfully posted object to queue: ", request_json)
