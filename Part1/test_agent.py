from agent import handle_prompt

def test_weather_tool():
    res = handle_prompt("What's the weather in Tokyo?")
    assert res["tool_used"] == "Weather API"

def test_wikipedia_tool():
    res = handle_prompt("Tell me about AI")
    assert res["tool_used"] == "Wikipedia Tool"

def test_fallback():
    res = handle_prompt("Dance for me")
    assert res["tool_used"] == "Fallback"
