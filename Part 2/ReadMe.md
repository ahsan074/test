# Part 2 – Dockerization and Deployment of FastAPI Agent

This part focuses on containerizing your FastAPI-based intelligent agent and preparing it for deployment using Docker. The agent supports weather queries and Wikipedia-style topic summaries.

---

## 🚀 Project Structure

part1/
│
├── agent.py
├── main.py
├── system_prompt.py
├── tools/
│ ├── init.py
│ ├── weather_api.py
│ └── wikipedia_tool.py
├── requirements.txt
├── Dockerfile
├── .env
└── README.md

part2/
│
├── readme.md
├── dockerfile


part3/
│
├── answers.md

---

## 🐳 Docker Instructions

### 1. ✅ Build the Docker Image

From the project root:

docker build -t agent-service .
docker run -p 8000:8000 agent-service

Once running, your API will be available at:

http://localhost:8000

Endpoint: POST /agent

curl -X POST http://127.0.0.1:8000/agent \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"What is the weather in Lahore?\"}"

 🌐 Deployment
 Railway

Sign in to Railway: https://railway.app/

New Project → Deploy from GitHub Repo

Set Environment Variable:

OPENWEATHER_API_KEY

WIKI_API_LANG (optional, default: en)

Railway auto-builds your Docker container.

Once deployed, test via public URL:
curl -X POST https://your-app-name.up.railway.app/agent \
  -H "Content-Type: application/json" \
  -d "{\"prompt\": \"Tell me about Albert Einstein\"}"


🧾 requirements.txt
  	fastapi
	uvicorn
	requests
	pydantic
	python-dotenv

🔐 Environment Variables
OPENWEATHER_API_KEY=your_openweather_api_key
WIKI_API_LANG=en

✅ Output Example
{
  "response": "You are a helpful assistant...\nThe weather in Lahore is 34°C with clear skies.",
  "tool_used": "Weather API"
}
