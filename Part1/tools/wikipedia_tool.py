def summarize_topic(topic: str) -> str:
    if not topic:
        raise ValueError("Missing topic")
    return f"{topic} is a widely discussed topic. Here's a short summary from Wikipedia."
