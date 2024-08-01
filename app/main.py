from fastapi import FastAPI
from app.routes.chat import chat_router
from app.dependencies import get_ollama_model_factory

app = FastAPI()

@app.on_event("startup")
def on_startup():
    get_ollama_model_factory()

app.include_router(chat_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
