from langchain_nvidia_ai_endpoints import ChatNVIDIA
from dotenv import load_dotenv  

load_dotenv()
model = ChatNVIDIA(model="openai/gpt-oss-20b", temperature=0.9, max_completion_tokens=2000)
result = model.invoke("What is the capital of India?")
print(result.content)