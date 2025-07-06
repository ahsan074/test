from fastapi import FastAPI
from pydantic import BaseModel
from agent import handle_prompt

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

class AgentResponse(BaseModel):
    response: str
    tool_used: str

@app.post("/agent", response_model=AgentResponse)
async def agent_endpoint(request: PromptRequest):
    return handle_prompt(request.prompt)
