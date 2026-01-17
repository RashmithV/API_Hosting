import os
from fastapi import FastAPI
from pydantic import BaseModel
from cerebras.cloud.sdk import Cerebras
from dotenv import load_dotenv

load_dotenv()
CEREBRAS_MODEL = "gpt-oss-120b"
api_key = os.getenv("CEREBRAS_API_KEY")
client = Cerebras(api_key=api_key)

app = FastAPI(title="Cerebras Chatbot API")

class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


def query_cerebras(prompt: str) -> str:
    stream = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        model=CEREBRAS_MODEL,
        stream=True,
        max_completion_tokens=1024,
        temperature=0.7,
        top_p=0.8
    )
    output = ""
    for chunk in stream:
        output += chunk.choices[0].delta.content or ""
    return output


@app.get("/test app for API")
def health():
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = query_cerebras(req.prompt)
    return {"response": reply}