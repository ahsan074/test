import random

def fetch_weather(location: str) -> str:
    if not location:
        raise ValueError("Missing location")
    # Simulated weather info
    return f"The weather in {location} is {random.choice(['sunny', 'cloudy', 'rainy'])}."
