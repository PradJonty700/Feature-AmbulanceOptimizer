# src/services/signal_service.py

def _extract_junctions_from_route(route_data: dict) -> list:
    """
    A mock function to extract junction coordinates or IDs from route steps.
    In a real system, this would parse the polyline or steps for specific GPS coordinates.
    """
    junctions = []
    # The route object contains legs, and legs contain steps.
    try:
        steps = route_data['legs'][0]['steps']
        for i, step in enumerate(steps):
            # Let's assume every second step is a major junction for this mock-up
            if i % 2 == 0:
                location = step['start_location']
                junctions.append(f"Junction at {location['lat']},{location['lng']}")
    except (KeyError, IndexError):
        # Fallback if route structure is unexpected
        return ["Mock_Junction_A", "Mock_Junction_B", "Mock_Junction_C"]
    
    return junctions

def notify_junctions(route_data: dict):
    """
    Simulates notifying all relevant traffic signals along a given route.
    """
    junctions_to_clear = _extract_junctions_from_route(route_data)
    
    print("\n--- NOTIFYING TRAFFIC SIGNALS ---")
    for junction in junctions_to_clear:
        # In a real-world scenario, this would be an API call (HTTP POST)
        # to a smart traffic management system's endpoint.
        # e.g., requests.post(f"https://api.traffic-system.com/clear_path", json={"junctionId": junction})
        print(f"[!] Sending 'clear path' command to: {junction}")
    print("--- NOTIFICATION COMPLETE ---\n")