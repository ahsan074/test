from tools.weather_api import fetch_weather
from tools.wikipedia_tool import summarize_topic
from system_prompt import SYSTEM_PROMPT

def handle_prompt(prompt: str):
    prompt_lower = prompt.lower().strip()

    try:
        # Handle empty input
        if not prompt_lower:
            raise ValueError("Empty prompt")

        # Handle weather queries
        if "weather" in prompt_lower:
            if "in" in prompt_lower:
                location = prompt_lower.split("in")[-1].strip(" ?.")
                if location:
                    result = fetch_weather(location)
                    return {
                        "response": f"{SYSTEM_PROMPT}\n{result}",
                        "tool_used": "Weather API"
                    }
            raise ValueError("Missing location for weather")

        # Handle Wikipedia-style prompts
        elif "tell me about" in prompt_lower:
            topic = prompt_lower.split("about")[-1].strip(" ?.")
            if topic:
                result = summarize_topic(topic)
                return {
                    "response": f"{SYSTEM_PROMPT}\n{result}",
                    "tool_used": "Wikipedia Tool"
                }
            raise ValueError("Missing topic for Wikipedia tool")

        # Fallback for unknown prompts
        return {
            "response": f"{SYSTEM_PROMPT}\nI'm not sure how to help with that.",
            "tool_used": "Fallback"
        }

    except Exception:
        return {
            "response": f"{SYSTEM_PROMPT}\nI couldn't process your request.",
            "tool_used": "Error Handler"
        }
