# Part 1 – Intelligent Agent with FastAPI and Tool Integration

This part implements an intelligent agent using **FastAPI** with modular support for tools like **weather queries** and **Wikipedia summaries**. The project is designed to be simple, extensible, and ready for local testing.

---

## 🧠 Features

- FastAPI-based web service with `/agent` endpoint
- Tool-based modular processing:
  - 🌦️ Weather via OpenWeatherMap API
  - 📚 Topic summary via Wikipedia API
- Graceful fallback for unrecognized prompts
- Environment variable support via `.env`
- Hugging Face LLM integration option (optional)

---

## 📁 Project Structure
part1/
│
├── main.py # FastAPI app entry point
├── agent.py # Tool orchestration logic
├── system_prompt.py # System-level response template
├── tools/
│ ├── init.py
│ ├── weather_api.py # Handles weather queries
│ └── wikipedia_tool.py # Handles topic summaries
├── .env # API keys (excluded from version control)
├── requirements.txt # Python dependencies
└── README.md



---

## 🚀 Running Locally

### 1. ✅ Install Dependencies

pip install -r requirements.txt


2. ✅ Add Environment Variables
Create a .env file in the project root:

OPENWEATHER_API_KEY=your_openweather_api_key
WIKI_API_LANG=en

3. ✅ Start the Server
uvicorn main:app --reload

App will run at:
👉 http://127.0.0.1:8000

🧪 API Usage
Endpoint: POST /agent
Example CURL
curl -X POST http://127.0.0.1:8000/agent \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"What is the weather in Lahore?\"}"

  JSON Response:
  {
  "response": "You are a helpful assistant...\nThe weather in Lahore is 34°C with clear skies.",
  "tool_used": "Weather API"
}

📦 requirements.txt
fastapi
uvicorn
requests
python-dotenv
