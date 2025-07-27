# src/services/maps_service.py
import os
import requests

def get_fastest_route(origin: str, destination: str):
    """Fetches the fastest route from Google Maps Directions API."""
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    if not api_key:
        raise Exception("GOOGLE_MAPS_API_KEY is not set in environment.")

    url = "https://maps.googleapis.com/maps/api/directions/json"
    params = {
        'origin': origin,
        'destination': destination,
        'key': api_key,
        'departure_time': 'now',
        'traffic_model': 'best_guess'
    }

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raises an exception for bad status codes (4xx or 5xx)

    data = response.json()
    if data['status'] != 'OK':
        error_message = data.get('error_message', 'Failed to get route from Google Maps')
        raise Exception(error_message)

    print("Successfully retrieved route from Google Maps.")
    return data['routes'][0] # Return the first and typically fastest route