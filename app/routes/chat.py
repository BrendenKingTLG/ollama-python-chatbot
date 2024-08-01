from fastapi import APIRouter, HTTPException, Depends
from app.dependencies import get_ollama_model_factory  # Import the dependency function
from app.ollama_model_factory import OllamaModelFactory
from app.models import ChatRequest, ChatResponse

chat_router = APIRouter()

@chat_router.post("/chat", response_model=ChatResponse)
async def chat_with_model(request: ChatRequest, model_factory: OllamaModelFactory = Depends(get_ollama_model_factory)):
    try:
        if not model_factory:
            raise HTTPException(status_code=404, detail="Model not found")
        response = model_factory.communicate(message=request.prompt)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
