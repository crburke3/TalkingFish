import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import uuid
from datetime import datetime
from structs.bubbles import Bubbles
from structs import server_globals
from structs.fish_information import FishInformation

# Use the application default credentials


class FishFirestore:

    def __init__(self):
        print("initalizing firestore client...")
        cred = credentials.Certificate(server_globals.gcs_cred_path)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        print("finished created firestore client!")
    
    def get_request_from_queue(self, device_id: str):
        collection_name = f"{device_id}_queue"
        print("checking queue for collection: ", collection_name)
        doc_ref = self.db.collection(collection_name)
        query = doc_ref.order_by("queue_count").limit(1)
        try:
            results = query.get()[0].to_dict()
            print("Successfully received object from queue: ", results)
            return results
        except IndexError:
            return 404

    def add_request_to_queue(self, message: str, commands: str, audio_url :str, device_id: str):
        # prepare post object
        new_request = Bubbles()
        new_request.queue_count = datetime.utcnow().timestamp()
        new_request.speech_text = message
        new_request.commands = commands
        new_request.audio_url = audio_url
        request_json = new_request.dict()

        # send object to database
        document_name = str(uuid.uuid4())
        doc_ref = self.db.collection(f"{device_id}_queue").document(document_name)
        doc_ref.set(request_json)
        print(f"Successfully posted object to queue for device: {device_id}: {request_json}")
    
    def delete_request_from_queue(self, queue_count: float, device_id: str):
        doc_ref = self.db.collection(f"{device_id}_queue")
        id = doc_ref.where(u'queue_count', u'==', queue_count).get()[0].id
        doc_ref.document(id).delete()
        print("Successfully deleted object from queue with id: ", id)

    def set_fish_information(self, fish_info: dict):
        assert fish_info is not None
        device_id = fish_info.get("device_id", f"UNKNOWN_FISH:{str(uuid.uuid4())}")
        doc_ref = self.db.collection(f"fish_information").document(device_id)
        doc_ref.set(fish_info)
        print(f"successfully upload fish data: {fish_info}")

    def get_name_to_device_id_dict(self) -> dict:
        # config = self.db.collection("globals").document("server_config").get().to_dict()
        # server_name_to_device_id = config.get("name_to_device_id", server_globals.NAME_TO_DEVICE_ID_DEFAULT)

        return server_globals.NAME_TO_DEVICE_ID_DEFAULT

    def get_fish_information(self, device_id: str) -> FishInformation:
        try:
            info = self.db.collection("fish_information").document(device_id).get().to_dict()
            return FishInformation(**info)
        except:
            return FishInformation()
