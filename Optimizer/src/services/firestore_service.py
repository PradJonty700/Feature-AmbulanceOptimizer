# src/services/firestore_service.py
import firebase_admin
from firebase_admin import credentials, firestore


try:
    if not firebase_admin._apps:
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    print("Firestore service initialized successfully.")
except Exception as e:
    print(f"Failed to initialize Firestore: {e}. Service will not work.")
    db = None

def save_ambulance_route(ambulance_id: str, current: str, destination: str, route_data: dict):
    """Saves or updates the ambulance's route information in Firestore."""
    if not db:
        raise Exception("Firestore is not initialized.")

    doc_ref = db.collection('ambulances').document(ambulance_id)
    doc_ref.set({
        'currentLocation': current,
        'destination': destination,
        'route': route_data,  # Store the entire route object
        'status': 'en_route',
        'updatedAt': firestore.SERVER_TIMESTAMP # Use server-side timestamp
    })
    print(f"Saved route for ambulance {ambulance_id} to Firestore.")