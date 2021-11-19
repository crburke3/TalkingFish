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
    
    def get_request_from_queue(self):
        doc_ref = self.db.collection("fish_1_queue")
        query = doc_ref.order_by("queue_count").limit(1)
        try:
            results = query.get()[0].to_dict()
            print("Successfully received object from queue: ", results)
            return results
        except IndexError:
            return 404

    def add_request_to_queue(self, message: str, commands: str, audio_url :str):
        # prepare post object
        new_request = Bubbles()
        new_request.queue_count = datetime.utcnow().timestamp()
        new_request.speech_text = message
        new_request.commands = commands
        new_request.audio_url = audio_url
        request_json = new_request.dict()

        # send object to database
        document_name = str(uuid.uuid4())
        doc_ref = self.db.collection("fish_1_queue").document(document_name)
        doc_ref.set(request_json)
        print("Successfully posted object to queue: ", request_json)
    
    def delete_request_from_queue(self, queue_count: float):
        doc_ref = self.db.collection("fish_1_queue")
        id = doc_ref.where(u'queue_count', u'==', queue_count).get()[0].id
        doc_ref.document(id).delete()
        print("Successfully deleted object from queue with id: ", id)
