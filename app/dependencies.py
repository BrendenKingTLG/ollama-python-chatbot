import os
from typing import Optional
from app.ollama_model_factory import OllamaModelFactory
from dotenv import load_dotenv
from app.modelfile import modelfile

load_dotenv()

ollama_model_factory: Optional[OllamaModelFactory] = None

def get_ollama_model_factory():
    global ollama_model_factory
    if ollama_model_factory is None:
        model_name = os.getenv("OLLAMA_MODEL_NAME", "default_model_name")
        ollama_model_factory = OllamaModelFactory(name=model_name, modelfile=modelfile)
    return ollama_model_factory
