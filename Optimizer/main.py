import functioms()
import requests
import os

@functions_framework.http
def get_ambulance_route(request):
    request_json = request.get_json(silent=True)
    
    origin = f"{request_json['current_location']['lat']},{request_json['current_location']['lng']}"
    destination = f"{request_json['destination']['lat']},{request_json['destination']['lng']}"
    
    api_key = os.environ.get("MAPS_API_KEY")

    url = f"https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': origin,
        'destination': destination,
        'key': api_key,
        'traffic_model': 'best_guess',
        'departure_time': 'now'
    }

    response = requests.get(url, params=params)
    data = response.json()

    steps = data['routes'][0]['legs'][0]['steps']
    route_points = [step['end_location'] for step in steps]

    return {
        "route": route_points,
        "eta": data['routes'][0]['legs'][0]['duration_in_traffic']['text']
    }
