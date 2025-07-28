# src/controllers/ambulance_controller.py

from flask import request, jsonify, Blueprint
from ..services import maps_service, firestore_service, signal_service
import traceback # <--- IMPORT THIS MODULE

ambulance_bp = Blueprint('ambulance', __name__, url_prefix='/api')

@ambulance_bp.route('/ambulance-route', methods=['POST'])
def handle_ambulance_route():
    # ... (the start of the function is the same)
    data = request.get_json()
    ambulance_id = data.get('ambulanceId')
    current_location = data.get('currentLocation')
    destination = data.get('destination')

    if not all([ambulance_id, current_location, destination]):
        return jsonify({"error": "Missing required fields"}), 400

    try:
        # ... (the main logic is the same)
        route_data = maps_service.get_fastest_route(current_location, destination)
        firestore_service.save_ambulance_route(ambulance_id, current_location, destination, route_data)
        signal_service.notify_junctions(route_data)

        return jsonify({
            "status": "success",
            "message": "Route processed and dispatched successfully.",
            "routeData": route_data
        }), 200

    except Exception as e:
        # --- THIS IS THE MODIFIED PART ---
        print("--- AN ERROR OCCURRED ---")
        traceback.print_exc() # This will print the full, detailed error traceback to your terminal.
        print("-------------------------")
        return jsonify({"error": f"An internal error occurred: {str(e)}"}), 500