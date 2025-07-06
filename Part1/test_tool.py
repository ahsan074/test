from tools.weather_api import fetch_weather
from tools.wikipedia_tool import summarize_topic
import pytest

def test_weather_api():
    assert "weather" in fetch_weather("Berlin").lower()

def test_wikipedia_tool():
    assert "summary" in summarize_topic("Quantum Physics").lower()

def test_weather_missing_location():
    with pytest.raises(ValueError):
        fetch_weather("")
