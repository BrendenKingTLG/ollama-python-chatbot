import ollama
from ollama import chat

class OllamaModelFactory:
    def __init__(self, name: str, modelfile: str):
        self.name = name
        self.model = self.create_model(name, modelfile)
        self.messages = []
        
    def create_model(self, name: str, modelfile: str):
        return ollama.create(model=name, modelfile=modelfile)
    
    def communicate(self, message: str):
        self.messages.append({'role': 'user', 'content': message})
        return chat(self.name, self.messages)
