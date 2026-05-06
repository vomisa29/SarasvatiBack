import firebase_admin
from firebase_admin import credentials, db



class firebaseDB:
    def __init__(self,credential_path,database_url):
        # Initialize Firebase with service account credentials
        cred = credentials.Certificate(credential_path)
        firebase_admin.initialize_app(cred, {
           "databaseURL": database_url 
        })

    
    def create_record(self, path, data):
        ref = db.reference(path)
        ref = ref.push()
        ref.set(data)
        
        return ref.key
        
    def read_record(self, path):
        ref = db.reference(path)
        return ref.get()
    
    def update_record(self, path, data):
        ref = db.reference(path)
        ref.update(data)
        
    def delete_record(self,path):
        ref = db.reference(path)
        ref.delete()